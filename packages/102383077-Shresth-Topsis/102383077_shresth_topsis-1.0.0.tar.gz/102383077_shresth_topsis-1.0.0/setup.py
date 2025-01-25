from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="102383077_Shresth_Topsis",  
    version="1.0.0",  
    author="Shresth Raj", 
    author_email="shresthraj77@gmail.com",  
    description="A Python implementation of the TOPSIS algorithm for multi-criteria decision analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis",  # Replace with the URL of your project repository
    # project_urls={
    #     "Bug Tracker": "https://github.com/yourusername/topsis/issues",  # Replace with issue tracker URL
    # },
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",  # Use your desired license
    #     "Operating System :: OS Independent",
    # ],
    packages=find_packages(),  # Automatically finds packages in the current directory
    # python_requires=">=3.6",  # Specify Python versions supported
    # install_requires=[
    #     "numpy>=1.21.0",  # Add dependencies
    #     "pandas>=1.3.0",
    # ],
    # entry_points={
    #     "console_scripts": [
    #         "topsis=topsis:main",  # Replace 'topsis' with the command and `topsis:main` with the entry function
    #     ],
    # },
)
