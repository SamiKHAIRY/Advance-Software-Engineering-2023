import random
from flask import Flask, render_template, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)

@app.route('/dice')
def dice():
    k = request.args.get('k', type=int)
    n = request.args.get('n', type=int)
    
    if k and n:
        res = []
        for i in range(k):
            res.append(random.randint(1, n))
        return make_response(jsonify(s = res), 200)
    else:
        return make_response('Invalid input examOne\n', 400)

def create_app():
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)