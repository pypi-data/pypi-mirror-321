# Performance Testing Framework

This repository contains a performance testing framework using Locust for API load testing, with a focus on testing the Lyric API endpoints.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- virtualenv (recommended)

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd lyric-probe-performance
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -e .
```

## Configuration

1. Create a `config.yaml` file in the root directory with your API credentials:
```yaml
# API Credentials
client_id: "your-client-id"
client_secret: "your-client-secret"
sequence_id: "your-sequence-id"
base_url: "https://your-api-base-url"

# Test Configuration
test_config:
  users: 1
  spawn_rate: 1

# Action Configuration
actions:
  - name: "YourAction"
    type: "Application"
    parameters: []
```

## Project Structure

```
lyric-probe-performance/
├── src/
│   ├── controllers/
│   │   ├── external_actions.py
│   │   ├── external_apps.py
│   │   ├── external_scenarios.py
│   │   ├── external_tables.py
│   │   └── external_token.py
│   ├── utils/
│   │   ├── authManager.py
│   │   ├── configLoader.py
│   │   ├── downloadManager.py
│   │   ├── logger.py
│   │   └── setUp.py
│   ├── main.py
│   └── routes.py
├── tests/
├── logs/
├── reports/
│   ├── csv/
│   └── html/
├── downloads/
├── setup.py
└── config.yaml
```

## Running Tests

1. Basic test execution:
```bash
python -m runner
```

2. Running with specific parameters:
```bash
python -m runner --users 10 --spawn-rate 2
```

## Test Reports

The framework generates several types of reports:

- HTML reports: Located in `reports/html/`
- CSV statistics: Located in `reports/csv/`
- Log files: Located in `logs/`

## Report Structure

### HTML Reports
The HTML reports provide a comprehensive view of the test execution including:
- Request statistics
- Response time graphs
- Error rates
- Distribution graphs

### CSV Reports
CSV reports contain detailed metrics including:
- Request counts
- Response times
- Error rates
- Custom metrics

## Logging

Logs are automatically generated in the `logs/` directory with the following format:
- Filename: `YYYYMMDD_HHMMSS.log`
- Log levels: DEBUG, INFO, WARNING, ERROR
- Contains detailed information about test execution, API calls, and errors

## Error Handling

The framework includes comprehensive error handling for:
- API authentication failures
- Network connectivity issues
- Invalid configurations
- File download/upload issues

## Development

### Adding New Tests

1. Create a new task class in `tasks/`:
```python
from locust import task
from tasks.base_task import BaseTask

class YourNewTask(BaseTask):
    @task
    def your_test_case(self):
        # Your test logic here
        pass
```

2. Register the task in `main.py`:
```python
class PerformanceUser(HttpUser):
    tasks = [YourNewTask]
```

## Troubleshooting

Common issues and solutions:

1. Authentication Errors
   - Verify your credentials in config.yaml
   - Check API endpoint accessibility
   - Verify network connectivity

2. File Download Issues
   - Check disk space
   - Verify write permissions
   - Ensure valid file paths

3. Performance Issues
   - Monitor system resources
   - Check network bandwidth
   - Verify test parameters
