from setuptools import setup, find_packages


with open("README.md", 'r') as f:
    description = f.read()

setup(
    name='intellx_api',
    version='0.0.0.0',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'load_dotenv'
    ],
    entry_points={
        'console_scripts': [
            'intellx=intellx.cli:main',
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)