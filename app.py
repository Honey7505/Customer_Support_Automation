from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agents.query_agent import QueryAgent
from agents.order_agent import OrderAgent
from agents.recommendation_agent import RecommendationAgent
from config import settings
from utils.utils import log_request, format_response
from pydantic import BaseModel
from typing import Dict, Any
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "Frontend"),
    name="static"
)

class QueryRequest(BaseModel):
    message: str
    context: Dict[str, Any] = {}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize agents
query_agent = QueryAgent()
order_agent = OrderAgent()
recommendation_agent = RecommendationAgent()

@app.get("/")
async def home():
    return FileResponse(BASE_DIR / "Frontend" / "index.html")

@app.post("/api/handle_query")
async def handle_query(request: QueryRequest):

    user_input = request.message
    user_context = request.context

    log_request(user_input)

    if "order" in user_input.lower():
        response = order_agent.handle(user_input, user_context)
    elif "recommend" in user_input.lower():
        response = recommendation_agent.handle(user_input, user_context)
    else:
        response = query_agent.handle(user_input, user_context)

    formatted_response = format_response(response)
    return {"response": formatted_response}
'''async def handle_query(request: Request):
    data = await request.json()
    user_input = data.get("message")
    user_context = data.get("context", {})

    log_request(user_input)

    # Simple keyword-based routing (for demonstration)
    if "order" in user_input.lower():
        response = order_agent.handle(user_input, user_context)
    elif "recommend" in user_input.lower():
        response = recommendation_agent.handle(user_input, user_context)
    else:
        response = query_agent.handle(user_input, user_context)

    formatted_response = format_response(response)
    return {"response": formatted_response}'''

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
