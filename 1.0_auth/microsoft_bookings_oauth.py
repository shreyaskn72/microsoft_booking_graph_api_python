from urllib.parse import urlencode
import requests
import json
import time


from datetime import datetime, timedelta, date

# Set your Microsoft Bookings OAuth client credentials
MSBOOKING_CLIENT_ID = "enter client id of msbooking here"
MSBOOKING_CLIENT_SECRET = "Enter client secret of ms booking here"

# Set the redirect URL for your application
MSBOOKING_REDIRECT_URI = "enter the redirect url u have given"

#Enter the ms booking tenant id here"
MSBOOKING_TENANT_ID = "common"


def fetch_authorization_url():
    TENANT_ID = MSBOOKING_TENANT_ID

    # Set the OAuth endpoints specific to Microsoft Bookings
    AUTH_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize'
    SCOPE = 'offline_access BookingsAppointment.ReadWrite.All Bookings.ReadWrite.All Calendars.ReadWrite Bookings.Manage.All'

    # Step 1: Get Authorization Code
    auth_params = {
        'client_id': MSBOOKING_CLIENT_ID,
        'redirect_uri': MSBOOKING_REDIRECT_URI,
        'response_type': 'code',
        'scope': SCOPE
    }

    # Construct the authorization URL
    auth_url = AUTH_URL + '?' + urlencode(auth_params)

    # Print the authorization URL for the user to visit and authorize the application
    print("authorization url is")
    print(auth_url)

    return auth_url



def exchange_token_with_code():
    TENANT_ID = MSBOOKING_TENANT_ID
    # After the user authorizes the application, they will be redirected back to the redirect URL
    # Extract the authorization code from the redirected URL
    redirect_response = input("Paste the full URL you were redirected to: ")
    code = redirect_response.split('code=')[1]

    TOKEN_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

    # Step 2: Exchange Authorization Code for Access Token
    token_data = {
        'client_id': MSBOOKING_CLIENT_ID,
        'client_secret': MSBOOKING_CLIENT_SECRET,
        'code': code,
        'redirect_uri': MSBOOKING_REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    # Step 3: Make a POST request to the token endpoint to exchange authorization code for tokens
    token_response = requests.post(TOKEN_URL, data=token_data)
    token_json = token_response.json()
    token_status_code = token_response.status_code

    # Check if the request was successful
    if token_status_code != 200:
        print("Failed to retrieve access token:", token_response.text)

        response_error = {"success": False, "error_response": token_json}

        print(response_error)
        return response_error

    print("Token Response:", json.dumps(token_json, indent=4))

    if "access_token" in token_json:
        today = datetime.now()
        unix_timestamp_now = time.mktime(today.timetuple())
        d = datetime.fromtimestamp(unix_timestamp_now + token_json["expires_in"])
        #
        ms_data = {
            "microsoft_access_token": token_json["access_token"],
            "microsoft_refresh_token": token_json["refresh_token"],
            "microsoft_expires_in": d
        }

        with open('ms_data.json', 'w') as json_file:
            # Step 4: Write the dictionary to the file
            json.dump(ms_data, json_file, indent=4)  # indent for pretty printing

    return token_json

if __name__ == "__main__":
    auth_url = fetch_authorization_url()
    token_json = exchange_token_with_code()