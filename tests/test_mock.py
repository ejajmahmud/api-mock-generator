"""Unit tests for api_mock_generator."""
import unittest
from api_mock_generator.generator import MockAPIEngine

class TestMock(unittest.TestCase):
    def test_mock_dispatch(self):
        m = MockAPIEngine()
        m.register_route("/users", "GET", [{"id": 1}])
        code, resp = m.dispatch("/users")
        self.assertEqual(code, 200)
        self.assertEqual(resp, [{"id": 1}])
        c404, _ = m.dispatch("/unknown")
        self.assertEqual(c404, 404)

if __name__ == "__main__":
    unittest.main()
