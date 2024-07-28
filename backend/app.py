from flask import Flask,request
from flask_cors import CORS, cross_origin
from api import run
import json

app=Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def home():
    c= json.loads(request.data)
    out = run(c["lang"],c["code"])
    print(out)
    return {
        "output" : out,
    }


if __name__=="__main__":
    app.run()