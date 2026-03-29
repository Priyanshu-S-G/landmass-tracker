from flask import Flask, request, jsonify

from geocode import get_coordinates
from geo_utils import get_bbox

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "Landmass Tracker API running"
    })

@app.route("/geocode", methods=["POST"])
def geocode_route():
    data = request.get_json()

    if not data or "place" not in data:
        return jsonify({"error": "Missing 'place' in request"}), 400

    place = data["place"]
    result = get_coordinates(place)

    if "error" in result:
        return jsonify(result), 400
    
    bbox = get_bbox(result["lat"], result["lon"])

    return jsonify({
    "lat": result["lat"],
    "lon": result["lon"],
    "bbox": bbox
    })

if __name__ == "__main__":
    app.run(debug=True)