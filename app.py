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

@app.route('/QueDeque.html', methods=["GET", "POST"])
def process_queuedeque():
    queue_input = request.form['queue_input']
    deque_input = request.form['deque_input']

    # Process Queue
    queue = Queue()
    for item in queue_input.split():
        queue.enqueue(item)

    # Process Deque
    deque = Deque()
    for item in deque_input.split():
        deque.add_front(item)

    return render_template('/QueDeque.html', queue_result=queue, deque_result=deque)


@app.route('/HashFunc.html')
def hashFunc():
    return render_template('/HashFunc.html')

@app.route('/Postfix.html', methods=["GET", "POST"])
def Postfix():
    # Request Infix Expression
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
    #print(test_data)
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

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

if __name__ == '__main__':
    app.run(debug=True)