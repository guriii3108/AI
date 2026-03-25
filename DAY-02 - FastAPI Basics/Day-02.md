# 📘 Day 02 — FastAPI Basics (HTTP Methods Deep Dive)

📅 **25 March 2026 (Wednesday)**

---

## 🎯 What I Learned Today

- How APIs communicate using **HTTP methods**
- The difference between **GET vs POST** (and PUT, DELETE)
- How to create multiple endpoints in FastAPI
- Using **Swagger UI** to test APIs without a frontend

---

## 🧠 Core Concept — HTTP Methods

When a client talks to a server, it uses **HTTP methods** to describe *what it wants to do*.

| Method | Purpose | Real-world Example |
|--------|---------|-------------------|
| `GET` | Fetch / retrieve data | Opening a webpage, fetching user profile |
| `POST` | Send / create data | Login form, asking ChatGPT a question |
| `PUT` | Update existing data | Editing your profile |
| `DELETE` | Remove data | Deleting a post |

---

## 🔹 GET vs POST — Real Understanding

### GET Request
> Used to **retrieve** data. Data is passed in the **URL**.

```
GET /users
```

- ✅ No request body (mostly)
- ✅ Fast & simple
- ✅ Bookmarkable / shareable URL
- ❌ Not for sensitive data

---

### POST Request
> Used to **send** data to be processed. Data is in the **request body** (JSON).

```
POST /ask
Body: { "question": "What is AI?" }
```

- ✅ Has a request body (JSON)
- ✅ More secure (data not in URL)
- ✅ Used for AI queries, form submissions
- ❌ Not cacheable

---

## 💻 Code I Built Today

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")           # Fetch homepage
def day2():
    return {"message": "Day 2 of FastAPI"}

@app.post("/post")      # Send data
def day2():
    return {"message": "POST request"}

@app.put("/put")        # Update data
def day2():
    return {"message": "PUT request"}

@app.delete("/delete")  # Delete data
def day2():
    return {"message": "DELETE request"}
```

---

## 🌐 Swagger UI — The Superpower

FastAPI gives you **free auto-generated docs** at:

```
http://127.0.0.1:8000/docs
```

### Why it's awesome:
- 🧪 Test all your endpoints without writing frontend code
- 📄 Auto-documents every route
- 👀 Shows request/response format clearly

---

## 🧪 Mini Challenge

> Create a `/status` endpoint that returns `"Server is healthy"` ✅

```python
@app.get("/status")
def status():
    return {"status": "Server is healthy"}
```

---

## ⚠️ Common Mistakes

| Mistake | Fix |
|---------|-----|
| Using `GET` when you should use `POST` | Think: *fetching* = GET, *sending* = POST |
| Server not reflecting changes | Make sure `--reload` flag is on |
| Multiple functions with same name | Give each function a unique name |

---

## 📌 Key Takeaways

- **GET** = fetch data (read-only)
- **POST** = send/process data
- **PUT** = update existing data
- **DELETE** = remove data
- FastAPI's **Swagger UI** at `/docs` is your best friend for testing
