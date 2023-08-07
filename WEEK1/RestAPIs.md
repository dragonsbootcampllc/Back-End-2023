> Name: Kerolos Emad Saad,
>
>  Dragons Bootcamp summer 2023 Back-end,
>
> WEEK 1 : web fundamentals,
>
> Task: REST  APIs,
---


# API (Application Programming Interface)
At first, I want to mention one of the uses of the API which we find repeated in our daily lives to clarify an initial idea of how the API works
- while using an Application (UBER) or any app for delivery we use google maps to access our location
In this case, Google Maps offers these applications its own API to access the location
- Any Website or Application dealing with file management systems to upload files 

# How API works ??? 
To know how the API works we want to know how the websites work in the traditional way without API 
As shown in Figure 1
1-The client request to get the website to the server (Request)
2-The server asks to get the data from the database
3-The database sends data to the server
4-The server fills the data into the HTML file 
5-The server sends this HTML file to the browser (Response)
6-The browser converts the HTML codes to visual format for the user
By using this way The codes of the Frontend(HTML+css+JS) and backend (Python+postgress) in one project Which are known as linked sites
This is another method (How the websites work) dependent on the API
In this way The client does not deal with the server directly but using API
As shown in Figure 2
1-The client sends an API request to the server  
2-The server asks to get the data from the database
3-The database sends data to the server
4-The server collects the data and builds API
5-The server sends API to the browser (Response)
6-The browser read the API (data only) and converts it to visual format for the user
By using this way The codes of frontend and backend don't be gathered in one project which is known as separate sites

# A simple classification of APIs
web service APIs: Soap, REST
Library-Based APIs: Javascript, TWAIN
Class-based APIs: Java API, Android API
OS functions and routines: Access to the file system, Access to the user interface
Object remoting APIs: CORBA,.Net Remoting
Hardware APIs: Hard disk drives, PCI buses

We will get to know the REST APIs but before that, we should know about HTTP protocol and HTTP methods

# HTTP Protocol
It depends on the Request, Response 
As shown in Figure 3
- The client makes a request to deal with data through HTTP protocol by using HTTP methods (GET, POST, PUT, PATCH, DELETE)
- The Database server sends a response which is usually a JSON (Javascript object notation): an easy formula to represent data that consists of a value and a key

# HTTP methods
- GET: retrieve an existing resource
- POST: create a new resource
- PUT: Update an existing resource
- Patch: partially update an existing resource
- Delete: Delete a resource 

> Note:: Web service is an API, but in order for it to work, it needs the HTTP protocol and Network, so we can say that every web service is an API, and not every API is a web service

#  REST (REpresentation State Transfer) APIs
- Depends on client-server protocol (ex: HTTP)
- Transfer Server objects as resources
- It uses HTTP methods to get data from Database Server

## 1)GET method
```py

import requests
api_url='.............'
response=requests.get(api_url)
print(response.json())
```

## 2)POST method
```py
import requests
api_url='.............'
new={"ID":258,"name":Carlos)
response=requests.post(api_url,json=new)
print(response.json())

```

## 3)PUT method
```py
import requests
api_url='.............'
response=requests.get(api_url)
print(response.json())
new={"ID":258,"name":Ali)
response=requests.put(api_url,json=new)
print(response.json())
```

## 4)PATCH method
```py

import requests
api_url='.............'
response=requests.get(api_url)
print(response.json())
new={"name":Ahmed)
response=requests.patch(api_url,json=new)
print(response.json())
```

## 5)Delete method
```py
import requests
api_url='.............'
response=requests.delete(api_url)
print(response.json())

```

