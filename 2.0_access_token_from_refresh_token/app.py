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


def microsoft_get_access_token_from_refresh_token(token_file):
    today = datetime.now()

    with open(token_file, 'r') as json_token_file:
        #Load the JSON data into a dictionary
        token_dict = json.load(json_token_file)

    if token_dict["microsoft_expires_in"] and token_dict["microsoft_expires_in"] <= today:
        TENANT_ID = MSBOOKING_TENANT_ID
        TOKEN_URL = f'https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token'

        SCOPE = 'https://graph.microsoft.com/.default offline_access'  # Scope for Microsoft Graph API with offline_access

        # Step 1: Exchange Refresh Token for New Access Token
        token_data = {
            'client_id': MSBOOKING_CLIENT_ID,
            'client_secret': MSBOOKING_CLIENT_SECRET,
            'refresh_token': token_dict["microsoft_refresh_token"],
            'grant_type': 'refresh_token',
            'scope': SCOPE
        }

        token_response = requests.post(TOKEN_URL, data=token_data)
        token_json = token_response.json()

        if token_response.status_code == 200:
            if "access_token" in token_json:
                today = datetime.now()
                unix_timestamp_now = time.mktime(today.timetuple())
                d = datetime.fromtimestamp(unix_timestamp_now + token_json["expires_in"])


                ms_data = {
                    "microsoft_access_token": token_json["access_token"],
                    "microsoft_refresh_token": token_json["refresh_token"],
                    "microsoft_expires_in": d
                }

                with open(token_file, 'w') as json_file:
                    # Step 4: Write the dictionary to the file
                    json.dump(ms_data, json_file, indent=4)  # indent for pretty printing

                return token_json

    with open(token_file, 'r') as final_tokens:
        #Load the JSON data into a dictionary
        final_tokens_data = json.load(final_tokens)

    return final_tokens_data

if __name__ == "__main__":
    token_file = 'ms_data.json'
    final_tokens_data = microsoft_get_access_token_from_refresh_token(token_file)