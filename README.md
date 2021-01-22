# 2AF_FRAUD_DETECTION
REST API for FRAUD DETECTION

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
        "prediction": "0"
    }
/api/v0/info
this endpoint give you the information you need to know about the API , the result look like this , you can add as many details as you like

 {
    'Author' : '2AF',
    'description' : 'A fraud detection model using a Credit Card Dataset',
 }
