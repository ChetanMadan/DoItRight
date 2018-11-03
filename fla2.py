from flask import Flask
import finalmost
app = Flask(__name__)

@app.route('/')
def index ():

    return "<html> <body> <a href='/vm'>Try Me Now</a> </body> </html>"
@app.route('/vm')
def index1 ():

    return finalmost.main()



if __name__ == "__main__":
    app.run()