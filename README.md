# FastAPI Project

## Overview

This project is a FastAPI-based backend that follows the DAO (Data Access Object) pattern to interact with the database efficiently. The project is structured to separate concerns between database operations, business logic, and API routes, making it scalable and maintainable.

## Project Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- FastAPI
- SQLModel
- Pytest & Pytest-Asyncio (for testing)
- K6 (for load testing)

### Installation

Clone the repository and install dependencies:

```bash
# Clone the repository
git clone https://github.com/peterlogo/blockchain-backend-api.git
cd fastapi-project

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Running the Server

Start the FastAPI server with fastapi-cli:

```bash
fastapi dev src/main.py
```

The API will be available at `http://127.0.0.1:8000`.

## DAO (Data Access Object) Setup

### Why Use DAO?
DAO is used to abstract and encapsulate database interactions, making it easier to:
- Manage database operations separately from business logic
- Improve testability by mocking database operations
- Follow clean architecture principles

### DAO Pattern Diagram

Below is a high-level representation of the DAO pattern:

```
+--------------------+
|      API Layer    |
| (FastAPI Routes)  |
+--------------------+
          |
          v
+--------------------+
|  Service Layer    |
| (Business Logic)  |
+--------------------+
          |
          v
+--------------------+
|  DAO Layer        |
| (Database Access) |
+--------------------+
          |
          v
+--------------------+
|  Database         |
+--------------------+
```

## Routes and Endpoints

### Available API Endpoints

| Method | Endpoint             | Description                      |
|--------|----------------------|----------------------------------|
| GET    | `/transactions`      | Fetch all transactions          |
| GET    | `/transactions/{tx_hash}` | Fetch transaction by hash |

### Example Requests
#### Get All Transactions
```bash
curl -X GET http://127.0.0.1:8000/transactions
```
##### Sample Response
```json
[
  {
    "id": 1,
    "from_address": "address1",
    "to_address": "address2",
    "amount": 100,
    "timestamp": "2025-02-27T18:47:16.964967Z",
    "tx_hash": "0x1e8a2a258283c7"
  },
  {
    "id": 2,
    "from_address": "address3",
    "to_address": "address4",
    "amount": 200,
    "timestamp": "2025-02-27T18:47:16.964967Z",
    "tx_hash": "0x2e8a2a258283c7"
  }
]
```

#### Get Transaction by Hash

```bash
curl -X GET http://127.0.0.1:8000/transactions/0xb4563fa94ba33
```

##### Sample Response

```json
{
  "id": 1,
  "from_address": "address1",
  "to_address": "address2",
  "amount": 100,
  "timestamp": "2025-02-27T18:47:16.964967Z",
  "tx_hash": "0x1e8a2a258283c7"
}
```

## Testing

### Unit Tests

We use `pytest` to test DAO, Service, and API layers.
Run the tests with:

```bash
pytest
```

### Load Testing with k6

We used k6 to test the `/transactions` endpoint under load.

#### Running Load Test

```bash
k6 run load_test.js
```

#### Sample Load Test Results

```
http_req_duration (p95) exceeded threshold: 59.99s
http_req_failed exceeded threshold: 10.97%
```

For detailed load test results, refer to [LOAD_TEST_REPORT.md](LOAD_TEST_REPORT.md).

### Optimization Suggestions

- Optimize database queries to reduce response time.
- Implement caching mechanisms for frequently accessed transactions.
- Scale horizontally with load balancers and multiple instances.

## Conclusion

This project is structured for scalability and maintainability using FastAPI and SQLModel. The DAO pattern ensures a clean separation of concerns, and we have implemented rigorous testing to maintain performance and reliability.
