# ede13c1ff1a483440e6fb44807b76b86
import requests as rq
import pandas as pd

api_key = "?apikey=ede13c1ff1a483440e6fb44807b76b86"
api = "http://financialmodelingprep.com"


def sectors():
    response = rq.get(api+"/api/v3/sectors-performance"+api_key)
    df = pd.read_json(response.content)
    return df


def gainers():
    response = rq.get(api+"/api/v3/gainers"+api_key)
    df = pd.read_json(response.content)
    return df


def losers():
    response = rq.get(api+"/api/v3/losers"+api_key)
    df = pd.read_json(response.content)
    return df


def scanner():
    response = rq.get(api+"/api/v3/quotes/nyse"+api_key)
    df = pd.read_json(response.content)
    return df
