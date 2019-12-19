import os
import json
import pandas as pd

from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping

def prepare_image(file):
    img_path = ''
    img = image.load_img(img_path + file, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

def generate(batch, shape, ptest):
    """Data generation and augmentation

    # Arguments
        batch: Integer, batch size.
        size: Integer, image size.
        ptest: test dir.

    # Returns
        test_generator: test set generator
        count1: Integer, number of train set.
    """
    
    datagen1 = ImageDataGenerator(rescale=1. / 255)

    test_generator = datagen1.flow_from_directory(
        ptest,
        target_size=shape,
        batch_size=batch,
        class_mode='categorical')

    count1 = 0
    for root, dirs, files in os.walk(ptest):
        for each in files:
            count1 += 1

    return test_generator, count1


def predict():
    with open('config/config.json', 'r') as f:
        cfg = json.load(f)

    save_dir = cfg['save_dir']
    shape = (int(cfg['height']), int(cfg['width']), 3)
    n_class = int(cfg['class_number'])
    batch = 1 #Number of test items to process in each batch
    test_dir = "test/" #Dir with test data

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    if cfg['model'] == 'large':
        from model.mobilenet_v3_large import MobileNetV3_Large
        model = MobileNetV3_Large(shape, n_class).build()
    if cfg['model'] == 'small':
        from model.mobilenet_v3_small import MobileNetV3_Small
        model = MobileNetV3_Small(shape, n_class).build()

    pre_weights = cfg['weights']
    if pre_weights and os.path.exists(pre_weights):
        model.load_weights(pre_weights, by_name=True)

    test_generator, count1 = generate(batch, shape[:2], test_dir)

    score = model.evaluate(test_generator, verbose = 1)
    print(score)

    predict = model.predict(test_generator, steps = len(test_generator.filenames))
    print(predict)
    
if __name__ == '__main__':
    predict()
