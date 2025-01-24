from setuptools import setup, find_packages

setup(
    name="praveengcs-test-my-library-new",  # Replace with your library's name
    version="0.1",
    author="Praveen",
    author_email="your_email@example.com",
    description="A brief description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/my_library_new",  # Optional: Link to your project repo
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Specify minimum Python version
)
