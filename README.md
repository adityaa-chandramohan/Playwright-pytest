This repository contains automated UI tests for a flight booking website using Playwright with Python.
Overview

Requirements

Python 3.8+
Playwright for Python
pytest
coverage.py

Installation

Clone the repository:
bashgit clone https://gitlab.com/your-username/Playwright-pytest.git
cd Playwright-pytest

Create and activate a virtual environment:
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
'pip install -r requirements.txt'

Install Playwright browsers:
'playwright install'

'pytest test_air_canada.py'

Run with visible browser (non-headless)

'pytest --headed'

Test Coverage

We use coverage.py to track and report code coverage metrics for our test suite.
Generating Coverage Reports

Run tests with coverage:
'coverage run -m pytest'

Generate a console report:
'coverage report'

Generate an HTML report:
'coverage html'
The HTML report will be available in the htmlcov directory.

Coverage Configuration
Coverage settings are configured in the .coveragerc file:
ini[run]
source = src
omit = 
    */venv/*
    */tests/*
    setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise NotImplementedError
CI/CD Integration
This project is configured to run in GitLab CI/CD pipelines. The configuration can be found in the .gitlab-ci.yml file.
Local Pipeline Simulation
To simulate the GitLab CI pipeline locally:

Install GitLab Runner:
bash# Linux
sudo curl -L --output /usr/local/bin/gitlab-runner "https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64"
sudo chmod +x /usr/local/bin/gitlab-runner

 macOS
brew install gitlab-runner

Run the pipeline job locally:
bashgitlab-runner exec docker test


Project Structure
├── .coveragerc             # Coverage configuration
├── .gitlab-ci.yml          # CI/CD configuration
├── requirements.txt        # Python dependencies
├── conftest.py             # Pytest fixtures
├── tests/
│   ├── test_air_canada.py  # Main test file
│   └── ...                 # Other test files
└── README.md               # This file
Best Practices

- Keep tests atomic and independent
- Use descriptive test names
- Maintain fixtures for common setup/teardown
- Run tests regularly on different browsers
- Monitor code coverage and aim for >80% coverage

Troubleshooting

Browser not opening: Make sure to use the --headed flag when running pytest
Element not found: Check if selectors need to be updated due to website changes
Timeouts: Consider increasing timeouts with page.set_default_timeout(30000)
CI failures: Ensure CI environment has all dependencies and browser binaries
