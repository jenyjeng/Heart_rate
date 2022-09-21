import json
from flask import Flask, jsonify,request
app = Flask(__name__)

record=[

    {
	    "heart_id": ["12345"],
	    "date": ["9/21/2022"],
	    "heart_rate": ["60 - 100 bpm"]
}
]
@app.route('/record', methods=['GET'])
def get():
    return jsonify(record)
    
if __name__ == '__main__':
    app.run()