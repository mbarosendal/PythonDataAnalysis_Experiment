# C# and Python Analytics Integration

This project demonstrates how an ASP.NET Core backend (C#) can leverage a Python analytics service to generate summaries and PDF reports from student activity data.

## Features
- **C# Backend**: Sends student data to the Python service.  
- **Python Service**: Accepts data, uses pandas/matplotlib to generate summaries and PDF reports, returns JSON + Base64 PDF.

## Setup

### Python Service
```bash
python -m venv venv
.\venv\Scripts\activate          # Windows PowerShell
pip install fastapi uvicorn pandas matplotlib pydantic
# OR if requirements.txt is available:
pip install -r requirements.txt
uvicorn analytics_service:app --reload --port 8000
```

### C# Backend
```
# Ensure Python service is running
dotnet run
```

The C# backend sends the data to the Python endpoint and returns a PDF with charts, that will be generated in the root folder of the C# project.
