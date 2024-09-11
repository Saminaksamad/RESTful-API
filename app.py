import os
from flask import Flask
from routes import register_routes

app = Flask (__name__)

register_routes(app)


if __name__ =='__main__':
    port = int (os.environ.get('port',5000))
    app.run (debug = False , host= '0.0.0.0' , port =port) 