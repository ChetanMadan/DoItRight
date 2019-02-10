from flask import Flask, render_template
app = Flask(__name__)
exc =[{
    'Name' : 'Toe touching',
    'Link' : 'https://www.youtube.com/'
},
{
    'Name' : 'push ups',
    'Link' : 'https://www.youtube.com/watch?v=IODxDxX7oi4'
},
]

@app.route("/")
def home():
    return render_template('h.html',exc=exc)

@app.route("/exc")
def excercise():
    return render_template('excercise.html',exc=exc)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')




