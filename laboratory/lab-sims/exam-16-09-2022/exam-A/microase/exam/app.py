from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

@app.route('/mulstring')
def mulstring():
    a = request.args.get('a')
    n = request.args.get('n', type=int)

    if (a and n) and (n > 0):
        res = a * n
        return make_response(jsonify(s=res), 200)
    else:
        return make_response('Invalid input\n', 400)
    
def create_app():
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)