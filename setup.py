from setuptools import setup, find_packages

setup(
    name="cuna",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "networkx>=2.6.0",
        "matplotlib>=3.4.0",
        "pyyaml>=6.0",
        "requests>=2.25.0",
        "numpy>=1.20.0",
        "tensorflow>=2.8.0",  # For AI-powered generation
        "transformers>=4.15.0",  # For NLP processing
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.5b2",
            "flake8>=3.9.0",
        ]
    },
    author="Cuna Team",
    author_email="info@cunaproject.com",
    description="AI-powered tool that transforms natural language descriptions into network topologies",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cunaproject/cuna",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)

