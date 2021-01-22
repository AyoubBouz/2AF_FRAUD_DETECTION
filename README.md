
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/pull/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# 2AF_FRAUD_DETECTION
REST API for FRAUD DETECTION

<<<<<<< HEAD
The API acces points
to be able to use the api , you need first install the requirements

pip install flask
Then test the application by runing the code :

python api.py
the app will be running on local host port 5000 with the endpoints :

/api/v0/verify
This endpoint get a JSON object in a post method , that represents the new transaction

 {
 "Merhchant": "M856947123",
"Customer": "C1093826151",
"Category":"es_health",
 "Amount" : 149.62
 }
The return result looks like this :

    {
        "id": 0,
        "prediction": "[0]"
    }
/api/v0/info
this endpoint give you the information you need to know about the API , the result look like this , you can add as many details as you like

 {
    'Author' : '2AF',
    'description' : 'A fraud detection model using a Credit Card Dataset',
 }
=======
### 8 steps for Finding Fraud Rings Using Graph Technology

The steps below are just one example. Your approach will vary depending on your goals and the data itself.

1-Use graph queries to uncover a suspicious pattern, such as multiple users coming from the same IP address. (Some of the techniques used in the first-party fraud example from blog 3 in this series will also apply.)

2-Use Community Detection algorithms to identify strongly connected communities engaged in known fraud across various accounts using email addresses, phone numbers, authorized users and previously flagged activity.

3-Use the Louvain Modularity graph algorithm to examine whether hierarchies exist among these communities. Set thresholds to separate petty thieves from fraud rings so that investigators prioritize their efforts.

4-Use a Centrality algorithm like PageRank to uncover influential individuals and to identify high frequency paths.

5-After verifying the pattern of one fraud ring, use a Similarity algorithm such as Jaccard to identify other potential fraud participants and rings across your data.

6-Once the approaches to find fraud rings have been validated by investigators, and a labeled and scored dataset has been created, you can use these graph-based features in a machine learning pipeline.

7-Extract the calculated node and relationship properties – graph features from the previous step – into your ML environment (e.g., into a Python notebook). Join those properties with any other relevant tabular data. Use variable selection and model-building techniques to pinpoint the most important features and use them to predict future fraudulent activities or entities.

8-Once you’re satisfied with your results, move your model into production. Write back any relevant findings to the Neo4j Graph Database to support further exploration.


>>>>>>> 5588a352dea1a8f58a272f06dd2c47e94493ca9a
