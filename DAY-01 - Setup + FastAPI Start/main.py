from fastapi import FastAPI #importing FastAPI
app = FastAPI() #creating an instance of FastAPI


@app.get("/test") #decorator to define a route
def test(): #defining a function to handle the GET request to /test
  return {"message":"Testingggg"} #returning a JSON response
  
@app.get("/hello")
def hello():
  return {"msg":"Hello from Guri"}