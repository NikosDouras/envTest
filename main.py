from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # No need to pass the value here

@app.route('/get_env_var')  # New route for the fetch request
def get_env_var():
    env_var_value = os.getenv("ENVTEST", "Environment variable ENVTEST not found.")
    return jsonify({'env_var_value': env_var_value})  # Return as JSON

if __name__ == '__main__':
    app.run(debug=True)
