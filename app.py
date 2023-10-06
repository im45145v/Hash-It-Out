from flask import Flask, render_template, request, jsonify, redirect, url_for, session


app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)