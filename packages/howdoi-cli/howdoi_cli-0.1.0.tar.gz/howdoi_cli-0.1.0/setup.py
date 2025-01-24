from setuptools import setup, find_packages

setup(
    name="howdoi-cli",
    version="0.1.0",
    author="Wojtek Grabski",
    author_email="mostlydev@mostlydev.com",
    description="AI-powered CLI tool for shell commands",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/mostlydev/howdoi-cli",
    packages=find_packages(),
    install_requires=[
        "click",
        "pyyaml",
        "python-dotenv",
        "anthropic",
        "openai"
    ],
    entry_points={
        "console_scripts": [
            "how=howdoi.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
