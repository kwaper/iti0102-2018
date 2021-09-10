"""Retrieve stops and departures info from REST service."""
import requests
API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    a = requests.get(api_base + f"/stops/{lat}/{lng}").json()
    return sorted([i for i in a], key=lambda i: int(i["distance"][:-2]))


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    a = requests.get(api_base + f"/stops/{lat}/{lng}").json()
    if len(a) > 0:
        return min([i for i in a], key=lambda i: int(i["distance"][:-2]))
    else:
        return None


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    a = requests.get(api_base + f"/departures/{region}/{stop_id}").json()
    return a["departures"]


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    a = requests.get(api_base + f"/departures/{region}/{stop_id}").json()
    if len(a["departures"]) > 0:
        return min(a["departures"], key=lambda x: x["timeLocal"])
    else:
        return None
