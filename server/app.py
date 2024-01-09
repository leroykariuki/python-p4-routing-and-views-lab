#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = range(1, parameter +1)
    return '\n'.join(map(str,numbers))

@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Error: Invalid operation."

    return f"Result: {result}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)