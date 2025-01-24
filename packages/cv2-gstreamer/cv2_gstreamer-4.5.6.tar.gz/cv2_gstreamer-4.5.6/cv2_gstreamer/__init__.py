import os
import importlib.util
from pathlib import Path

def _initialize():
    # Get the user's home directory for build location
    home = str(Path.home())
    build_dir = os.path.join(home, 'opencv-4.5.4/build')
    cv2_path = os.path.join(build_dir, 'lib/cv2.so')

    if not os.path.exists(cv2_path):
        from .builder import build_opencv
        build_opencv()

    # Load the built module
    spec = importlib.util.spec_from_file_location('cv2', cv2_path)
    if spec is None:
        raise ImportError(f"Failed to load OpenCV from {cv2_path}")
    
    cv2 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cv2)
    return cv2

# Initialize the module
try:
    cv2 = _initialize()
except Exception as e:
    raise ImportError(f"Failed to initialize OpenCV: {str(e)}")
