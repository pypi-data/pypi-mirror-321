from setuptools import setup, find_packages

setup(
    name="gtrbench",
    version="0.0.1",
    author="Ali Shazal (with Michael Lu, Xiang Zheng, Juno Lee, Arihant Choudhary)",
    author_email="ali.shazal@berkeley.edu",
    description="A benchmark to evaluate implicit reasoning in LLMs using guess-the-rule games",
    long_description=open("README.md").read(),  # Ensure you have a README.md file
    long_description_content_type="text/markdown",
    packages=find_packages(where="."),  # Finds all packages under the current directory
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "openai==1.56.0",
        "python-dotenv==1.0.0",
        "nltk==3.8.1",
        "anthropic==0.3.0",
        "retry==0.9.2",
        "google-generativeai==0.3.2",
    ],
    extras_require={
        "test": ["pytest==7.3.1", "httpx==0.24.0"],
        "dev": ["black==23.7.0", "flake8==6.1.0"],
    },
    keywords=["benchmark", "llm", "implicit reasoning", "guess-the-rule games", "gtrbench"],
    license="MIT",
)
