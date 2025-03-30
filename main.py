from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse
import shutil, os, zipfile, pandas as pd
from tempfile import TemporaryDirectory

app = FastAPI()


@app.post("/api/")
async def solve_question(
        question: str = Form(...),
        file: UploadFile = File(None)
):
    print(f"Received question: {question}")
    if file:
        print(f"Received file: {file.filename}")

        # Create a temporary directory to work in
        with TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, file.filename)

            # Save the uploaded file to disk
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            # Check if it's a zip file
            if zipfile.is_zipfile(file_path):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(tmpdir)

                # Find CSV file inside the zip
                for name in os.listdir(tmpdir):
                    if name.endswith(".csv"):
                        csv_path = os.path.join(tmpdir, name)

                        # Read CSV and extract value from "answer" column
                        df = pd.read_csv(csv_path)
                        if "answer" in df.columns:
                            # Just return the first non-null value
                            answer = df["answer"].dropna().iloc[0]
                            return JSONResponse(content={"answer": str(answer)})
                        else:
                            return JSONResponse(content={"answer": "No 'answer' column found in CSV."})

                return JSONResponse(content={"answer": "No CSV file found in the ZIP."})
            else:
                return JSONResponse(content={"answer": "Uploaded file is not a ZIP."})

    return JSONResponse(content={"answer": f"Dummy answer for: {question}"})
