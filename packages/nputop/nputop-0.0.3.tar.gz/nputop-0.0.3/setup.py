import os
from setuptools import setup, find_packages

repo_root = os.path.dirname(os.path.abspath(__file__))

# build long description
def build_long_description():
    readme_path = os.path.join(os.path.abspath(repo_root), "README.md")

    with open(readme_path, encoding="utf-8") as f:
        return f.read()

setup(
    name='nputop',
    version='0.0.3',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nputop = nputop.main:main',
        ],
    },
    install_requires=[
        'textual',
        'psutil',
        'rich'
    ],
    long_description=build_long_description(),
    long_description_content_type="text/markdown",
    description='NPU monitoring tool with TUI interface',
    author='Rvelamen',
    author_email='your.email@example.com',
    url='https://github.com/Rvelamen/nputop',
)