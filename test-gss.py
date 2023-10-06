import requests

# Replace with your actual API token
API_TOKEN = "api_live.a11aaaaAaA3.a_-000aaaAAAaaa00ddddddddaaaaaaa"
API_TOKEN_sandbox = "api_sandbox.a11aaaaAaA3.a_-000aaaAAAaaa00ddddddddaaaaaaa"

# Replace with the applicant ID you want to perform a check on
APPLICANT_ID = "APPLICANT_ID"

# Replace with the type of check you want to perform (e.g., 'standard' or 'express')
CHECK_TYPE = "CHECK_TYPE"

# Onfido API endpoint URL
BASE_URL = "https://api.onfido.com/v3/checks"

# Headers with the API token
headers = {
    "Authorization": f"Token {API_TOKEN}",
}

# Request payload
data = {
    "type": CHECK_TYPE,
    "applicant_id": APPLICANT_ID,
}

try:
    # Make a POST request to create a check
    response = requests.post(BASE_URL, json=data, headers=headers)

    if response.status_code == 201:
        print("Check created successfully!")
        print("Response:")
        print(response.json())
    else:
        print("Error creating check:")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
