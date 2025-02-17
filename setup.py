from setuptools import setup, find_packages

# Read the README file for long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dooGL",  # The name of your package
    version="0.2.3",  # Initial version
    packages=find_packages(),  # Automatically discover all modules
    python_requires='>=3.6',  # Minimum Python version requirement
    include_package_data=True,  # Automatically include files specified in package_data
    package_data={
        'dooGL.core._2d': ['doGl_logo.png'],  # Specify the path to your image
    },
    install_requires=[
        'PyOpenGL',        # OpenGL for Python
        'PyOpenGL_accelerate',  # Optional acceleration of OpenGL functions
        'pygame',          # Pygame library for game development
        'Pillow',          # Python Imaging Library (PIL fork)
        # Add any other dependencies your project requires here
    ],
     long_description=long_description,  # Use the content of README.md
     long_description_content_type="text/markdown",  # Specify that README is in Markdown format
     url="https://github.com/MahmoudHanyFathalla/dooGL-Python-Package",
)
