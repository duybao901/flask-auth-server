import os
import configparser
from App.factory import create_app

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("config.ini")))

if __name__ == "__main__":
  app = create_app()
  app.config['MONGO_URI'] = "mongodb+srv://baoduy123:baoduy123@cluster0.ubjer5c.mongodb.net/face-data?retryWrites=true&w=majority"
 
  app.run(debug=True)      

  
  