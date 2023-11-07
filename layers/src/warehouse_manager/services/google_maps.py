from typing import Union

from requests import post
from requests.exceptions import HTTPError

from warehouse_manager.configs.google_maps import GOOGLE_MAPS_API_KEY, MAPS_DISTANCE_API_PREFIX
from warehouse_manager.models.database.customer import Customer
from warehouse_manager.models.database.warehouse import Warehouse


def get_location_distance(
    origin: Union[Customer, Warehouse], destination: Union[Customer, Warehouse]
) -> dict[str, str]:
    url = f"{MAPS_DISTANCE_API_PREFIX}computeRouteMatrix"
    query_params = {"key": GOOGLE_MAPS_API_KEY}
    headers = {"Content-Type": "application/json", "X-Goog-FieldMask": "*"}
    payload = {
        "origins": [
            {
                "waypoint": {
                    "via": False,
                    "vehicleStopover": False,
                    "sideOfRoad": False,
                    "location": {"latLng": {"latitude": origin.latitude, "longitude": origin.longitude}},
                }
            }
        ],
        "destinations": [
            {
                "waypoint": {
                    "via": False,
                    "vehicleStopover": False,
                    "sideOfRoad": False,
                    "location": {"latLng": {"latitude": destination.latitude, "longitude": destination.longitude}},
                }
            }
        ],
    }

    try:
        request = post(url, params=query_params, headers=headers, json=payload, timeout=20)
        request.raise_for_status()
    except HTTPError as error:
        # log error or do some business rule process when the API returns an HTTPError
        raise error

    response = request.json()

    result = {
        "distance": str(response[0]["localizedValues"]["distance"]["text"]),
        "duration": str(response[0]["localizedValues"]["duration"]["text"]),
    }

    return result
