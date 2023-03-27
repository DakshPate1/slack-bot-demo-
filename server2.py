import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/slack', methods=['POST'])
def slack_request():
    # Get the data from the request
    data = request.form

    # Send the data to the API endpoint
    api_endpoint_url = "http://127.0.0.1:5000/api"
    response = requests.post(api_endpoint_url, json=data)

    # Return the response from the API endpoint to the original Slack request
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
