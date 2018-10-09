
from fastai.conv_learner import *

def train():

    path = 'data/pill/small'
    labels_csv = f'{path}/classify_test_shape.csv'
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

    learn.fit(0.01, 1, cycle_len=1, cycle_mult=2, wds=wd)

if __name__ == "__main__":
    train()
