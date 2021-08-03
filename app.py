from flask import Flask
import flask_restful

app = Flask(__name__)
api= Api(app)

if __name__ == '__main__':
    app.run(debug=True)