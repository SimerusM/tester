from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "csddc"

if __name__ == "__main__":
    app.run(debug=True)

