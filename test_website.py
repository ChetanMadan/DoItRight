from flask import Flask
import enter
import fin_comparison_working
 
app = Flask(__name__)

@app.route('/')
def index ():
    return enter

exercises = ['push_ups','plank','crunches','toe_touch']


@app.route('/v')
def index1 ():
    
    return fin_comparison_working.main('exer.mp4')


if __name__ == ("__main__"):
    app.run(debug=True,host='0.0.0.0')
