from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

MICROSERVICES = {
    "room_inventory_service": "http://localhost:5002",
    "reservation_service": "http://localhost:5003",
    "CSV_export_service": "http://localhost:5005",
    "drinks_service": "http://localhost:5004",
    "drinks_sales_service": "http://localhost:5006",
    "guest_service": "http://localhost:5001"
}

@app.route('/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    if service not in MICROSERVICES:
        return jsonify({"error": "Service not found"}), 404

    # Get the full URL for the microservice
    url = f"{MICROSERVICES[service]}/{path}"

    # Forward request with appropriate HTTP method
    response = requests.request(
        method=request.method,
        url=url,
        headers={key: value for key, value in request.headers},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )

    # Pass response back to client
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)