import numpy as np
import pandas as pd

import geopandas as gpd
from shapely import wkb, vectorized
from shapely.geometry import Point


class CityLocator:
    def __init__(self, shp_file: str):
        """
        :des 
            通过 feater 文件确定城市位置。
            feater 文件从天地图下载, 转换。
            通过构造 Point 和 Polygon 的关系来批量确定城市位置。
        :param shp_file: shp文件路径 
        """
        _df = pd.read_feather(shp_file)
        
        if 'geometry' not in _df.columns or 'name' not in _df.columns:
            raise ValueError("请检查文件是否包含geometry, name列")

        _df['geometry'] = _df['geometry'].apply(lambda wkb_geom: wkb.loads(wkb_geom))
        self.map = gpd.GeoDataFrame(_df, geometry='geometry')
        self.map = self.map.set_crs("EPSG:4326")

    def get_cityname(self, lat, lon):
        # 单个float 和 批量 list 区分, 直接 numpy 转换
        # 将输入转换为 numpy 数组以便统一处理
        lat_array, lon_array = np.asarray(lat), np.asarray(lon)

        # 确保纬度经度数组形状一致
        if lat_array.shape != lon_array.shape:
            raise ValueError(f"经纬度长度不一致, lat: {lat_array.shape}, lon: {lon_array.shape}")

        # 创建 Point 对象
        # points = [Point(lon, lat) for lon, lat in zip(lon_array, lat_array)]
        points = gpd.points_from_xy(lon_array, lat_array)

        # 将点列表转换为 GeoDataFrame
        points_gdf = gpd.GeoDataFrame(geometry=points, crs="EPSG:4326")

        
        # 使用空间连接（sjoin）进行批量查询
        joined_gdf = gpd.sjoin(points_gdf, self.map, how="left", predicate="within")

        # 提取城市名称
        results = joined_gdf["name"].fillna("NULL").tolist()

        return results