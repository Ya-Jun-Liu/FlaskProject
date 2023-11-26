from flask import Flask

app = Flask(__name__)


# @app.route('/')  # specifies the URL that will result in that function being called.
# def hello_world():  # put application's code here
#     return '<h1>Hello/Hola/Bonjour World! :)</h1>'  # returns a string!!! in Flask


# @app.route('/greet')
# def greet():
#     return "Hello"


# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name=""):
#     return "Hello{Jun}"


@app.route('/f/<float:celsius>')
def convert_celsius_to_fahrenheit(celsius=""):
    """Convert from Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    string = f"{fahrenheit:.2f}"
    return string


if __name__ == '__main__':
    app.run()
