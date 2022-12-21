from flask import Flask, render_template

app = Flask(__name__)

applicantData = [
    {'idx': 1, 'pic':'panda', 'name':'Panda Bear', 'school':'CC', 'grad':'2025', 'status':'Accepted', 'interviewed':True},
    {'idx': 2, 'pic':'ice', 'name':'Ice Bear', 'school':'SEAS', 'grad':'2024', 'status':'In Review', 'interviewed':True},
    {'idx': 3, 'pic':'grizz', 'name':'Grizz Bear', 'school':'SEAS', 'grad':'2026', 'status':'Accepted', 'interviewed':True},
    {'idx': 4, 'pic':'pooh', 'name':'Winnie T. Pooh', 'school':'GS', 'grad':'2023', 'status':'Rejected', 'interviewed':True},
    {'idx': 5, 'pic':'kfp', 'name':'Kung Fu Panda', 'school':'CC', 'grad':'2024', 'status':'Accepted', 'interviewed':True},
    {'idx': 6, 'pic':'paddy', 'name':'Paddington Bear', 'school':'BC', 'grad':'2025', 'status':'In Review', 'interviewed':True},
    {'idx': 7, 'pic':'dk', 'name':'Donkey Kong', 'school':'GS', 'grad':'2024', 'status':'In Review', 'interviewed':True},
    {'idx': 8, 'pic':'care', 'name':'Care Bear', 'school':'BC', 'grad':'2026', 'status':'In Review', 'interviewed':True},
    {'idx': 9, 'pic':'kirby', 'name':'Kirby', 'school':'CC', 'grad':'2024', 'status':'In Review', 'interviewed':True},
    {'idx': 10, 'pic':'simba', 'name':'Simba the Lion', 'school':'SEAS', 'grad':'2026', 'status':'In Review', 'interviewed':True},
]


@app.route('/applicants')
@app.route('/applicants/<path:path>')
def applicant(path=''):
    appid = path
    for app in applicantData:
        if app['name'] == appid: return render_template('applicant.html', data = app)
    return render_template('dashboard.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html', data = applicantData)

@app.route('/')
def hello_world():
    return render_template('dashboard.html', data = applicantData)

if __name__ == '__main__':
    app.run(debug = True)