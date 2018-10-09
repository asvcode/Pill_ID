from fastai.conv_learner import *
from fastai.plots import *

path = 'data/pill/small'
labels_csv = f'{path}/classify_shape_color_single.csv'
n = len(list(open(labels_csv)))-1
val_idxs = get_cv_idxs(n)

aug_tfms = [RandomDihedral(), RandomLighting(0.2, 1.8)]

arch = resnet152
sz = 32
bs = 64
tfms = tfms_from_model(arch, sz, aug_tfms)
data = ImageClassifierData.from_csv(path, 'train', labels_csv, tfms=tfms,
                            val_idxs=val_idxs, test_name='test_one', bs=bs)

x,y=(next(iter((data.val_dl))))

learn = ConvLearner.pretrained(arch, data, ps=0.25)

wd=5e-4

learn.load('NIH_one')

def infer():
    learn.precompute = False
    trn_tfms, val_tfms = tfms_from_model(arch, sz)
    fn = (f'{path}/test_one/C5_600.jpg')
    test_img = open_image(fn)
    plt.imshow(test_img)

    lm = val_tfms(test_img)
    lm.shape

    pred = learn.predict_array(lm[None])
    probs = np.exp(pred)
    result = np.argmax(probs)
    result

    md.classes[result]
