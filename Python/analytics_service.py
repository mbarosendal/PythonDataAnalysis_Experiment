# file: analytics_service.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import io
import base64

# 1) Create venv for project: python -m venv venv ✔️ 
# 2) Activate venv: .\venv\Scripts\activate (from project root folder)
# 3) Install dependencies: pip install fastapi uvicorn pandas matplotlib pydantic ✔️ 
# OR if requirements.txt available: pip install -r requirements.txt ✔️ 
# 4) Run with: uvicorn analytics_service:app --reload --port 8000

app = FastAPI(title="LMS Analytics Service")

# Base model with alias to accept C#'s CamelCase
class StudentActivity(BaseModel):
    student_id: int = Field(..., alias="studentId")
    login_count: int = Field(..., alias="loginCount")
    time_spent_minutes: float = Field(..., alias="timeSpentMinutes")
    submissions: int

@app.post("/generate-report")
async def generate_report(data: list[StudentActivity]):
    print("Received student data! Generating PDF report...")

    df = pd.DataFrame([d.dict() for d in data])

    summary = {
        "total_students": len(df),
        "average_logins": df["login_count"].mean(),
        "average_time_spent": df["time_spent_minutes"].mean(),
        "average_submissions": df["submissions"].mean()
    }

    # Generate PDF report with three models
    buffer = io.BytesIO()
    with PdfPages(buffer) as pdf:

        # Login Count
        plt.figure(figsize=(8,6))
        plt.bar(df['student_id'], df['login_count'], color='skyblue')
        plt.xlabel("Student ID")
        plt.ylabel("Login Count")
        plt.title("Student Login Count")
        pdf.savefig()
        plt.close()

        # Time Spent
        plt.figure(figsize=(8,6))
        plt.bar(df['student_id'], df['time_spent_minutes'], color='orange')
        plt.xlabel("Student ID")
        plt.ylabel("Time Spent (minutes)")
        plt.title("Student Time Spent")
        pdf.savefig()
        plt.close()

        # Submissions
        plt.figure(figsize=(8,6))
        plt.bar(df['student_id'], df['submissions'], color='green')
        plt.xlabel("Student ID")
        plt.ylabel("Submissions")
        plt.title("Student Submissions")
        pdf.savefig()
        plt.close()

    # Encode PDF to base64 string
    buffer.seek(0)
    pdf_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    print("PDF report generated successfully!")
    return JSONResponse({"summary": summary, "report_base64": pdf_base64})
