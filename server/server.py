from flask import Flask, request, jsonify, render_template
import os

# ============================================================================
# IMPORT CONFIGURATION FOR LOCAL vs DEPLOYMENT
# ============================================================================
# FOR DEPLOYMENT (Render.com, Heroku, etc.):
#   Use: from server import util
#   This works because gunicorn treats 'server' as a Python package
#
# FOR LOCAL DEVELOPMENT (running: python server/server.py):
#   Use: import util
#   This works when running from project root because both files are in same directory
# ============================================================================

# DEPLOYMENT: Uncomment this line and comment out the next one
from . import util


# LOCAL DEVELOPMENT: Uncomment this line and comment out the one above
# import util

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, static_folder=os.path.join(BASE_DIR, "static"), template_folder=os.path.join(BASE_DIR, "templates"))

util.load_saved_artifacts()

@app.route("/")
def home():
    return render_template("app.html")

@app.route("/get_location_names")
def get_location_names():
    return jsonify({
        "locations": util.get_location_names()
    })

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():
    sqft = float(request.form["total_sqft"])
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])
    location = request.form["location"]

    price = util.get_estimated_price(location, sqft, bhk, bath)
    return jsonify({"estimated_price": price})

# ============================================================================
# LOCAL DEVELOPMENT SERVER
# ============================================================================
# This block runs the Flask development server when you execute:
#   python server/server.py
#
# FOR LOCAL DEVELOPMENT: Keep this block uncommented
# FOR DEPLOYMENT: This block is ignored (gunicorn handles the server)
# ============================================================================
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)









# from flask import Flask, request, jsonify
# import util
# app = Flask(__name__)

# # 🔥 LOAD MODEL & COLUMNS ON SERVER START
# util.load_saved_artifacts()

# @app.route('/get_location_names')
# def get_location_names():
#     response = jsonify({
#         'locations': util.get_location_names()
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
    
#     return response
#     # return "Bibek"
    

# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(location, total_sqft,bhk,bath)
#     })
    
#     response.headers.add('Access-Control-Allow-Origin', '*')
    
#     return response


# if __name__ == "__main__":
#     print("Starting Python Flask Server For Home Price Prediction..")
#     app.run()