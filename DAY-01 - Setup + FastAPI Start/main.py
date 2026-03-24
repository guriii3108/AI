from fastapi import FastAPI
app = FastAPI()

# make Routes now
@app.get("/test")
def test():
  return {"message":"Testingggg"}
  
@app.get("/hello")
def hello():
  return {"msg":"Hello from Guri"}