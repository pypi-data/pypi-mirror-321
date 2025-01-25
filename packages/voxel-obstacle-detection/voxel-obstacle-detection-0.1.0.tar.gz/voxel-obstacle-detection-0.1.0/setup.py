from setuptools import setup, find_packages

setup(
    name="voxel-obstacle-detection",  # Package name (used in pip install)
    version="0.1.0",  # Initial version
    description="A Python package for obstacle detection in voxel maps using Open3D and raycasting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexandre Correia",
    author_email="alexandre17dc@gmail.com",
    url="https://github.com/alexandre-dc/voxel-object-detection",  # GitHub or project URL
    license="MIT",  # License type
    packages=find_packages(exclude=["examples", "tests"]),  # Automatically find packages
    install_requires=[
        "numpy<2.0.0",
        "open3d>=0.18.0",
        "scikit-learn",
    ],  # Dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)