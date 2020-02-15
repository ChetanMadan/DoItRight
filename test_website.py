from flask import Flask
import enter
import fin_comparison_working
import finalmost_comparison_working
import socket_finalmost_comparison_working
app = Flask(__name__)


@app.route('/')
def index ():
    return enter

exercises = ['push_ups','plank','crunches','toe_touch']


@app.route('/v')
def index1 ():
    return socket_finalmost_comparison_working.main('/dev/video0')

@app.route('/<exercise>')
def index2(exercise):
    ex = 'msgifs/'+exercise+'.gif'
    return socket_finalmost_comparison_working.main(ex)

if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0')
