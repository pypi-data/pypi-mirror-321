from setuptools import setup, find_packages

# Ensure proper encoding for README.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="topsis_Akhil_102203565",
    version="1.0.0",
    description="A Python package for TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Ensure correct content type
    author="Akhil Goyal",
    author_email="goyalakhil06022004@gmail.com",
    url="https://github.com/YOUR_GITHUB_USERNAME/topsis_Akhil_102203565",  # Update this
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
