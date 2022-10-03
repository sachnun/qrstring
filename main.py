# flask server
from flask import Flask, request
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import urllib.request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# QR code image to string


def decode(im) :
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    # Print results
    for obj in decodedObjects:
        return obj.data
    
    
@app.route('/qr')
def qr():
    # parameter url
    url = request.args.get('url')
    # import image form url
    # download image to var
    resp = urllib.request.urlopen(url)
    # convert to numpy array
    image = cv2.imdecode(np.asarray(bytearray(resp.read()), dtype="uint8"), cv2.IMREAD_COLOR)
    # decode image
    data = decode(image)
    return data

if __name__ == '__main__':
    app.run()