import requests
import json
from getpass import getpass

creds = {}

with open("config.json", "r") as f:
    creds = json.loads(f.read())
creds["password"] = getpass()


def getToken():
    r = requests.post(
        "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token", data=creds)
    tokens = json.loads(r)
    creds["access_token"] = tokens["access_token"]
    creds["refresh_token"] = tokens["refresh_token"]


def refreshToken():
    r = requests.post(
        "https://auth.mangadex.org/realms/mangadex/protocol/openid-connect/token/auth/refresh", data=creds)
    tokens = json.loads(r)
    creds["access_token"] = tokens["access_token"]
    creds["refresh_token"] = tokens["refresh_token"]
