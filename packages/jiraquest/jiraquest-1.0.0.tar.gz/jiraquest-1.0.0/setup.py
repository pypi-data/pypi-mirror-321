from setuptools import setup, find_packages

setup(
    name="jiraquest",
    version="1.0.0",
    description="A tool for analyzing Jira comments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rainbowgore/JiraQuest",
    license="MIT",
    packages=find_packages(where="src"),  # Finds all Python files directly in `src`
    package_dir={"": "src"},  # Maps the `src` directory as the root for packages
    py_modules=["cli", "cli_integration", "jira_comments_script", "slack_integration", "tableau_integration"],  # Explicitly list all modules
    include_package_data=True,
    install_requires=[
        "pandas>=1.5.0",
        "requests>=2.28.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "jiraquest=cli:main",  # Maps `cli.py` as the entry point for the CLI
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)