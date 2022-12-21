from flask import Flask, render_template

app = Flask(__name__)

applicantData = [
    {'pic':'panda', 'name':'Panda Bear', 'school':'CC', 'grad':'2025', 'status':'Accepted', 'interviewed':True},
    {'pic':'ice', 'name':'Ice Bear', 'school':'SEAS', 'grad':'2024', 'status':'In Review', 'interviewed':True},
    {'pic':'grizz', 'name':'Grizz Bear', 'school':'SEAS', 'grad':'2026', 'status':'Accepted', 'interviewed':True},
    {'pic':'pooh', 'name':'Winnie T. Pooh', 'school':'GS', 'grad':'2023', 'status':'Rejected', 'interviewed':True},
    {'pic':'kfp', 'name':'Kung Fu Panda', 'school':'CC', 'grad':'2024', 'status':'Accepted', 'interviewed':True},
    {'pic':'paddy', 'name':'Paddington Bear', 'school':'BC', 'grad':'2025', 'status':'In Review', 'interviewed':True},
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
    app.run(port=8000, debug = True)