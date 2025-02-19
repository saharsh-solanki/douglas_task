# Define variables for common paths
VENV_DIR = venv
REPORTS_DIR = reports
LOGS_DIR = logs
DATA_DIR = data
TESTS_DIR = tests

# Python executable in virtual environment
PYTHON = $(VENV_DIR)/bin/python

# The command for activating the virtual environment
ACTIVATE = source $(VENV_DIR)/bin/activate

# Install dependencies
install: 
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV_DIR)
	@echo "Activating virtual environment..."
	$(ACTIVATE) && pip install -r requirements.txt
	@echo "Dependencies installed successfully."

# Run all tests with Allure reporting
run-tests:
	@echo "Running tests..."
	$(ACTIVATE) && pytest $(TESTS_DIR) --alluredir=$(REPORTS_DIR) -s
	@echo "Test execution completed."

# Serve Allure reports after test run
serve-reports:
	@echo "Serving Allure reports..."
	$(ACTIVATE) && allure serve $(REPORTS_DIR)
	@echo "Allure report server started."
