import logging as log
import geopandas as gpd
from pathlib import Path
from shapely.wkt import loads

log.basicConfig(
    level = log.INFO,
    # filename = local_config.log_path,
    format = "%(levelname)s: %(message)s")

def is_wkt(text: str) -> bool:
    """Check if the input string is in WKT format."""
    try:
        loads(text)
        return True
    except Exception:
        return False

def to_openeo_wkt(aoi: Path | str | None) -> str | None:
    """Returns WKT coordinates of area extent"""
    if aoi is None:
        return None

    if isinstance(aoi, str):
        if is_wkt(aoi):
            return aoi
        else:
            try:
                gdf = gpd.read_file(aoi)
                return gdf.unary_union.wkt
            except Exception as e:
                log.info(f"{e.__class__.__name__}: {e} \n"
                         "AOI will not be considered for this query")
                return None

    try:
        gdf = gpd.read_file(aoi)
        return gdf.unary_union.wkt
    except Exception as e:
        log.info(f"{e.__class__.__name__}: {e} \n"
                 "AOI will not be considered for this query")
        return None
