# BE-01 Build your first CRUD API

This project involves building a CRUD api to handle task management.
It uses python 3.12 and FastAPI.

---

## Features

* **Full CRUD Operations:** GET, POST, PUT, and delete.
* **Input Validation:** Uses pydantic and rejects empty or whitespace-only task titles with `400 Bad Request`.
* **Proper HTTP Status Codes:** Uses `200`, `201`, `204`, `400`, and `404` accurately.
* **Interactive API Docs:** Built-in Swagger UI documentation hosted natively at `/docs`.
* **In-Memory Storage:** Keeps track of tasks state in memory without external database dependencies.

---

## Getting Started

### Prerequisites

* Python 3.12
* `uv` or `pip` package manager (I recommend uv)

### Installation & Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhammed-Yilmaz2003/Flyrank-backend.git
   cd Flyrank-backend/BE-01
   ```

2. **Install dependencies:**

   *if using `pip`:*
   ```bash
   pip install fastapi[standard] uvicorn pydantic
   ```
   *if using `uv`:*
   ```bash
   uv add fastapi uvicorn
   ```

3. **Start the server:**

   *if using `pip`:*
   ```bash
   uvicorn main:app --reload --port 8000
   ```
   *if using `uv`:*
   ```bash
   uv run fastapi dev
   ```
   The API will start listening at `http://127.0.0.1:8000`.

---

## Endpoints Summary

| HTTP Method | Endpoint | Description | Success Status | Error Statuses |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/` | Returns basic API metadata | `200 OK` | — |
| `GET` | `/health` | Server health check | `200 OK` | — |
| `GET` | `/tasks` | List all tasks or search or query| `200 OK` | — |
| `GET` | `/tasks/{id}` | Retrieve a specific task by ID | `200 OK` | `404 Not Found` |
| `POST` | `/tasks` | Create a new task | `201 Created` | `400 Bad Request` |
| `PUT` | `/tasks/{id}` | Update title and/or done status | `200 OK` | `400 Bad Request`, `404 Not Found` |
| `DELETE` | `/tasks/{id}` | Delete a task by ID | `204 No Content` | `404 Not Found` |

---

## Sample Request & Response

Here is an example of creating a new task using `curl`:

### Command
```bash
curl -i -X POST [http://127.0.0.1:8000/tasks](http://127.0.0.1:8000/tasks) \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk"}'
```

### Output
```http
HTTP/1.1 201 Created
date: Wed, 16 Sep 2026 12:00:00 GMT
server: uvicorn
content-length: 42
content-type: application/json

{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

---

## Interactive Documentation (Swagger UI)

FastAPI automatically generates interactive OpenAPI documentation. 

Once the server is running, visit **`http://127.0.0.1:8000/docs`** in your browser to test endpoints directly via your web browser.

![Swagger UI Screenshot](/BE-01/assets/firefox_yhkxOqHncw.png)
