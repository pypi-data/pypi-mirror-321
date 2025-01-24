from setuptools import setup, find_packages

setup(
    name="streamlit-crewai-process-output",
    version="0.1.1",
    author="Tony Kipkemboi",
    author_email="iamtonykipkemboi@gmail.com",
    description="A component for displaying CrewAI agent process outputs in Streamlit applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tonykipkemboi/streamlit-crewai-process-output",
    project_urls={
        "Bug Tracker": "https://github.com/tonykipkemboi/streamlit-crewai-process-output/issues",
        "Source Code": "https://github.com/tonykipkemboi/streamlit-crewai-process-output",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10,<3.13",
    install_requires=[
        "streamlit>=1.41.0",
        "crewai>=0.95.0",
        "crewai-tools>=0.25.8",
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-asyncio>=0.21.0',
            'pytest-cov>=4.1.0',
        ],
    },
)
