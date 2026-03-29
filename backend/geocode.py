import requests

def get_coordinates(place: str):
  url = "https://nominatim.openstreetmap.org/search"
    
  params = {
    "q": place,
    "format": "json",
    "limit": 1
  }
  
  headers = {
    "User-Agent": "landmass-tracker-app"
  }

  response = requests.get(url, params=params, headers=headers)
  
  if response.status_code != 200:
    return {"error": "Geocoding request failed"}
  
  data = response.json()
  
  if not data:
    return {"error": "Place not found"}
  
  return {
    "lat": float(data[0]["lat"]),
    "lon": float(data[0]["lon"])
  }