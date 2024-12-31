# Task
To go through a set of coloured balls (either red, yellow, green or blue) and sort them into separate containers based on their colour.

Original source code used was from [here](https://github.com/samyakmohelay/Dog-Breed-Image-Prediction), but instead modified to work with our images and required parameters. Still uses the same pre-trained MobileNet KerasLayer model, which is definitely overkill for this task. A simpler, custom model could easily be created instead. 

# Installation
Tested only on Windows 11 (with CPU side inference used for TensorFlow)
Used pip to download required packages automatically, did no manual versioning stuff

Python version: 3.12.4
Pip version: 24.0
TF Version: 2.18.0
TF hub Version: 0.16.1

Download ``images.zip`` from [here](https://drive.google.com/file/d/1zOzkzrH54HQYHtl2KO6aTReyYVQoxOM8/view?usp=drive_link) and unzip it inside the project folder. It should unzip to a single ``images`` folder where all images are contained within it.

## Missing
* Retrieve dedicated server code and upload it