# Task 2: API Key Generation and Authentication

## Introduction
This project demonstrates API key generation and authentication using Flask. It creates unique API keys for three different consumers and allows them to access a protected API endpoint.

## Features
- Generates unique API keys for three consumers.
- Provides an endpoint to view the generated keys.
- Uses API keys for authentication.
- Rejects requests with invalid or missing API keys.
- Accepts text through a POST request.
- Converts the submitted text into uppercase.
- Validates the input before processing.

## Technologies Used
- Python
- Flask
- REST API
- JSON
- PowerShell for testing

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the API is running |
| GET | `/keys` | Displays API keys for consumers |
| POST | `/process` | Authenticates the consumer and processes text |

## How to Run the Project

1. Open the Task_2 folder in the terminal.
2. Install Flask:

   `py -m pip install flask`

3. Run the application:

   `py app.py`

4. Open the following address in your browser:

   `http://127.0.0.1:5001/keys`

5. Use a consumer's API key in the `x-api-key` request header when accessing the `/process` endpoint.

## Testing
The API was tested with:
- Three valid consumer API keys.
- Invalid API key.
- Missing API key.
- Empty text input.
- Successful text processing.

## Expected Output
The API returns the original text and its uppercase version after successful authentication.

## Conclusion
This project demonstrates how API keys can be generated and used to authenticate multiple consumers accessing a protected Flask API.