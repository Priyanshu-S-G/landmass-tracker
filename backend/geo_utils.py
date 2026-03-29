from config import BBOX_DELTA

def get_bbox(lat: float, lon: float):
    return {
        "min_lat": lat - BBOX_DELTA,
        "max_lat": lat + BBOX_DELTA,
        "min_lon": lon - BBOX_DELTA,
        "max_lon": lon + BBOX_DELTA
    }