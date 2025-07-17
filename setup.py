from setuptools import setup, find_packages

setup(
    name="terraform-gpt-plan-explainer",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "openai>=1.0.0",
        "click",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "terraform-plan-explainer=cli:main",
        ],
    },
    python_requires=">=3.9",
    author="Your Name",
    description="A CLI tool to explain Terraform plans using GPT and generate diagrams.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)