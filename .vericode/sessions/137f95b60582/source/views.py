from rest_framework.response import Response
import structlog
logger = structlog.get_logger(__name__)

def _error_response(code: str, message: str, resource_id: str = "", status: int = 400) -> Response:
    logger.warning("stripe_app.error_response", code=code, message=message, resource_id=resource_id, status=status)
    return Response({"status": "error", "id": resource_id, "error": {"code": code, "message": message}}, status=status)
