# Pill Identifier - Pill_ID
<div align="center">
Project for identifying prescription pills.  Current methods utitilize a drop down method where the user has to manually input the pill characteristics such as shape, color and imprint.
  
</div align>
<div align="center">
  <img src="static/slide_one.jpg" width="200" height="411">
</div align>


Screenshot from the National Library of Medicine Pillbox pill identifier portal (https://pillbox.nlm.nih.gov/) that shows the current drop down menu for identifying pills.  There is no option for using pictures to help pre-populate the fields.

## Motivation

Patients particularly those over 50 are more likely to be prescribed more pills,have dexterity issues and may also have issues with eyesight.  This project is looking at a way to improve efficiency and accuracy by using images to help pre-populate input fields.

## Project format:

- **src** : Source code
- **tests** : Test model on specific image
- **data** : Example data
- **Android** : Code for Android deployment
- **Flask** : Code for Flask deployment
- **static** : README content and images

## Installation
Requirements for this project can be installed by creating the required environment using the `pillid.yml` file

```
conda env create -f pillid.yml 
```

## Requisites
- Fastai
- Flask
- Android Studio

## Build Environment
- Include instructions of how to launch scripts in the build subfolder
- Build scripts can include shell scripts or python setup.py files
- The purpose of these scripts is to build a standalone environment, for running the code in this repository
- The environment can be for local use, or for use in a cloud environment
- If using for a cloud environment, commands could include CLI tools from a cloud provider (i.e. gsutil from Google Cloud Platform)
```
# Example

# Step 1
# Step 2
```

## Configs
- pillid.yml contains all configuration requirements


## Test
- Include instructions for how to run all tests after the software is installed
```
# Example

# Step 1
# Step 2
```

## Run Inference
- Include instructions on how to run inference
- i.e. image classification on a single image for a CNN deep learning project
```
# Example

# Step 1
# Step 2
```

## Build Model
- Include instructions of how to build the model
- This can be done either locally or on the cloud
```
# Example

# Step 1
# Step 2
```

## Serve Model
- Include instructions of how to set up a REST or RPC endpoint 
- This is for running remote inference via a custom model
```
# Example

# Step 1
# Step 2
```

## Analysis
- Include some form of EDA (exploratory data analysis)
- And/or include benchmarking of the model and results
```
# Example

# Step 1
# Step 2
```
