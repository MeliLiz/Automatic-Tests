# Automatic Tests

This repository contains automated tests for web pages using Selenium and Behave in Python.

## Description

This project utilizes Selenium for browser automation and Behave for behavior-driven development (BDD) to implement automated tests for web applications. It aims to ensure the reliability and functionality of web pages through comprehensive automated testing.

## Tools and Technologies

- **Python**: The programming language used for writing scripts and tests.
- **Selenium**: A tool for automating web browsers.
- **Behave**: A BDD framework for Python, which allows writing tests in a natural language style.

## Structure

- `features/`: Contains feature files and step definitions.
- `tests/`: Contains unit tests.
- `pages/`: Contains page object models.
- `requirements.txt`: Lists Python dependencies.

## Usage

1. **Set Up**: Install the necessary dependencies.

    ```sh
    pip install -r requirements.txt
    ```

2. **Run Behave Tests**: Execute the tests defined in the feature files.

    ```sh
    behave
    ```

3. **Run Unit Tests**: Execute the unit tests.

    ```sh
    pytest
    ```

## Future Plans

- Add more complex test scenarios.
- Explore other testing frameworks and tools.
- Improve test coverage and robustness.
