using PythonDataAnalysis_Experiment.Services;

/// Instructions ///
// 1) After Python service is running, just: dotnet run

var builder = WebApplication.CreateBuilder(args);

// Learn more about configuring OpenAPI at https://aka.ms/aspnet/openapi
builder.Services.AddOpenApi();
builder.Services.AddLogging();
builder.Logging.ClearProviders();
builder.Logging.AddConsole();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.MapOpenApi();
}

app.UseHttpsRedirection();

var activityService = new ActivityService();
await activityService.SendActivitiesAsync();

app.Run();
