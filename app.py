import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from postfix import infix_to_postfix
from queue_deque import Queue, Deque
from HashFunction import HashTable, process_commands
from graph import Graph, build_mrt_lrt_graph, find_shortest_path, mrt_lrt_graph
from bubble_sort_algo import bubble_sort
from selection_sort_algo import selection_sort
from insertion_sort_algo import insertion_sort
from merge_sort_algo import merge_sort
from quick_sort_algo import quick_sort
import time


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AppList.html')
def appList():
    return render_template('/AppList.html')


@app.route('/MemberPage.html')
def Memberpage():
    return render_template('/MemberPage.html')

@app.route('/SearchAlgo.html')
def searchAlgo():
    return render_template('/SearchAlgo.html')

@app.route('/InPost.html')
def inPost():
    # Request Infix Expression
    if request.method == "POST":
        infix_str = request.form.get("infix")

        try:
            float(infix_str)
            return render_template("InPost.html", error="Invalid input. Ensure the operators are only `*`, `(`, `)`, `+`, `-`, or `/`, and free from numbers or whitespaces.")
        except:
            result = infix_to_postfix(infix_str)
            return render_template('InPost.html', result=result, infix_str=infix_str)
    else:
        return render_template('InPost.html', result=None)

queue = []
@app.route('/QueueDeque.html', methods=["GET", "POST"])
def queue_operations():
    Enqueue = None
    Dequeue = None
    if request.method == 'POST':
        if request.form.get('enqueue', ''):
            data = str(request.form.get('inputString', ''))
            queue.append(data)

        elif request.form.get('dequeue', ''):
            if queue:
                Dequeue = queue.pop(0)
    return render_template('QueueDeque.html', Enqueue=queue, Dequeue=Dequeue)

@app.route('/HashFunc.html', methods=['GET', 'POST'])
def enchanting_table():
    if request.method == "POST":
        cmd = request.form.get('HashOptions')  # Correct variable name
        numcommand = request.form.get('IntegerSelect')
        listall = request.form.get('DataInput')
        new_list = listall.split('\r\n')
        my_array = []
        for item in new_list:
            my_array.append(item)
        
        try:
            # check if it is an integer
            int(numcommand)
        except(ValueError):
            error = 'input is not integer. Please use integers only.'
            return render_template('HashFunction.html', cmd=None, numcommand=None, result=None, listall=None, error=error)
        
        numtype = int(numcommand)
        if numtype >= 1:
            result = process_commands(my_array, cmd) 
            return render_template('HashFunction.html', cmd=None, numcommand=None, result=result, listall=None, error=None)
        if numtype <= 0:
            error = 'input is less than 1. Please use an integer greater than or equal to 1.'
            return render_template('HashFunction.html', cmd=None, numcommand=None, result=None, listall=None, error=error)
    else:
        return render_template('HashFunction.html', cmd=None, numcommand=None, result=None, listall=None, error=None)

@app.route('/Postfix.html', methods=["GET", "POST"])
def Postfix():
    if request.method == "POST":
        infix_str = request.form.get("infix")

        try:
            float(infix_str)
            return render_template("Postfix.html", error="Invalid input. Ensure the operators are only `*`, `(`, `)`, `+`, `-`, or `/`, and free from numbers or whitespaces.")
        except:
            result = infix_to_postfix(infix_str)
            return render_template("Postfix.html", result=result, infix_str=infix_str)
    else:
        return render_template('Postfix.html', result=None)

@app.route("/searchalgo-interface.html", methods=["GET", "POST"])
def dir():
    
    numbers = range(1, 1001)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1 

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                #arr = list(map(int, array_str.split(",")))
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("searchalgo-interface.html", result=result, search_type=search_type, execution_time=execution_time,test_data=test_data)
        except ValueError:
            return render_template("searchalgo-interface.html", error="Invalid input. Ensure the array and target are integers.")
    

    return render_template("searchalgo-interface.html",test_data=test_data)

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)
    #result_recursive = exponential_search_recursive(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
       # "recursive_search_result": result_recursive
    })

stations = [
    'North Avenue', 'Quezon Avenue', 'Kamuning', 'MRT Cubao', 'MRT Santolan', 
    'Ortigas', 'Shaw Boulevard', 'Boni', 'Guadalupe', 'Buendia', 'Ayala', 
    'Magallanes', 'Taft Avenue', 'Baclaran', 'EDSA', 'Libertad', 'Gil Puyat', 
    'Vito Cruz', 'Quirino', 'Pedro Gil', 'United Nations', 'Central Terminal', 
    'Carriedo', 'Doroteo Jose', 'Bambang', 'Tayuman', 'Blumetritt', 'Abad Santos', 
    'R. Papa', '5th Avenue', 'Monumento', 'Balintawak', 'Roosevelt',  'Recto', 'Legarda', 
    'Pureza', 'V. Mapa', 'J. Ruiz', 'Gilmore', 'Betty Go-Belmonte', 
    'Araneta Center-Cubao', 'Anonas', 'Katipunan', 'LRT Santolan', 'Marikina', 
    'Antipolo'
]

@app.route('/graphs.html', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        start_station = request.form['startStation']
        end_station = request.form['endStation']
        shortest_path = find_shortest_path(mrt_lrt_graph, start_station, end_station)

        if shortest_path:
            return render_template('graphs.html', stations=stations, shortest_path=shortest_path, start_station=start_station, end_station=end_station)
        else:
            return render_template('graphs.html', stations=stations, no_path=True, start_station=start_station, end_station=end_station)
    else:
        return render_template('graphs.html', stations=stations)
    

@app.route('/SortingAlgo.html', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        input_array = request.form.get('inputArray')

        # Check if input_array is None or empty
        if input_array is None or input_array.strip() == "":
            return render_template('SortingAlgo.html', error_message="Please enter valid input.")

        input_array = list(map(int, input_array.split(',')))

        selected_algorithm = request.form.get('algorithm')
        start_time = time.time()

        if selected_algorithm == 'bubble':
            sorted_array = bubble_sort(input_array)
        elif selected_algorithm == 'selection':
            sorted_array = selection_sort(input_array)
        elif selected_algorithm == 'insertion':
            sorted_array = insertion_sort(input_array)
        elif selected_algorithm == 'merge':
            sorted_array = merge_sort(input_array)
        elif selected_algorithm == 'quick':
            sorted_array = quick_sort(input_array)
        else:
            sorted_array = input_array  # Default to the input array if no algorithm is selected
        
        end_time = time.time()  # Record the end time

        execution_time = end_time - start_time  # Calculate the execution time

        return render_template('SortingAlgo.html', result=sorted_array, execution_time=execution_time)


    # If it's a GET request, render the initial page without any sorting results
    return render_template('SortingAlgo.html')


if __name__ == '__main__':
    app.run(debug=True)