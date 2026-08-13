from fastapi import FastAPI
from mcp.server.fastapi import create_mcp_fastapi_router
from composio_mcp import ComposioMcpServer
import os

app = FastAPI(title="Yeastar Calendar MCP")

# Initialisation du serveur Composio MCP en filtrant UNIQUEMENT Google Calendar
composio_server = ComposioMcpServer(
    api_key=os.environ.get("COMPOSIO_API_KEY"),
    apps=["GOOGLECALENDAR"] # On bloque le Tool Router, on ne garde que l'agenda
)

# On connecte le serveur Composio au routeur FastAPI pour le flux SSE
router = create_mcp_fastapi_router(composio_server.server)
app.include_router(router)

# Note pour Render : le lancement se fera via la commande uvicorn
