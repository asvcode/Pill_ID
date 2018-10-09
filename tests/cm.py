from fastai.conv_learner import *
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

path = 'data/pill/small'
labels_csv = f'{path}/classify_shape_color_single.csv'
n = len(list(open(labels_csv)))-1
val_idxs = get_cv_idxs(n)

aug_tfms = [RandomDihedral(), RandomLighting(0.2, 1.8)]

arch = resnet50
sz = 32
bs = 64
tfms = tfms_from_model(arch, sz, aug_tfms)
data = ImageClassifierData.from_csv(path, 'train', labels_csv, tfms=tfms,
                            val_idxs=val_idxs, test_name='test_one', bs=bs)

x,y=(next(iter((data.val_dl))))

learn = ConvLearner.pretrained(arch, data, ps=0.25)

wd=5e-4

learn.load('NIH_one')

log_preds,y = learn.predict_with_targs()
preds = np.exp(log_preds)
pred_labels = np.argmax(preds, axis=1)

def confusion_matrix():
    cm = confusion_matrix(y, pred_labels)
    plot_confusion_matrix(cm, data.classes)
