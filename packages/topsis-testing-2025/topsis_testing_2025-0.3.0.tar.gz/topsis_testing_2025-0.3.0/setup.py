from setuptools import setup, find_packages

setup(
    name="topsis_testing_2025",
    version="0.3.0",
    description="TOPSIS Python Package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/topsis",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.topsis:main",  # Ensure the `main()` function exists in topsis.py
        ],
    },
    python_requires=">=3.6",
)
