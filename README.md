### DESCRIPTION
   A Machine learning application to predict whether or not a patient has diabetes.

## MOTIVATION
- To gain experience in executing life-cycle of data science projects(data collection, feature engineering, feature selection, model selection, model hyper parameter tuning and model deployment).  
- To contribute on sharing knowledge to the data science community. 
  

## DATA SOURCE
The data is source is here [UCI-Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
# Built with
<code><img height="50" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="50" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>
<code><img height="50" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png"></code>
<code><img height="50" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
<code><img height="50" src="https://symbols.getvecta.com/stencil_80/56_flask.3a79b5a056.jpg"></code>
<code><img height="50" src="https://cdn.iconscout.com/icon/free/png-256/heroku-225989.png"></code>
<code><img height="50" src="https://github.com/ourylydibin/Banknote-Authentication/blob/main/static/css/dockerr.jpg"></code>



<code><img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="30" src="https://matplotlib.org/_static/logo2.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>


## DEPLOYMENT
#### This application is deployed to [Heroku](https://dashboard.heroku.com).
#### You can access the application [here](https://diabeteprediction.herokuapp.com/).
#### Note: Making a query may take few secondes to load the data sometimes, as the server may be in hibernate state.

## CHALLENGES
- The issue was that after installing docker it was not starting. After reading some Stackoverflow pages they were saying that I had to enable the virtual machine. Once I did that from the Bios it worked.
- I had other issues when creating the Dockerfile. Docker could not build the docker image because I did not include the right base image in the file. It worked after I pulled the right image.
- I had also problems with misunderstanding some docker and Kubernetes commands. But everything was solved after reading some blogs.   

## How to use
- In the application bars, type only numerical values(positive of negative values). If you type other than numerical values you will be getting an error.

- Once you type the convenient values, click on the submit botton to get the result of the prediction.
  
  
## DEMO

   ### Diabetes Detection

![demo](https://media.giphy.com/media/kK1Y0WIc7UzYFDN9p2/giphy.gif)


## Usage
You can use this project for further developing it and adding your work in it. If you use this project, kindly mention the original source of the project and mention the link of this repo in your report.

## Further Improvements
There are somethings to improve upon

- CSS style is not in the CSS folder instead I have included the style in the html code. When I included the CSS in the CSS folder, it was not having effect on the application interface :cry:
- One can include a deep learning model in the model selection as one of the candidate.
- The application can be modularized.
- 
## Contact
