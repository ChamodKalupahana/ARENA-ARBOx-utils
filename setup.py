from setuptools import setup, find_packages

setup(
    name="arena_arbox_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
    ],
    author="Chamod Kalupahana",
    description="Utility functions for ARENA ARBOx",
    python_requires=">=3.7",
)
