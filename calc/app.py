# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/math/<op>')
def do_math(op):
    a = request.args.get('a')
    b = request.args.get('b')
    print(a, b)
    result = eval('operations.'+op + f"({a}, {b})")
    return str(result)

