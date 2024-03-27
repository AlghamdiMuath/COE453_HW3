import functions_framework
from flask import jsonify

@functions_framework.http
def add(request):
    # Extracting values from query parameters instead of JSON body
    x = request.args.get('X')
    y = request.args.get('Y')

    if x is not None and y is not None:
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return jsonify({'error': 'Invalid input. Ensure X and Y are numbers.'}), 400

        result = x + y
        return jsonify({'X': x, 'Y': y, 'Result': result})
    else:
        return jsonify({'error': 'Invalid input. X and Y must be provided as query parameters.'}), 400
