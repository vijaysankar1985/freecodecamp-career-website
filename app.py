# importing necessary modules
from flask import Flask, jsonify, render_template

#app instance initialisation
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
  }
]

#Registerd a minimalistic route
@app.route('/')
def hello_vijay():
  return render_template('home.html', jobs=JOBS, company_name='Vijay R.S.')

#Registerd a route to return json
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  
#Running the app
if __name__=="__main__":
  app.run(host='0.0.0.0', debug= True)
  