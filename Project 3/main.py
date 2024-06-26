from PIL import Image
import numpy as np
from RRT import RRT
from PRM import PRM


def load_map(file_path, resolution_scale):
    """Load map from an image and return a 2D binary numpy array
    where 0 represents obstacles and 1 represents free space
    """
    # Load the image with grayscale
    img = Image.open(file_path).convert("L")
    # Rescale the image
    size_x, size_y = img.size
    new_x, new_y = int(size_x * resolution_scale), int(
        size_y * resolution_scale
    )
    img = img.resize((new_x, new_y), Image.ANTIALIAS)

    map_array = np.asarray(img, dtype="uint8")

    # Get bianry image
    threshold = 127
    map_array = 1 * (map_array > threshold)

    # Result 2D numpy array
    return map_array


if __name__ == "__main__":
    # Load the map
    start = (200, 75)
    goal = (30, 250)
    map_array = load_map("WPI_map.jpg", 0.3)

    # Planning class
    PRM_planner = PRM(map_array)
    RRT_planner = RRT(map_array, start, goal)

    # Search with PRM
    PRM_planner.sample(n_pts=1000, sampling_method="uniform_random")
    PRM_planner.search(start, goal)
    
    PRM_planner.sample(n_pts=1000, sampling_method="uniform")
    PRM_planner.search(start, goal)
    
    PRM_planner.sample(n_pts=2000, sampling_method="gaussian")
    PRM_planner.search(start, goal)
    
    PRM_planner.sample(n_pts=20000, sampling_method="bridge")
    PRM_planner.search(start, goal)

    # Search with RRT
    RRT_planner.RRT(n_pts=1000)
