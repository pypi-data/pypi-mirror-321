from setuptools import setup, find_packages

setup(
    name="cursor-agent",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cursor_agent': [
            '.cursorrules',
            '.env.example',
            'requirements.txt',
            'tools/*.py',
        ],
    },
    install_requires=[
        'requests>=2.31.0',
        'playwright>=1.40.0',
        'anthropic>=0.7.0',
        'openai>=1.3.0',
        'google-generativeai>=0.3.0',
        'python-dotenv>=1.0.0',
    ],
    entry_points={
        'console_scripts': [
            'cursor-agent=cursor_agent.main:main',
        ],
    },
    python_requires='>=3.8',
    author="grapeot",
    author_email="",
    description="A tool for initializing projects with Cursor agent capabilities",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/grapeot/devin.cursorrules",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 