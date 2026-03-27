from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "🚀 Flask app is running successfully!"

# Health check route
@app.route('/health')
def health():
    return jsonify({
        "status": "OK",
        "message": "App is healthy 💚"
    })

# Sample ML prediction route (dummy)
@app.route('/predict')
def predict():
    # Dummy prediction logic
    result = {
        "input": "sample data",
        "prediction": "positive",
        "confidence": 0.92
    }
    return jsonify(result)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)