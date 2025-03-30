# TDS Solver API (IIT Madras - Tools in Data Science)

This is a Python-based API to solve graded assignment questions automatically using LLMs and file processing. It is designed for the Tools in Data Science course offered by IIT Madras' Online Degree Program.

## Features
- Accepts questions and optional file attachments via a `/api/` POST endpoint
- Processes assignment questions and extracts answers from uploaded files
- Returns the answer as a JSON response
- Built with FastAPI and deployable on platforms like Vercel

## Project Structure (WIP)
```
tds_solver/
├── main.py
├── README.md
├── venv/ (optional virtual environment)
```

## 🧰 Requirements
Install the required dependencies:

```bash
pip install fastapi uvicorn python-multipart aiofiles pandas
```

## 🔧 Setup Instructions

### 1. Create and activate a virtual environment (optional)
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 2. Install dependencies
```bash
pip install fastapi uvicorn python-multipart aiofiles pandas
```

### 3. Run the API locally
```bash
uvicorn main:app --reload
```

This will start the server at `http://127.0.0.1:8000`.

## 🧪 Testing the API

### Option 1: Swagger UI (Recommended for beginners)
- Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Find the `POST /api/` section
- Click **Try it out**
- Enter a question (e.g. `What is 2 + 2?`)
- Upload a file if needed (optional)
- Click **Execute**

### Option 2: Using `curl`
#### With both question and file:
```bash
curl -X POST "http://127.0.0.1:8000/api/" -H "Content-Type: multipart/form-data" -F "question=What is the answer?" -F "file=@C:/Repositories/TDS-Solver/test.zip"
```
Make sure your ZIP file contains a CSV (like `extract.csv`) with an `answer` column.

#### With question only (no file):
```bash
curl -X POST "http://127.0.0.1:8000/api/" -H "Content-Type: multipart/form-data" -F "question=What is the answer?"
```

---

## 🚧 Work in Progress
We are building this project step-by-step:
1. ✅ Environment setup
2. ✅ Basic FastAPI endpoint
3. ✅ Handle multipart form-data (question + file)
4. ✅ File processing (ZIP + CSV)
5. ⏳ Integrate LLM for dynamic answers
6. ⏳ Deployment

Stay tuned!

