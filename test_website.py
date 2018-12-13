from flask import Flask
import enter
import finalmost_nolag

app = Flask(__name__)

@app.route('/')
def index ():
    return enter.main()

@app.route('/v')
def index1 ():
    return finalmost_nolag.main()


if __name__ == "__main__":
    app.run()
