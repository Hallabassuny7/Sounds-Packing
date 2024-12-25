from flask import Flask, render_template, request, redirect, url_for
import io
import sys

app = Flask(__name__)

# Algorithm functions
def algorithm_a():
    print("Algorithm A is running...")
    print("This is the output from Algorithm A.")
    return "Algorithm A has completed successfully."

def algorithm_b():
    print("Algorithm B starts now.")
    print("Processing data with Algorithm B...")
    return "Algorithm B has completed its execution."

def algorithm_c():
    print("Executing Algorithm C.")
    print("Algorithm C is designed for advanced data analysis.")
    return "Algorithm C execution finished."

# Map algorithms to functions
algorithms = {
    'A': algorithm_a,
    'B': algorithm_b,
    'C': algorithm_c
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_choice = request.form.get('test_choice')
        algorithm_choice = request.form.get('algorithm_choice')

        if not test_choice or not algorithm_choice:
            return render_template('index.html', error="Please make sure to select both a sample test and an algorithm.")

        # Redirect output to a string buffer
        buffer = io.StringIO()
        sys.stdout = buffer

        # Call the selected algorithm function
        result = algorithms[algorithm_choice]()

        # Restore standard output
        sys.stdout = sys.__stdout__

        # Get the buffered output
        output = buffer.getvalue()

        return render_template('confirm.html', test_choice=test_choice, algorithm_choice=algorithm_choice, output=output, result=result)
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    action = request.form.get('action')
    if action == 'restart':
        return redirect(url_for('index'))
    return "Thank you for using the application! Goodbye."

if __name__ == '__main__':
    app.run(debug=True)
