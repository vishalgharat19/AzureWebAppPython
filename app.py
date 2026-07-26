from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running',
        'python_version': os.sys.version
    })

@app.route('/api/info')
def info():
    return jsonify({
        'app_name': 'Python Web App',
        'version': '1.0.0',
        'framework': 'Flask'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
