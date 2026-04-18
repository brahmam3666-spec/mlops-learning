from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "MLOps API is Running"

@app.route('/predict/<int:num>')
def predict(num):
    result = num * 2
    return {"prediction": result}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
