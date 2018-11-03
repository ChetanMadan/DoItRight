from flask import Flask
import enter
import finalmost

app = Flask(__name__)

@app.route('/')
def index ():
    return enter

@app.route('/v')
def index1 ():
    return finalmost.main()


if __name__ == "__main__":
    app.run()
