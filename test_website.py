from flask import Flask
import enter
import fin_comparison_working

app = Flask(__name__)

@app.route('/')
def index ():
    return enter

exercises = ['push_ups','plank','crunches','toe_touch']


@app.route('/<key>')
def index1 (key):
    to_dict={
        'push_ups':'icon1.gif',
        'plank':'icon2.gif',
        'crunches':'icon3.gif',
        'toe_touch':'icon4.gif'
    }
    return fin_comparison_working.main('msgifs/'+to_dict[key])


if __name__ == "__main__":
    app.run(host='0.0.0.0')
