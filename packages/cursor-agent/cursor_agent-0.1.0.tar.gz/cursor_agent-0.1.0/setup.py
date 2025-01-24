from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cursor-agent",
    version="0.1.0",
    author="TOKYO",
    author_email="dongjin.xu.jill@gmail.com",
    description="Transform Cursor IDE into a Devin-like experience with agentic capabilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/crazywowmen/devin.cursorrules",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.31.0",
        "playwright>=1.40.0",
        "anthropic>=0.7.0",
        "openai>=1.3.0",
        "google-generativeai>=0.3.0",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "cursor-agent=cursor_agent.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "cursor_agent": [
            ".cursorrules",
            ".env.example",
            "tools/*.py",
        ],
    },
) 