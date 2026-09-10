from fastapi.openapi.utils import get_openapi

def custom_openapi_schema(app):
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="AgentForge Core API",
        version="0.4.0",
        description="Autonomous Multi-Agent Workflow Execution Engine API Documentation",
        routes=app.routes,
    )
    openapi_schema["info"]["x-vendor-name"] = "AgentForge Technologies"
    app.openapi_schema = openapi_schema
    return app.openapi_schema