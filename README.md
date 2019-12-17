# MobileNetV3 for Birthmark classification
The implementation from the paper into the Keras model mobileNetV3 is provided by xiaochus. No official model is published by Keras at time of writing.
According to the paper: [Searching for MobileNetV3](https://arxiv.org/abs/1905.02244?context=cs)

## Requirement
- Python > 3.6
- Tensorflow-gpu > 1.10.0  
- Keras > 2.2.4

For GPU support follow [Tensorflow GPU support](https://www.tensorflow.org/install/gpu)

## Data
The data can be downloaded at [ISIC Dataset](https://www.isic-archive.com/#!/topWithHeader/onlyHeaderTop/gallery) or use the [ISIC-Archive-Downloader](https://github.com/GalAvineri/ISIC-Archive-Downloader) created by [GalAvineri](https://github.com/GalAvineri).
We use the following data sets: MSK-1, MSK-2, MSK-3, MSK-4, MSK-5, UDA-1, UDA-2.

This gives us approximate 2282 malignant images and 10122 benign.

## Label the images

**Set the correct paths**
path_of_descriptions = "../BirthmarkGPU/Data/Descriptions" <br/>
path_of_images = "../BirthmarkGPU/Data/Images" <br/>
image_file_extension = ".jpeg" <br/>
image_destination_path = "../BirthmarkGPU/Data/Labeled" <br/>

**Run command below to label the data into Benign and Malignant:**

```
python label_images.py
```

## Image augmentation
This can be done using Keras.preprossing.image.ImageDataGenerator, but we strive after a 50-50 benign-malignant ratio. We therefore only want to create additional malignant data.
**Set the correct config**<br/>
rotation = 1 #Rotate vertically = 0, horizontally = 1. <br/>
images = 2282 #The number om images before each image augmentation process<br/>

After first run set rotation to the inverse setting. Run on both the "old" data and the newly created in ../Modified/Vertically(or Horizontally depending on settings).

Once done you should have approximate 9124 malignant images.

**The dataset folder structure is as follows:**

	| - Data/
		| - Labeled/
			| - Benign/
				| - benign0.jpeg
					....
			| - Malignant/
				| - malignant0.jpeg
					....

**Run command below to do create additional data:**

```
python image_augmentation.py path_to_malignant_images
```

## Train the model

 The ```config/config.json``` file provide a config for training.

### Train the classification
Split the data in 80:20 ratio for training and validation test.
**The dataset folder structure is as follows:**

	| - data/
		| - train/
	  		| - class 0/
				| - image.jpg
					....
			| - class 1/
			  ....
			| - class n/
		| - eval
	  		| - class 0/
			| - class 1/
			  ....
			| - class n/

**Run command below to train the model:**

```
python train_cls.py
```
