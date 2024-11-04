from urllib.parse import urlencode
import requests
import json
import time


from datetime import datetime, timedelta, date



def get_booking_businesses_based_on_token(microsoft_access_token, query):
    ms_booking_business_api = "https://graph.microsoft.com/v1.0/solutions/bookingBusinesses"

    headers = {
        'Authorization': f'Bearer {microsoft_access_token}',
        'Content-Type': 'application/json'
    }

    ms_business_final_url = ms_booking_business_api + "?query=" + query
    # Make a GET request to retrieve meeting types
    response = requests.get(url=ms_business_final_url, headers=headers)

    return response


if __name__ == "__main__":
    query = "booking page name" #enter the booking page name you want to use
    microsoft_access_token = "token data" #input access token data obtained in step 2
    response_json = get_booking_businesses_based_on_token(microsoft_access_token, query)
    print("response_json is")
    print(json.dumps(response_json,indent=4))
