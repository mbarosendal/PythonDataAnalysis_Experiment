using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Net.Http;
using System.Net.Http.Json;
using System.Text.Json;

namespace PythonDataAnalysis_Experiment.Services
{
    public class ActivityService
    {
        public class StudentActivity
        {
            public int StudentId { get; set; }
            public int LoginCount { get; set; }
            public float TimeSpentMinutes { get; set; }
            public int Submissions { get; set; }
        }

        public async Task SendActivitiesAsync()
        {
            var httpClient = new HttpClient();
            var resultsJson = string.Empty;

            var data = new List<StudentActivity>
            {
                new StudentActivity { StudentId=1, LoginCount=5, TimeSpentMinutes=120, Submissions=13 },
                new StudentActivity { StudentId=2, LoginCount=1, TimeSpentMinutes=75, Submissions=5 },
                new StudentActivity { StudentId=3, LoginCount=7, TimeSpentMinutes=200, Submissions=15 }
            };

            try
            {
                var response = await httpClient.PostAsJsonAsync("http://localhost:8000/generate-report", data);
                Console.WriteLine("Sending student activities...");
                resultsJson = await response.Content.ReadAsStringAsync();
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error sending student activities: {ex.Message}");
            }

            if (resultsJson != null)
            {
                var date = DateTime.Now;

                Console.WriteLine("Results received:");
                using JsonDocument doc = JsonDocument.Parse(resultsJson);
                string pdfBase64 = doc.RootElement.GetProperty("report_base64").GetString();
                byte[] pdfBytes = Convert.FromBase64String(pdfBase64);
                File.WriteAllBytes($"weekly_report({date:f}).pdf", pdfBytes);
            }
        }
    }
}