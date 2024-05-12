from flask import Flask, jsonify
from calculator import Calculator 

app = Flask(__name__)
calc = Calculator()

@app.route('/calc/<operation>/<int:num1>/<int:num2>')
def calculate(operation, num1, num2):
    if operation == 'add':
        result = calc.add(num1, num2)
    elif operation == 'subtract':
        result = calc.subtract(num1, num2)
    elif operation == 'multiply':
        result = calc.multiply(num1, num2)
    elif operation == 'divide':
        try:
            result = calc.divide(num1, num2)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
