from flask import Flask
import enter
import fin_comparison_working
import finalmost_comparison_working
app = Flask(__name__)

@app.route('/')
def index ():
    return enter

exercises = ['push_ups','plank','crunches','toe_touch']


@app.route('/v')
def index1 ():
    return finalmost_comparison_working.main('exer.mp4')

@app.route('/<exercise>')
def index2(exercise):
    ex = 'msgifs/'+exercise+'.gif'
    return finalmost_comparison_working.main(ex)

if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0')
