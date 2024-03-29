from flask import Flask, render_template
import subprocess
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dice.html')

@app.route('/ps')
def ps():
    return render_template('ps.html')

@app.route('/solution')
def solution():
    return render_template('solution.html')

@app.route('/partb')
def partb():
    return render_template('partb.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/dice')
def home():
    return render_template('dice.html')

@app.route('/parta')
def parta():
    try:
        # Get the path to the Python interpreter
        python_executable = sys.executable

        # Execute parta.py script and capture output
        result = subprocess.check_output([python_executable, '/Users/shivanibalasubramani/Desktop/sec/parta.py']).decode('utf-8')
    except Exception as e:
        # Handle any exceptions that occur during script execution
        result = f"Error: {e}"

    # Pass the result to the parta.html template
    return render_template('parta.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
