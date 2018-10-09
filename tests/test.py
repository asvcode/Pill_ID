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

learn.load('NIH_one')

test_preds, _ = learn.TTA(is_test=True)
preds = np.mean(test_preds, axis=0)
classes = np.array(data.classes)

res = np.array([" ".join(classes[(np.where(pp>0.60))]) for pp in preds])
filenames = np.array([os.path.basename(fn).split('.')[0] for fn in data.test_ds.fnames],)
frame=pd.DataFrame(res, index=filenames, columns=['tags'])

frame.to_csv('test_results.csv', index_label='image')
