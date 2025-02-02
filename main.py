from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Add CORS middleware to allow all origins for GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],  # Allow all headers
)

# Load the marks file
with open('q-vercel-python.json', 'r') as file:
    marks_data = json.load(file)

@app.get("/api")
async def get_marks(request: Request):
    # Retrieve the query parameters manually from the request object
    name = request.query_params.getlist("name")
    print(f"Received names: {name}")  # Debugging line to show the received query parameters

    result = []
    for n in name:
        # Search through the list of dictionaries to find the matching name
        mark = next((item['marks'] for item in marks_data if item['name'] == n), None)
        result.append(mark)  # Append the found mark, or None if not found

    return JSONResponse(content={"marks": result})
