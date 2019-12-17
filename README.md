# MobileNetV3 for Birthmark classification
The implementation from the paper into the Keras model mobileNetV3 is provided by xiaochus. No official model is published by Keras at time of writing.
According to the paper: [Searching for MobileNetV3](https://arxiv.org/abs/1905.02244?context=cs)

## Requirement
- Python > 3.6
- Tensorflow-gpu > 1.10.0  
- Keras > 2.2.4


## Create additional data

**Set the correct config**
rotation = 1 #Rotate vertically = 0, horizontally = 1.
images = 4563 #The number om images before each image augmentation process.

After first run set rotation to the inverse setting. Run on both the "old" data and the newly created in ../Modified/Vertically(or Horizontally depending on settings)

**Run command below to do create additional data:**

```
python image_augmentation.py path_to_images
```


## Label the images

**Set the correct paths**
path_of_descriptions = "../BirthmarkGPU/Data/Descriptions/"
path_of_images = "../BirthmarkGPU/Data/Images/"
image_file_extension = ".jpeg"
image_destination_path = "../BirthmarkGPU/Data/Labeled/"

**Run command below to label the data into Benign and Malignant:**

```
python label_images.py
```


## Train the model

 The ```config/config.json``` file provide a config for training.

### Train the classification

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
