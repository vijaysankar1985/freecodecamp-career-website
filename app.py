# importing necessary modules
from flask import Flask

#app instance initialisation
app = Flask(__name__)

#Registerd a minimalistic route
@app.route('/')
def hello_world():
  return "Hello World!"

#Running the app
if __name__=="__main__":
  app.run(host='0.0.0.0', debug= True)
  