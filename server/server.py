from flask import Flask,request,Response,json
from json import load

def loadJson(path):
    with open(path,'r') as file:
        return load(file)

data = loadJson('product_db.json')[::-1]

app = Flask(__name__)

@app.route("/product",methods=['GET'])
def getProduct():
    count = request.args.get('count')
    response = {'result' : data[0:int(count)]}
    return Response(status=200,mimetype='application/json',response=json.dumps(response))

if(__name__ == "__main__"):
    app.run()
