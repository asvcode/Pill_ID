import flask
from flask import Flask, render_template, request
from fastai.conv_learner import *
from fastai.dataset import *

app = flask.Flask(__name__)

import torch
print(torch.cuda.is_available())

def load_model():
    global arch, learn, sz
    PATH = 'data/'
    arch = resnet50
    sz = 32
    bs = 64
    wd=5e-4

    labels_csv = f'{PATH}/classify_shape_color.csv'
    n = len(list(open(labels_csv))) -1
    val_idxs = get_cv_idxs(n)

    aug_tfms = [RandomDihedral(), RandomLighting(0.2, 1.8)]
    tfms = tfms_from_model(arch, sz, aug_tfms, crop_type=CropType.RANDOM)
    data = ImageClassifierData.from_csv(PATH, 'train', labels_csv, tfms=tfms,
                         val_idxs=val_idxs, test_name='new_nih', bs=bs)
    learn = ConvLearner.pretrained(arch, data, ps=0.25)
    learn.load('flask_test')

    #torch.load('my_file.pt', map_location=lambda storage, location: 'cpu')

def prepare_image(nparr):
    PATH ='data/'
    trn_tfms,val_tfms = tfms_from_model(arch, sz)
    #flags = cv2.IMREAD_UNCHANGED+cv2.IMREAD_ANYDEPTH+cv2.IMREAD_ANYCOLOR
    #image = cv2.cvtColor(cv2.imdecode(nparr, flags).astype(np.float32)/255, cv2.COLOR_BGR2RGB)
    image = cv2.imread(f'{PATH}/test2.jpg')
    #inputs = cv2.cvtColor(inputs, cv2.COLOR_BGR2RGB).astype(np.float32)
    #image = (cv2.COLOR_BGR2RGB.astype(np.float32))
    image = val_tfms(image)
    return image


#@app.route('/')
#def runit():
#    return render_template('layout.html')

@app.route('/index')
@app.route('/')
def index():
    return render_template('select_files.html')

#@app.route('/layout.html')
#def signup():
#    return render_template('layout.html')

#@app.route('/index')
#@app.route('/')
#def index():
    #return render_template('settings.html')

@app.route("/predict", methods=["POST"])
def predict():
    data = {"success": False}

    if flask.request.method == "POST":
        nparr = np.fromstring(flask.request.data, np.uint8)
        image = prepare_image(nparr)
        preds = learn.predict_array(image[None])

        if(np.argmax(preds) < 0.5):
            data["result"] = "capsule"
        else:
            data["result"] = "tablet"

        print(np.argmax(preds))
        data["probability"] = int(np.argmax(preds))
        data["success"] = True

    return flask.jsonify(data)

if __name__ == "__main__":
    print(("loading fastai...."))
    load_model()
    app.run()
