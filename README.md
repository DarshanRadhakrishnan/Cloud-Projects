## 1. Why do we need Mangum?

### The Problem: Language Mismatch

FastAPI is designed to speak **HTTP**.  
It expects requests that look like standard web traffic (`GET` / `POST` requests, headers, paths).

AWS Lambda does not speak HTTP naturally.  
It speaks **"JSON Events."**

When a Lambda is triggered, it receives a generic Python dictionary  
(e.g., `{'resource': '/', 'path': '/', 'httpMethod': 'GET'...}`).

---

### The Solution: Mangum is the Translator

When a request hits your Lambda, **Mangum** catches the AWS Event.

It converts that event into a standard **HTTP request** that FastAPI can understand.

FastAPI processes it and sends back a response.

Mangum catches that response and converts it back into the **JSON format** that AWS Lambda expects.

Without Mangum, your FastAPI app would receive the AWS event, get confused,  
and crash because it wouldn't know how to read the input.

---

## 2. Why do we need to create a ZIP file?

### The Problem: AWS Lambda is "Empty"

When AWS creates a Lambda environment for you, it gives you:
- A basic Linux environment
- Python installed

It does **not** have:
- FastAPI
- Mangum
- Any other libraries installed

It is just a **bare-bones Python runner**.

If you just uploaded your `todo.py` file, the code would fail immediately on the first line  
(`import fastapi`) because that library simply doesn't exist on the AWS server.
