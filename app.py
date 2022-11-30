from flask import Flask, render_template

app = Flask(__name__)

applicantData = [
    {'name':'Panda Bear', 'school':'CC', 'grad':'2025', 'status':'Accepted'},
    {'name':'Ice Bear', 'school':'SEAS', 'grad':'2024', 'status':'In Review'},
    {'name':'Grizz Bear', 'school':'SEAS', 'grad':'2026', 'status':'Accepted'},
    {'name':'Winnie T. Pooh', 'school':'GS', 'grad':'2023', 'status':'Rejected'},
    {'name':'Kung Fu Panda', 'school':'CC', 'grad':'2024', 'status':'Accepted'},
    {'name':'Paddington Bear', 'school':'BC', 'grad':'2025', 'status':'In Review'},
]

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html', data = applicantData)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug = True)