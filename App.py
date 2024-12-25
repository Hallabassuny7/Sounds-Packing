from flask import Flask, render_template, request, redirect, url_for
import io
import sys
from WorstFit import *
from HarmonicPartitioning import Harmonic_Partitioning
from FileHandling import *
from FolderFilling import *
from fractionalPacking import *
from pack import *
from BestFit import *
from NextFit import *
from FirstFit import *

app = Flask(__name__)
filehandler = FileHandlingClass()

# Map algorithms to functions
algorithms = {
    'Worst Fit Linear Search': WorstFit_LinearSearch,
    'Worst Fit Linear Search Decreasing': WorstFit_LinearSearch_Decreasing,
    'Worst Fit Priority Queue': WorstFit_PriorityQueue,
    'Worst Fit Priority Queue Decreasing':WorstFit_PriorityQueue_Decreasing,
    'Harmonic Partitioning':Harmonic_Partitioning,
    'Folder Filling':folder_filling,
    'Fractional Packing':fractional_packing,
    'Pack':pack,
    'Best Fit Dynamic Programming':best_fit_dp,
    'Best Fit Priority Queue Decreasing':best_fit_with_priority_queue,
    'Next Fit Divide & Conquer':next_fit_D_C,
    'Next Fit Greedy':next_fit_greedy,
    'First Fit Linear Search Decreasing':FirstFit
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        test_choice = request.form.get('test_choice')
        algorithm_choice = request.form.get('algorithm_choice')
        folder_capacity = request.form.get('folder_capacity', type=int)
        folder_location=rf"Sample Tests\{test_choice}\Audios"
        files = filehandler.readfile(rf"{folder_location}Info.txt")
        output_location=rf"Sample Tests"
        if not test_choice or not algorithm_choice or folder_capacity is None:
            return render_template('index.html', error="Please make sure to select both a sample test, an algorithm, and enter folder capacity.")
    
        # Redirect output to a string buffer
        buffer = io.StringIO()
        sys.stdout = buffer

        # Call the selected algorithm function with folder capacity
        folders = algorithms[algorithm_choice](files,folder_capacity)
        filehandler.Output(folder_location,output_location,folders,algorithm_choice,test_choice)

        # Restore standard output
        sys.stdout = sys.__stdout__

        # Get the buffered output
        output = buffer.getvalue()

        return render_template('confirm.html', test_choice=test_choice, algorithm_choice=algorithm_choice, folder_capacity=folder_capacity, output=output, result=folders)
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def confirm():
    action = request.form.get('action')
    if action == 'restart':
        return redirect(url_for('index'))
    return "Thank you for using the application! Goodbye."

if __name__ == '__main__':
    app.run(debug=True)



