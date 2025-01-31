from imports import *
print("Initializing FastAPI app...")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific domains in production)
    allow_methods=["GET"],
    allow_headers=["*"],
)
import endpoints
print("Initializing FastAPI app endpoints imported...")
@app.get("/sse")
def sse():
    def event_stream():
        while True:
            time.sleep(3)  # Simulate live updates
            yield f"data: Server time is {time.ctime()}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")

# ✅ Keep the server running!
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
