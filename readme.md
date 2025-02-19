# Douglas.de Automation

## Overview
This project automates the Douglas.de website to fetch product counts based on different filters. It primarily focuses on three test cases:
- Sale
- Neu (New)
- Limited

Additional filters such as product type, brand, target audience (for whom), and gift options can be applied dynamically. The extracted product count is then saved in an Excel file with a timestamped filename under the `data` folder.

## Project Structure
```
├── config
│   ├── settings.py  # Contains BASEURL and timeout configurations
├── data             # Stores extracted product data in Excel format
├── logs             # Stores logs, organized by date-time subfolders
├── reports          # Contains Allure reports
├── test             # Contains and configures test cases
├── utils            # Helper scripts (helper.py, browser_setup.py)
├── base.py          # Base class and methods including error handling
├── constants.py     # Contains all constant values such as XPaths and JS scripts
├── scrapy.py        # Main automation logic
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
```
## Prerequisites
1. Python dependencies
```
python 3.10.5
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
```

### 3. Activate the Virtual Environment
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Run Tests
```sh
pytest tests --alluredir=./reports -s
```

### 6. View Allure Reports
To view the Allure report, run:
```sh
allure serve reports
```

## Logging & Reports
- Logs are stored in the `logs` directory with timestamped subfolders.
- Test execution results are stored in the `reports` directory.
- Allure reports provide detailed test execution insights.

## Key Features
- Automates Douglas.de product search with filters.
- Extracts and saves product count dynamically.
- Supports logging and structured reporting.
- Uses Selenium for browser automation.
- Generates test execution reports using Allure.
