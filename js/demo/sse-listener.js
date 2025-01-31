const eventSource = new EventSource("http://127.0.0.1:8000/sse");

eventSource.onmessage = function(event) {
    UpdateAll();
};