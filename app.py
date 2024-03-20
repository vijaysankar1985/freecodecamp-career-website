# importing necessary modules
from flask import Flask, render_template

#app instance initialisation
app = Flask(__name__)

#Registerd a minimalistic route
@app.route('/')
def hello_world():
  return render_template('home.html')
  

#Running the app
if __name__=="__main__":
  app.run(host='0.0.0.0', debug= True)
  