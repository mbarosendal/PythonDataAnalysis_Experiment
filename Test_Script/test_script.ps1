# Root folder of the project (one level up from the script)
$rootDir = Join-Path $PSScriptRoot ".." | Resolve-Path

# Join root with the directories for the Python and C# projects
$pythonDir = Join-Path $rootDir "Python"
$csharpDir = Join-Path $rootDir "Csharp\student_activity"

# Start the Python service
Write-Host "Starting Python analytics service..."
Start-Process powershell -ArgumentList "-NoExit", "-Command Set-Location '$pythonDir'; .\venv\Scripts\Activate.ps1; uvicorn analytics_service:app --reload --port 8000"

# Wait a few seconds to make sure the Python service is up
Start-Sleep -Seconds 7

# Start the C# backend
Write-Host "Starting C# ASP.NET Core backend..."
Set-Location $csharpDir
dotnet run

Write-Host "Report should be available in directory: $csharpDir"