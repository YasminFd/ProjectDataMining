TESTER = document.getElementById('tester');

var trace1 = {
    x: [1, 2, 3, 4],
    y: [10, 11, 12, 13],
    mode: 'markers',
    marker: {
        size: [40, 60, 80, 100]
    }
};

var data = [trace1];

var layout = {
    title: {
        text: 'Marker Size'
    },
    showlegend: false,
    autosize: true ,
    margin: { l: 40, r: 40, t: 40, b: 40 },// Automatically adjust to container size
};

// Render the plot
Plotly.newPlot(TESTER, data, layout, { responsive: true });

// Resize on window change
window.addEventListener('resize', function () {
    Plotly.Plots.resize(TESTER);
});