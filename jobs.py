import requests
from config import API_URL

def get_jobs():
    try:
        res = requests.get(API_URL)
        data = res.json()
        return data.get("jobs", [])[:5]
    except Exception as e:
        print("Error:", e)
        return []