from flask import Flask
app = Flask(__name__)


# after install flask run first $env:FLASK_APP = "hello.py" and then "flask run"



# @app.route('/')
# @make_bold
# def hello_world():
#     return "<h1 style= 'text-align: center'> Hello Natnael </h1>"

# def outer():
#     print("i am outer")
#     def inter():
#         print("i am inter")
#     inter()
#
# outer()


@app.route("/username/<name>")
def greeting(name):
    return f"Hello {name}"
# def logging_decorator(func):
#     def wrapper(*args):
#         print(f"You called {func.__name__}{args}")
#         print(f"this {func.__name__}")
#         result = func(*args)
#         print(f"It returned: {result}")
#         return result
#
#     return wrapper


# @logging_decorator
# def a_function(*args):
#     return sum(args)
#
#
# a_function(1, 2, 3)
#
if __name__ == "__main__": ## it use to run the app automatically instead of using termianl
    app.run(debug=True)
