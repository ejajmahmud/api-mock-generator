"""Command line interface for api-mock-generator."""
from .generator import MockAPIEngine

def main():
    mock = MockAPIEngine()
    mock.register_route("/status", "GET", {"healthy": True})
    code, data = mock.dispatch("/status")
    print(f"Mock Response [{code}]:", data)

if __name__ == "__main__":
    main()
