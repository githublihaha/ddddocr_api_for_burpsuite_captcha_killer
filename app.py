from flask import Flask, request
import json
import ddddocr
import base64

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ["POST"])
def getCode():
    data = request.get_data()
    print("1111111111111111111111111111111111")
    print(data)
    print("1111111111111111111111111111111111")
    data_json = json.loads(data)


    ocr = ddddocr.DdddOcr()
    img_b64 = data_json.get('img')
    x = base64.b64decode(img_b64)
    res = ocr.classification(x)
    return res
