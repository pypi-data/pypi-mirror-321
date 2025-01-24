from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import os

class OpenCVBuild(build_ext):
    def run(self):
        from .cv2_gstreamer.builder import build_opencv
        build_opencv()
        super().run()

setup(
    name='cv2-gstreamer',
    version='4.5.6',  # Increment version number
    packages=find_packages(),
    install_requires=[
        'numpy>=1.19.3',
        'requests',
    ],
    description='OpenCV with GStreamer support',
    author='LeoMuuuu',
    author_email='your.email@example.com',
)
