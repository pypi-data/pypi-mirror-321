from setuptools import setup, find_packages

setup(
    name="wztools",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # 公共依赖
        "uuid",
    ],
    extras_require={
        'services': ['numpy', 'pandas', 'geopandas', 'shapely', 'pyproj', 'pyarrow'],  # 额外依赖
    },
)