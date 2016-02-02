from flask import Flask
app = Flask(__name__)
app.run(host='74.207.235.39')
@app.route("/")
def hello():
    return "Hello, I love Digital Ocean!"
if __name__ == "__main__":
    app.run()
