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


def get_logged_in_user_details(microsoft_access_token):

    import requests
    get_user_info_api = "https://graph.microsoft.com/oidc/userinfo"
    headers = {
        'Authorization': f'Bearer {microsoft_access_token}',
        'Content-Type': 'application/json'}
    response = requests.get(url=get_user_info_api, headers=headers)
    response_json = response.json()
    response_status_code = response.status_code
    if response.status_code != 200:
        print("api failed")

        return response_json

    print("successfully fetched logged in user's details")

    return response_json



if __name__ == "__main__":
    microsoft_access_token = "token data" #input access token data obtained in step 2
    response_json = get_logged_in_user_details(microsoft_access_token)
    print("response_json is")
    print(json.dumps(response_json,indent=4))