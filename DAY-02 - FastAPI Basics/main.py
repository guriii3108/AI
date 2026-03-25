from fastapi import FastAPI
app = FastAPI()

@app.get("/") #get request
def day2():
  return {"message":"Day 2 of fastAPI"}

@app.post("/post") #post request
def day2():
  return {"message":"POST request"}

@app.put("/put") #put request
def day2():
  return {"message":"PUT request"}

@app.delete("/delete") #delete request
def day2(): 
  return {"message":"DELETE request"} 
