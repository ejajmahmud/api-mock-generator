"""Lightweight in-memory stateful API mock."""
from typing import Dict, Any, Tuple, List

class MockAPIEngine:
    def __init__(self):
        self.routes: Dict[str, Dict[str, Any]] = {}
        self.call_history: List[Dict[str, Any]] = []

    def register_route(self, path: str, method: str, response_payload: Any, status_code: int = 200) -> None:
        key = f"{method.upper()}:{path}"
        self.routes[key] = {"payload": response_payload, "status": status_code}

    def dispatch(self, path: str, method: str = "GET") -> Tuple[int, Any]:
        key = f"{method.upper()}:{path}"
        if key in self.routes:
            return self.routes[key]["status"], self.routes[key]["payload"]
        return 404, {"error": "Endpoint not found"}
