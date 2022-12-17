from flask import render_template
from flask import request, jsonify
from flask_cors import cross_origin
from controllers import validation
from modules import modules

def configRoute(app):
    @app.route("/")
    def index():
        hello = modules.hello()
        content = modules.content()
        return render_template("index.html", hello=hello, content=content)
    
    @app.route("/parsing", methods=['POST'])
    @cross_origin()
    def parsing():
        requestString = request.get_json()
        string = requestString['string']
        result = validation.is_accepted(string)
        return jsonify({
            'status' : 1,
            'message' : 'succes get validation',
            'result': result
        })
