from setuptools import setup, find_packages

setup(
    name="heartlens_dataset_lib",                    # Package name
    version="0.1.0",                                 # Initial version
    author="Mitchell Klusty",                        # Author name
    author_email="mitchell.klusty@uky.edu",          # Author email
    description="Dataset Loader for Heartlens",      # Short description
    long_description=open("README.md").read(),       # Long description (optional)
    long_description_content_type="text/markdown",   # README content type
    url="https://github.com/innovationcore/heartlens_dataset_library",  # Project URL
    packages=find_packages(),                        # Automatically discover modules
    install_requires=[           # Dependencies
        "torch>=1.9.0",
        "numpy>=1.21.0",
        "zarr>=2.12.0"
    ],
    classifiers=[                           # Metadata classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",                # Minimum Python version
)
