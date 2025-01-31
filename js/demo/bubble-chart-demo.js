// Function to update chart dynamically
async function fetchChartData() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/bubble-chart-data');
        return await response.json();
    } catch (error) {
        console.error('Error fetching chart data:', error);
        return null;
    }
}
async function updateBubbleChart() {
    // Fetch data from the endpoint
    const data = await fetchChartData();
    console.log("Fetched data:");
    console.log(data);  // Debug the structure of the fetched data

    if (data && data.x && data.y && data.size) {
        // Ensure trace1 is properly initialized
        let trace1 = {
            x: data.x,          // Data for x-axis
            y: data.y,          // Data for y-axis
            mode: 'markers',    // Plot markers
            marker: {
                size: data.size // Marker sizes
            }
        };

        // Define layout for the chart
        const layout = {
            title: {
                text: 'Dynamic Marker Size'
            },
            showlegend: false,
            autosize: true,
            margin: { l: 40, r: 40, t: 40, b: 40 }
        };

        // Efficiently update the chart with Plotly.react
        Plotly.react(document.getElementById('chart-area-tester'), [trace1], layout);
    } else {
        console.error("Invalid data format:", data);
    }
}

// Initialize chart and set interval for updates
setupChart(); // Update every 5 seconds