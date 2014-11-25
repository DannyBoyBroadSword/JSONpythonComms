import requests
#Library for Post Get and Put Requests
import json
#Handels Data
from __builtin__ import raw_input
#Auto IMport thanks eclipse
def initiate():
    #initiate() creates a url with some "data" 
    headers = {'content-type': 'application/json'}
    #headers make everything smoothe
    data=json.dumps({"Data":[]})
    #dump that data with zero list
    r = requests.post("https://api.myjson.com/bins", data,headers)
    #awsome website stores json data 
    decoded = r.json()
    #it returns an enocded url of were the data is sitting Return it to use in other functions or just call it to start a new data instance. 
    return decoded["uri"]

def getdata(elements):
    data = []
    #get data but first make a list.
    for i in range(elements):
        #we ask the programmer how many data objects are their. For each one we then ask okay whats the data. 
        input_element = raw_input("Data: ")
        data.append(input_element)
    return data
    #return the data in hopes of using it to update(Put) or create data instance (POST)
 
def update():
    #This will update an existing data instance
    andrew=getdata(10)
    # we want data so we call the data function and how many pieces as the argument. 
    payload = {"Command":andrew}
    #the payload is the command object with its dict or list andrew which is the getdata(10) thing
    headers = {'content-type': 'application/json'}
    # headers make everything smoother
    bob = "https://api.myjson.com/bins/1hdk7"
    #bob = initiate()
    #this will create new data instance but you can update if you want you will have to define urls in public vars so that your program doesn't make new instances update is called
    r = requests.put(bob,data=json.dumps(payload),headers = headers)
    we ask requests to make a new object r with the mehtod put and pass in the url the data and the headers
    decoded = json.dumps(r.json())
    #this returns the data that was updated
    print(decoded)
    print("At "+bob)
    #this prints were the data is
#You will Have to Copy in Url or Prebuild and import
update()
# we call update to start the whole process. 
