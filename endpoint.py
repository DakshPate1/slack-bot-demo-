from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api_endpoint():
    data = request.get_json()

    # Do some processing with the data here

    # Make API call to the server
    url = 'http://127.0.0.1:5000/slack'
    response = requests.post(url, json=data)

    # Return response from server
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
