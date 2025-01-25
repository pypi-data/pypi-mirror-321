from setuptools import setup, find_packages

setup(
    name="topsis_Akshat_102203644",
    packages=find_packages(),
    version="1.1.2",       
    author="Akshat Khurana",  # Your name
    author_email="akhurana_be22@thapar.edu",  # Your email
    description="A Python package to perform TOPSIS (Technique for Order Preference by Similarity to Ideal Solution).",
    long_description=open("README.md").read(),  # Make sure you have a README.md
    long_description_content_type="text/markdown",
    url="https://github.com/Akshatkhurana/TOPSIS-package",  # Replace with your GitHub repo URL
      # Automatically find packages in the folder
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify Python version compatibility
    install_requires=[
        "numpy",
        "pandas" # Add dependencies here (e.g., pandas, numpy, etc.)
    ],
)
