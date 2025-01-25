import open3d as o3d
import json
import numpy as np
from sklearn.decomposition import PCA

class Obstacle_Detection:
    def __init__(self, 
                 center: np.ndarray = np.array([64, 64, 20]), 
                 max_distance: float = 50, 
                 num_rays: int = 15,
                 angle_range: float = 45,
                 ):
        
        self.center = center
        self.max_distance = max_distance
        self.num_rays = num_rays
        self.angle_range = self.degree_to_radian(angle_range)
        self.mesh = o3d.geometry.TriangleMesh()

    def degree_to_radian(self, degree: float) -> float:
        """
        Convert an angle from degrees to radians.

        Parameters:
            degree (float): Angle in degrees.

        Returns:
            float: Angle in radians.
        """
        return degree * np.pi / 180.0

    def load_voxel_map_from_json(self, file_path: str):
        """
        Load a voxel map from a JSON file.
        
        Parameters:
            file_path (str): Path to the JSON file.
            
        Returns:
            dict: The voxel map as a dictionary.
        """
        with open(file_path) as f:
            return json.load(f)
        
    def extract_positions_and_indices_from_voxel_map(self, voxel_map: dict):
        """
        Extract positions and indices from a voxel map.

        Parameters:
            voxel_map (dict): The voxel map as a dictionary.

        Returns:
            np.ndarray: Array of positions with shape (N, 3).
            np.ndarray: Array of indices with shape (M, 3).
        """
        positions = np.array(voxel_map["data"]["positions"]).reshape(-1, 3)
        indices = np.array(voxel_map["data"]["indices"]).reshape(-1, 3)

        return positions, indices
        
    def get_scene_from_voxel_map(self, voxel_map: dict):
        # Extract positions and indices
        positions, indices = self.extract_positions_and_indices(voxel_map)

        # Create a TriangleMesh
        self.mesh.vertices = o3d.utility.Vector3dVector(positions)
        self.mesh.triangles = o3d.utility.Vector3iVector(indices)
        self.mesh.compute_vertex_normals()

        # Create a scene for raycasting
        scene = o3d.t.geometry.RaycastingScene()
        scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(self.mesh))

        return scene
    
    def get_dominant_direction(self, positions: np.ndarray, render: False) -> np.ndarray:
        """
        Compute the dominant direction of a point cloud.

        Parameters:
            positions (np.ndarray): Array of positions with shape (N, 3).
            render (bool): Whether to render the dominant direction arrow.

        Returns:
            np.ndarray: The dominant direction vector.
            o3d.geometry.TriangleMesh (condition: render=True): The arrow representing the dominant direction.
        """
        pca = PCA(n_components=3)
        pca.fit(positions)

        # The first principal component represents the dominant direction
        dominant_direction = pca.components_[0]
        dominant_direction = [dominant_direction[0], dominant_direction[1]]

        if not render:
            # Normalize the dominant direction
            dominant_direction = np.array(dominant_direction + [0])
            dominant_direction = dominant_direction / np.linalg.norm(dominant_direction)
            # Rotate the dominant direction to the XY plane
            dominant_direction = np.cross(dominant_direction, [0, 0, 1])
            dominant_direction = dominant_direction / np.linalg.norm(dominant_direction)

            return dominant_direction
        
        else:
            arrow = o3d.geometry.TriangleMesh.create_arrow(
                cylinder_radius=1,
                cone_radius=2,
                cylinder_height=10.0,
                cone_height=5
            )
            arrow.paint_uniform_color([1, 0, 0])  # Red color for the arrow
            arrow.translate(self.center)  # Place at the origin
            # arrow.rotate(o3d.geometry.get_rotation_matrix_from_xyz(dominant_direction), center=center)

            # Place the arrow initially in the XY plane
            rotation_matrix = o3d.geometry.get_rotation_matrix_from_axis_angle([np.pi / 2, 0, 0])  # Rotation around X-axis
            arrow.rotate(rotation_matrix, center=self.center)

            # Compute the angle to rotate within the XY plane
            angle = np.arctan2(dominant_direction[1], dominant_direction[0])  # Angle with respect to +x-axis

            # Rotate the arrow around the Z-axis by the computed angle
            rotation_matrix = o3d.geometry.get_rotation_matrix_from_axis_angle([0, 0, angle])
            arrow.rotate(rotation_matrix, center=self.center)

            # Normalize the dominant direction
            dominant_direction = np.array(dominant_direction + [0])
            dominant_direction = dominant_direction / np.linalg.norm(dominant_direction)
            # Rotate the dominant direction to the XY plane
            dominant_direction = np.cross(dominant_direction, [0, 0, 1])
            dominant_direction = dominant_direction / np.linalg.norm(dominant_direction)

            return dominant_direction, arrow
    
    def preprocess_voxel_map(self, voxel_map: dict, render: bool = False):
        """
        Preprocess a voxel map by extracting positions and indices and creating a scene for raycasting.

        Parameters:
            voxel_map (dict): The voxel map as a dictionary.
            render (bool): Whether to render the dominant direction arrow.

        Returns:
            o3d.t.geometry.RaycastingScene: The scene for raycasting.
            np.ndarray: The dominant direction vector.
            o3d.geometry.TriangleMesh (condition: render=True): The arrow representing the dominant direction.
        """
        # Extract positions and indices
        positions, indices = self.extract_positions_and_indices_from_voxel_map(voxel_map)

        # Create a TriangleMesh
        self.mesh.vertices = o3d.utility.Vector3dVector(positions)
        self.mesh.triangles = o3d.utility.Vector3iVector(indices)
        self.mesh.compute_vertex_normals()

        # Create a scene for raycasting
        scene = o3d.t.geometry.RaycastingScene()
        scene.add_triangles(o3d.t.geometry.TriangleMesh.from_legacy(self.mesh))

        if not render:
            dominant_direction = self.get_dominant_direction(positions, render=False)
            return scene, dominant_direction
        
        else:
            dominant_direction, arrow = self.get_dominant_direction(positions, render=True)
            return scene, dominant_direction, arrow

    def generate_rays_within_angle(self, 
                                   center: np.ndarray, 
                                   base_direction: list, 
                                   angle_range: float, 
                                   num_rays: int
                                   ) -> np.ndarray:
        """
        Generate rays within a given angle range around a base direction.

        Parameters:
            center (array-like): Origin of the rays.
            base_direction (array-like): Base direction for the rays.
            angle_range (float): Angle range in radians (e.g., np.pi / 4 for ±45°).
            num_rays (int): Number of rays to generate within the angle range.

        Returns:
            np.ndarray: Array of rays with shape (num_rays, 6).
        """
        # Normalize the base direction
        base_direction = np.array(base_direction)
        base_direction = base_direction / np.linalg.norm(base_direction)

        # Compute perpendicular vector in the XY plane
        perpendicular_vector = np.array([-base_direction[1], base_direction[0], 0])

        # Generate angles within the range [-angle_range, +angle_range]
        angles = np.linspace(-angle_range, angle_range, num_rays)

        rays = []
        for angle in angles:
            # Compute rotated direction
            rotated_direction = (
                np.cos(angle) * base_direction + np.sin(angle) * perpendicular_vector
            )
            rotated_direction = rotated_direction / np.linalg.norm(rotated_direction)

            # Append the ray (origin and direction)
            rays.append(np.hstack([center, rotated_direction]))

        rays = np.array(rays)

        return rays
    
    def is_path_clear(self,
                      dominant_direction: list, 
                      relative_walking_vector: list,
                      scene: o3d.t.geometry.RaycastingScene = None,
                      threshold: float = 0.1,
                      render: bool = False):
        """
        Check if there is a clear path in a direction specified relative to the dominant direction.

        Parameters:
            center (array-like): Origin of the ray (e.g., robot's center position).
            dominant_direction (array-like): Dominant direction vector in the XY plane.
            relative_walking_vector (array-like): 2D vector specifying the walking direction relative to the dominant direction.
            mesh (o3d.geometry.TriangleMesh): The mesh to test for ray intersections.
            max_distance (float): Maximum distance for raycasting.
            
        Returns:
            bool: True if the path is clear, False if an obstacle is found.
        """

        # Compute the perpendicular vector in the XY plane
        perpendicular_vector = np.cross(dominant_direction, [0, 0, 1])
        perpendicular_vector = perpendicular_vector / np.linalg.norm(perpendicular_vector)

        # Compute the absolute walking direction
        relative_walking_vector = np.array(relative_walking_vector)
        absolute_walking_direction = (
            relative_walking_vector[0] * dominant_direction
            + relative_walking_vector[1] * perpendicular_vector
        )
        absolute_walking_direction = absolute_walking_direction / np.linalg.norm(absolute_walking_direction)

        rays = self.generate_rays_within_angle(self.center, absolute_walking_direction, self.angle_range, self.num_rays)
        ray_tensor = o3d.core.Tensor(rays, dtype=o3d.core.Dtype.Float32)

        # Cast rays and collect intersection points
        results = scene.cast_rays(ray_tensor)

        # Count the number of hits
        num_hits = np.sum(results["t_hit"].numpy() < self.max_distance)

        if num_hits / self.num_rays > threshold:
            path_is_clear = False
        else:
            path_is_clear = True

        if render:
            # Visualize rays
            ray_lines = []
            ray_colors = []

            for i, result in enumerate(results["t_hit"].numpy()):
                origin = rays[i, :3]
                direction = rays[i, 3:]
                if result < self.max_distance:
                    # Hit: Get intersection point
                    hit_point = origin + min(result, self.max_distance) * direction
                    ray_lines.append([origin, hit_point])
                    ray_colors.append([1, 0, 0])  # Red for hit rays
                else:
                    # Miss: Extend ray to max distance
                    ray_lines.append([origin, origin + direction * self.max_distance])
                    ray_colors.append([0, 1, 0])  # Green for miss rays

            return path_is_clear, ray_lines, ray_colors

        return path_is_clear
    
    def show_voxel_map(self, file_path: str = "./data/dump.json"):
        voxel_map = self.load_voxel_map_from_json(file_path)

        # Extract positions and indices
        positions, indices = self.extract_positions_and_indices_from_voxel_map(voxel_map)

        # Create a TriangleMesh
        self.mesh.vertices = o3d.utility.Vector3dVector(positions)
        self.mesh.triangles = o3d.utility.Vector3iVector(indices)
        self.mesh.compute_vertex_normals()

        # Visualize the mesh
        o3d.visualization.draw_geometries([self.mesh])
    
    def show_voxel_map_with_obstacle_detection(self, file_path: str = "./data/dump.json", move_direction: list = [1, 0, 0], threshold: float = 0.1):
        voxel_map = self.load_voxel_map_from_json(file_path)

        # Extract positions and indices
        self.positions, self.indices = self.extract_positions_and_indices_from_voxel_map(voxel_map)
        scene, dominant_direction, arrow = self.preprocess_voxel_map(voxel_map, True)
        
        ########################################

        path_is_clear, self.ray_lines, self.ray_colors = self.is_path_clear(dominant_direction, move_direction, scene, threshold=threshold, render=True)
        print("\n"*1)
        print("Path is clear:", path_is_clear)
        print("\n"*2)

        line_set = o3d.geometry.LineSet()
        line_points = np.array(self.ray_lines).reshape(-1, 3)
        line_indices = [[2 * i, 2 * i + 1] for i in range(len(self.ray_lines))]
        line_set.points = o3d.utility.Vector3dVector(line_points)
        line_set.lines = o3d.utility.Vector2iVector(line_indices)
        line_set.colors = o3d.utility.Vector3dVector(self.ray_colors)

        # Visualize the mesh and rays
        o3d.visualization.draw_geometries([obj for obj in [self.mesh, line_set, arrow] if obj is not None])