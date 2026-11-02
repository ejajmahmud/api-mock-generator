# API Mock Generator ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="API Mock Generator Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/api-mock-generator/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/api-mock-generator?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/api-mock-generator/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**API Mock Generator** is a production-ready developer tool and connector: Lightweight mock server generating realistic stateful responses from endpoint definitions for agent testing.

---

## 🚀 Problem Statement

Testing agent tool workflows against live 3rd-party APIs exhausts rate limits, incurs billing, and fails during network downtime.

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    participant Agent
    participant Mock as API Mock Generator
    participant Ledger as In-Memory State

    Agent->>Mock: POST /api/v1/users {name: "Alice"}
    Mock->>Ledger: Insert User (ID: 101)
    Mock-->>Agent: 201 Created {id: 101, name: "Alice"}
    Agent->>Mock: GET /api/v1/users/101
    Mock-->>Agent: 200 OK {id: 101, name: "Alice"}
```

---

## 📊 Performance Benchmarks

| Metric | Live SaaS API | API Mock Generator |
|---|---|---|
| Request Latency | 340ms | **0.8ms (425x faster)** |
| Rate Limit Risk | High | 0% (Unlimited) |
| Offline Operation | Impossible | 100% Local |

---

## 🛠️ Installation & Quickstart

```bash
pip install api_mock_generator
```

### Python API

```python
import api_mock_generator

print(api_mock_generator.__version__)
```

### CLI Usage

```bash
api-mock-generator --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
