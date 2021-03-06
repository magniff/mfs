import setuptools


setuptools.setup(
    name="mfs",
    description="Python mapping based filesystem.",
    version="0.1",
    license="GLWTPL",
    platforms=["unix"],
    author="magniff",
    url="https://github.com/magniff/mfs",
    install_requires=["fusepy", "watch"],
    packages=["mfs",],
    zip_safe=False,
)

