import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello {}!".format(os.environ["USER"])

if __name__ == "__main__":
    if "USER" not in os.environ:
        raise EnvironmentError("USER environment variable is not defined.")

    app.run("0.0.0.0")
