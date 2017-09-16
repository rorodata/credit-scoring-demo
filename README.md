# credit-scoring-demo
## Introduction
Jupyter notebooks are the most commonly used tool to iteratively build data science models.  In this writeup, we discuss how a data scientist can deploy and manage data science models in production, without just a few simple lines of command from a CLI. In this writeup, we shall illustrate this using models in Python, a similar write-up for R is on the way.

The process is a simple two-step process, you will (1) create a project on rorocloud and (2) deploy your model files to rorocloud. These two steps will be executed using the roro client, which is a CLI tool.

### Step by Step Guide

####  0: Prerequisites
1.	You must have a rorodata platform account, as the models will be deployed on rorodata platform for this example. You may request access here
2.	Download roro client for python3 using pip install roro

#### 1: Setup your code folder or repository
1.	Clean up your notebook code and create the .py files for production. Follow simple hygiene rules for your code, e.g. split the code into train.py which trains the model, and predict.py which has the services you want to deploy like the predict function. 
2.	Create two additional files
    - roro.yml: This is a simple YML file that tells rorocloud what python environment should be provisioned for this project, which of your functions should be deployed as services, etc. For ease, you can copy a roro.yml from the example repository and change a few lines, it is self-explanatory
    - requirements.txt: In case you have a library that is not part of the base python environment, you will have to add these library names to the requirements.txt file (one library per line). If there are no additional libraries to include, you do not have to create a blank requirements.txt file


#### 2: Setup your project on rorocloud
1.	From command prompt, navigate to the code repository on your local machine. If you have your code on git or any other online repository, clone the repository to your local machine and navigate to this repository on command prompt. For this example, please go to https://github.com/rorodata and clone the credit-scoring-demo repository
2.	Login to rorodata platform
3.	Create a new project using the <b>roro create *credit-scoring-demo* </b> command from the command prompt. If you have already created a project, you do not have to repeat this step. The command roro projects will show you all your current projects. Remember, this project name i.e. credit-scoring-demo is the same name you must use in the roro.yml file, so give it a simple, short, catchy name like face-recognition. In fact, this project name also appears in the service endpoint/url, so don’t use special characters

#### 3: Deploy your project
1.	If you have everything in place, you can use the command roro deploy to deploy your project to production. This creates the services you want to deploy and prints out the url/endpoint, but in addition it does a lot of things behind the scenes. For our understanding, let’s list down what goes on in the background, in sequential order
                    i.   Creates a base docker image based on the environment you have chosen in the roro.yml file
                    ii.  Augments the docker image with additional libraries from the requirements.txt file, if any
                    iii. Provisions the hardware as indicated in the roro.yml file
                    iv.  Uses matching existing instance on rorocloud if available, else starts a new instance for this project
                    v.   Copies and loads the augmented docker image to this project space on rorocloud
                    vi.  Starts web services….
                    vii. Exposes your python functions as RESTful API services.

2.	Remember, you must have a trained model in production for your services to work. If you have a pretrained model, you must serialize it and copy it to the project. If you plan to train the model in the production environment e.g. using your train.py, then you must copy the data for this and run the train function. To do this, you can use the following command 
> roro run python train.py
from the command prompt from within the local repository

#### 4: Use the services you have deployed

If you have everything in place, you can use the command roro deploy to deploy your project to production. This creates the services you want to deploy and prints out the url/endpoint. You can now access you model at https://credit-scoring-demo.rorocloud.io
