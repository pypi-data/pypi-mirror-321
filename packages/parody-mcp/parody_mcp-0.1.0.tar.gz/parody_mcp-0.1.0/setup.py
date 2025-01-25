from setuptools import setup, find_packages

setup(
    name="parody-mcp",  # Changed hyphen for PyPI naming conventions
    version="0.1.0",
    author="Patrick Ruff",
    author_email="your.email@example.com",  # Add your email
    description="An MCP tool that suggests funny, phonetically similar words",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "mcp",
        "pronouncing"
    ],
    entry_points={
        "mcp.tools": [
            "parody_mcp = parody_mcp:create_tools",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)