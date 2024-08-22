## Heart-Disease-Prediction-Model-Deployment-with-IBM-Watson-Studio-as-a-web-service

### Overview

A simple web application which uses Machine Learning algorithm to predict the heart condition of a person by providing some inputs about the person health like age, gender, blood pressure, cholesterol level etc built using `Flask`

 ### Technical Aspect
 
 This Project is mainly divided into two parts:
 
 1. Exploring the dataset and training and deploying the model in IBM Watson Studio.
 2. Integrating the Deployed Model with the Flask application using the provided API endpoint.

**About the repository Structure :**

- Project consist `app.py` script which is used to run the application and is engine of this app. contians API that gets input from the user and computes a predicted value based on the model.
- "templates" folder contains two files `main.html` and `result.html` which describe the structure of the app and the way this web application behaves. These files are connected with Python via Flask framework.  
- "static" folder contains file `style.css` which adds some styling and enhance the look of the application. 

### Requirements

- In the `app.py` script replace the '<API-Key>' and '<Deployment_ID>' with your IBM Cloud account API_Key and your model's deployment id respectively.
- replace the <Access_Token> with the access token you generate using the API Key

### Run 

- To Run the Application : python app.py

### Technologies used 

- IBM Cloud Watson Studio: This serves as the backend for model deployment and management. It includes features for model deployment, scalability, and monitoring.
- Flask Application: This frontend component provides a user-friendly web interface. Users can access the heart disease prediction tool through a form, input their health-related data, and receive predictions.

### Future work 

- improve model performance.
- Add more better styling to the user interface.








  
  
  


