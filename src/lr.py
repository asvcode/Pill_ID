from fastai.conv_learner import *

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

def lr_find(self, start_lr=1e-5, end_lr=10, wds=None):
    self.save('tmp')
    layer_opt = self.get_layer_opt(start_lr, wds)
    self.sched = LR_Finder(layer_opt, len(self.data.trn_dl), end_lr)
    self.fit_gen(self.model, self.data, layer_opt, 1)
    self.load('tmp')

    learn.lr_find()
    learn.sched.plot_lr()
