import math

def haversine(lat, lng, dst_lat, dst_lng):
    lat = float(lat)
    lng = float(lng)
    dst_lat = float(dst_lat)
    dst_lng = float(dst_lng)

    d_lng = dst_lng - lng
    d_lat = dst_lat - lat

    a = (math.sin(math.radians(d_lat/2)))**2 + math.cos(math.radians(lat)) * math.cos(math.radians(dst_lat)) * (math.sin(math.radians(d_lng/2)))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    angle = math.atan2(math.fabs(d_lat), math.fabs(d_lng))
    return 3959 * c * (math.cos(angle) + math.sin(angle))
