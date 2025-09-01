# C# and Python Analytics Integration

This is a small test project for my [semester portfolio](https://mbarosendal.github.io/Portfolio/) that demonstrates how an ASP.NET Core backend (C#) can leverage a Python analytics service to generate summaries and PDF reports from student activity data.

## Features
- **C# Backend**: Sends student data to the Python service.  
- **Python Service**: Accepts data, uses pandas/matplotlib to generate summaries and PDF reports, returns JSON + Base64 PDF.

## Setup

### Python Service terminal
```bash
1) Create a venv:                              python -m venv venv
2) Activate the venv:                          .\venv\Scripts\activate
3) Intall dependencies:                        pip install fastapi uvicorn pandas matplotlib pydantic
  - # OR if requirements.txt is available:     pip install -r requirements.txt
4) Run the project:                            uvicorn analytics_service:app --reload --port 8000
```

### C# Backend terminal
```
# 1) Ensure Python service is running:         dotnet run
```

### Alternatively
To avoid manual setup, just run the test_script.ps1 in /Test_Script/. It should run the projects automatically and generate the report.

The resulting PDF with charts will be generated in the root folder of the C# project.
