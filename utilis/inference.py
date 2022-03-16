from skimage.io import imread
import time
import cv2
from skimage import feature
import mahotas as mt
import numpy as np
import progressbar
from numpy.lib import stride_tricks
import pickle
import math
SVM_PATH = 'utilis/models/SVM_model_kaggle .pkl'
DT_PATH = 'utilis/models/model_DT.pkl'
RF_PATH = 'utilis/models/RF_model_1000.pkl'


def extract_features(img, img_gary, label, train, lbp_radius=10, lbp_points_ratio=4, h_neighbors=11, num_examples=10000):
    '''
    extract above 13 features
    '''

    # 1.  RGB values have beed extracted when loading the orignal dataset --img--
    # 2.  Local Binary Pattern https://www.researchgate.net/figure/Local-binary-patterns-LBP-texture-a-Principle-of-LBP-b-LBP-texture-of-the-canopy_fig4_323741245
    def LBP(img, points, radius):
        '''
         points: Number of circularly symmetric neighbour set points 
         radius: Radius of circle
        '''
        #print(' extracting local binary pattern features.')
        lbp = feature.local_binary_pattern(img, points, radius)
        return (lbp-np.min(lbp))/(np.max(lbp)-np.min(lbp)) * 255

    # 3. Haralick's texture features https://gogul.dev/software/texture-recognition
    # https://www.dovepress.com/application-of-haralick-texture-features-in-brain-18f-florbetapir-posi-peer-reviewed-fulltext-article-CIA
    def HTF(img, h_neighbors, ss_dix):
        '''
        h_neighbors:
        '''
        #print(' extracting haralick texture features.')
        size = h_neighbors
        shape = (img.shape[0] - size + 1, img.shape[1] - size + 1, size, size)
        # should be equal to the size of feature_img = feature_img[h_index:-h_index, h_index:-h_index]
        strides = 2 * img.strides
        patches = stride_tricks.as_strided(img, shape=shape, strides=strides)
        patches = patches.reshape(-1, size, size)

        if len(ss_idx) == 0:
            bar = progressbar.ProgressBar(maxval=len(patches),
                                          widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        else:
            bar = progressbar.ProgressBar(maxval=len(ss_idx),
                                          widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

        def calculate_haralick(img):
            '''
            calculate haralick features for each patch
            '''
            features = []

            feature_ = mt.features.haralick(img)
            mean_ = feature_.mean(axis=0)

            [features.append(i) for i in mean_[0:9]]

            return np.array(features)

        bar.start()
        h_features = []

        if len(ss_idx) == 0:
            for i, p in enumerate(patches):
                bar.update(i+1)
                h_features.append(calculate_haralick(p))
        else:
            for i, p in enumerate(patches[ss_idx]):
                bar.update(i+1)
                h_features.append(calculate_haralick(p))

        return np.array(h_features)

    # 4. extracting all the features

    # Hyperparameters:
    # number of circularly symmetric neighbour set points
    lbp_points = lbp_radius*lbp_points_ratio

    # num_examples = 1000 # number of examples (pixels) per image to use for training model
    h_index = int((h_neighbors - 1)/2)
    feature_img = np.zeros((img.shape[0], img.shape[1], 4))
    feature_img[:, :, :3] = img
    feature_img[:, :, 3] = LBP(img_gary, lbp_points, lbp_radius)
    feature_img = feature_img[h_index:-h_index, h_index:-h_index]
    s = feature_img.shape
    features = feature_img.reshape((s[0]*s[1], s[2]))

    if train:
        ss_idx = np.random.randint(0, features.shape[0], num_examples)
        features = features[ss_idx]
    else:
        ss_idx = []

    h_features = HTF(img_gary, h_neighbors, ss_idx)
    features = np.hstack((features, h_features))

    if train:
        label = label[h_index:-h_index, h_index:-h_index]
        labels = label.reshape(label.shape[0]*label.shape[1], 1)
        labels = labels[ss_idx]
    else:
        labels = None

    return features, labels


def fake_img_resp():
    img = imread('utilis/tmp/thematic_layer.jpg')
    return img


def inference(classifier, h_neighbors=11,upload_tmp=True):
    if upload_tmp:
        img=imread('utilis/tmp/tmp_upload.png')
    else:
        img = imread('utilis/tmp/tmp.png')

    start_time = time.time()
    print("_"*30)
    print('[INFO] Doing inference on test images...')
    print('loading trained model.')

    border = int((h_neighbors-1)/2)
    Feature = []
    print('infer for image')
    if classifier == 'SVM':
        model = pickle.load(open(SVM_PATH, 'rb'))
    if classifier == 'DT':
        model = pickle.load(open(DT_PATH, 'rb'))
    if classifier == 'RF':
        model = pickle.load(open(RF_PATH, 'rb'))

    img = cv2.copyMakeBorder(img, top=border, bottom=border,
                             left=border, right=border,
                             borderType=cv2.BORDER_CONSTANT,
                             value=[0, 0, 0])
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features, _ = extract_features(img, img_gray, label=None, train=False)
    Feature.append(features)
    prediction = model.predict(features.reshape((-1, features.shape[1])))
    size_pred = int(math.sqrt(features.shape[0]))
    pred_img = prediction.reshape(size_pred, size_pred)
    end_time = time.time()
    print('predection time: %.4f s' % (end_time-start_time))
    cv2.imwrite('utilis/tmp/thematic_layer.jpg', pred_img*255)
    return pred_img
