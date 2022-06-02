from flask import Flask, request, jsonify
from PIL import Image
import torch

app = Flask(__name__)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt',device='cpu')
model.to("cpu")

@app.route('/api',methods=['POST'])

def predict():

    try:
        file = request.files['files']
        img1 = Image.open(file)

        results = model([img1])

        output = results.pandas().xyxy[0].to_json(orient='records')
        
        return (output)

    except:

        return("ERROR, something went wrong ..."),500

if __name__ == '__main__':
    app.run(port=5000, debug=True)