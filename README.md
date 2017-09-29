# Credit Scoring

### About This Demo Application
In this Credit Scoring Demo, we demonstrate the workings of a machine learning model that assigns a “credit score” to each applicant applying for credit, based on some data (attributes) from the applicant. The credit score is actually a probability score, and is used to make an accept/reject decision on the request for credit or loan. 

Please look at the notebook in the rorodata github repository [here](https://github.com/rorodata/credit-scoring-demo/blob/master/notebooks/Credit_Scoring_NB.ipynb) for more details about the modelling and data that went into this effort.

### Productionizing Machine Learning Models Using rorodata 
Below, we discuss how a data scientist can deploy and manage data science models in production using rorodata platform, with just a few simple lines of command from a CLI. In this writeup, we shall illustrate this using Python, a similar write-up for R is on the way. 

To understand the big picture view about the rorodata platform, [go here](https://github.com/rorodata/)


#### Prerequisites
- Download roro client for python3 using pip install roro-client. Note that currently, we only support python 3.5 and above.
- You must have a rorodata platform account, as the models will be deployed on rorodata platform for this example. You may request access here. 

#### Steps (code only)
```
> git clone https://github.com/rorodata/credit-scoring-demo.git
> cd credit-scoring-demo

# NOTE: edit roro.yml to change project name to name of new project, I am using the project name credit-score for this example
> roro create credit-score
Created project: credit-score

> roro deploy
Your project has been deployed.

# run training to create trained model
> roro run python train.py
Started new job ed5906db

#inspect processes, make sure training is finished before using service
> roro ps
JOBID     STATUS    WHEN            TIME     INSTANCE TYPE    CMD
--------  --------  --------------  -------  ---------------  -------------------------------------
f9400f3e  running   1 minute ago    0:01:47  C1               firefly -b 0.0.0.0:8080 train.predict
ed5906db  running   23 seconds ago  0:00:23  C1               python train.py

```


#### Steps (verbose)
1.	Clone the code repository rorodata/credit-scoring-demo (manually or using git) and download the files to a local directory. You will shortly deploy this repository on rorocloud as your own project.
2.	Pick a unique project name for the project you are about to create on the data platform. Remember to keep a short readable name without spaces or special characters (hyphen is ok). 
3.	Edit the roro.yml file, and change the part after project: to match your project name exactly, and save it. The roro.yml is a simple text file that tells the rorodata platform what to do during deployment. You can understand more about the structure and specifications that can go into the YML file here 
4.	You will now deploy code from the local repository you just edited, into production on rorodata platform.  Navigate to the above mentioned repository using command prompt. From here, login to the rorodata platform using roro login from command prompt. You are now using roro client connected to rorodata platform. Send us an email if you run into any issues and we shall help you out quickly
5.	Create your (new) project using the command roro create your-project-name. Remember to us the same name you picked in step 2,3. Remember, this project is the entire machine learning application including its code, all associated tasks and services, persistent data volumes, and ML models. Once done, you can use the command roro projects to view a list of all your projects. Make sure that you can see the project you just created.
6.	You are now ready to deploy your project code to production. From the same command prompt location as in the previous step, type roro deploy and press enter. This When a project is deployed, rorodata takes its cue from the roro.yml file and execute deployment steps one by one. You can see a list / trace of all these steps once roro deploy finishes.
7.	To train the model, run the command roro run python train.py from the same command prompt location. Once this finishes, you have a new model ready to serve prediction requests. rorodata platform helps you save models including model metadata, for every version. To understand how this is done, go here.
8.	Your services should now be ready and serving, with URL endpoints for each service as instructed by you in the roro.yml file.   You can check if the service is running using the command roro ps –a.  In rare cases, the service may fail due to a conflict e.g. if the trained model was not available at the time of launching service. Simple rerun roro deploy from the command prompt and the service will come up 
9.	The rorodata platform services are REST-APIs, and can be accessed using any client service. The easiest way to test this is through our firefly library. You can install this using pip install firefly-python and query the service using the same example as in the notebook
10.	Let’s now use the API we created, to predict if we should give loan to a new applicant, using his data attributes as inputs to our model


```
new_loan_application= { 'delinq_2yrs': 0.0,
 'delinq_2yrs_zero': 1.0,
 'dti': 8.72,
 'emp_length_num': 0,
 'grade': 'F',
 'home_ownership': 'RENT',
 'inq_last_6mths': 3.0,
 'last_delinq_none': 1,
 'last_major_derog_none': 1,
 'open_acc': 2.0,
 'payment_inc_ratio': 4.5,
 'pub_rec': 0.0,
 'pub_rec_zero': 1.0,
 'purpose': 'vacation',
 'revol_util': 98.5,
 'short_emp': 0,
 'sub_grade_num': 1.0}

#we will use firefly to call our API, you can use any other library e.g. Requests
import firefly

#change the below statement to match your prediction service api name
client = firefly.Client(“credit-scoring-demo.rorodata.io”)

client.predict(row=new_loan_application)
```
