// Function to update the chart dynamically with data from FastAPI endpoint
async function updateBarChart() {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/bar-chart-data');
    const data = await response.json();

    // Extract data from the response
    const labels = data.labels;
    const chartData = data.data;

    // Update the chart data dynamically
    myBarChart.data.labels = labels;
    myBarChart.data.datasets[0].data = chartData;

    // Re-render the chart with the new data
    myBarChart.update();
  } catch (error) {
    console.error('Error fetching chart data:', error);
  }
}

// Set up the initial chart
const myBarChart = setupBarChart();
