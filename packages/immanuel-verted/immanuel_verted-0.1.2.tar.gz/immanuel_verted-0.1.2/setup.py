from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="immanuel-verted",  # Your unique package name
    version="0.1.2",        # Start with 0.1.0 for first release
    author="Your Name",
    author_email="your.email@example.com",
    description="A modified version of immanuel with polar coordinate support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EthanAbra/immanuel-verted",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pyswisseph>=2.0.0",
        "pendulum>=2.0.0",
        "python-dateutil>=2.8.0",
        "pytz",
        # Add any other dependencies you need
    ],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'pytest-cov>=2.0',
            'black',
            'flake8',
            'mypy',
            'twine',
            'wheel',
        ],
    },
)