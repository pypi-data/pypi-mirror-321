import os
import subprocess
import sys
import requests
import tarfile
from pathlib import Path

def download_opencv():
    home = str(Path.home())
    os.chdir(home)  # Change to home directory for build
    
    # Download minimal OpenCV source
    url = "https://github.com/opencv/opencv/archive/refs/tags/4.5.4.tar.gz"
    response = requests.get(url, stream=True)
    with open("opencv.tar.gz", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Extract
    with tarfile.open("opencv.tar.gz", "r:gz") as tar:
        tar.extractall()
    os.remove("opencv.tar.gz")

def build_opencv():
    home = str(Path.home())
    opencv_dir = os.path.join(home, 'opencv-4.5.4')
    
    if not os.path.exists(opencv_dir):
        download_opencv()

    build_dir = os.path.join(opencv_dir, 'build')
    os.makedirs(build_dir, exist_ok=True)
    
    cmake_args = [
        'cmake',
        '-D', 'CMAKE_BUILD_TYPE=RELEASE',
        '-D', 'WITH_GSTREAMER=ON',
        '-D', 'WITH_FFMPEG=ON',
        # Minimize size
        '-D', 'BUILD_TESTS=OFF',
        '-D', 'BUILD_PERF_TESTS=OFF',
        '-D', 'BUILD_EXAMPLES=OFF',
        '-D', 'INSTALL_TESTS=OFF',
        '-D', 'INSTALL_C_EXAMPLES=OFF',
        '-D', 'INSTALL_PYTHON_EXAMPLES=OFF',
        '-D', 'BUILD_opencv_python2=OFF',
        '-D', 'BUILD_opencv_java=OFF',
        '-D', 'BUILD_opencv_js=OFF',
        '-D', 'BUILD_opencv_apps=OFF',
        '-D', 'BUILD_LIST=core,imgproc,imgcodecs,videoio,highgui',
        '-D', f'PYTHON_EXECUTABLE={sys.executable}',
        '..'
    ]
    
    subprocess.check_call(cmake_args, cwd=build_dir)
    subprocess.check_call(['make', '-j8'], cwd=build_dir)
