from setuptools import setup, find_packages

setup(
    name="multiframe",
    version="0.1.0",
    description="A multi-agent framework for various AI tasks",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "groq",
        "google-api-python-client",
        "youtube-transcript-api",
        "wikipedia-api",
        "beautifulsoup4",
        "requests",
        "pandas",
        "PyPDF2",
        "langchain-community",
        "langchain",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
