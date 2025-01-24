from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='wallpapers',
    version='0.0.1',
    description='wallpapers',
    author='huang yi yi',
    author_email='363766687@qq.com',
    long_description=long_description,
    packages=['wallpaper'],
    python_requires='>=3.6',
    install_requires=[
        "winshell>=0.5.4.post1",
        "pywin32>=307.post1",
    ]
)