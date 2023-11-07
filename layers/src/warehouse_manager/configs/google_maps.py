from os import getenv

GOOGLE_MAPS_API_KEY = getenv("GOOGLE_MAPS_API_KEY")
MAPS_DISTANCE_API_PREFIX = getenv("MAPS_DISTANCE_API_PREFIX", "https://routes.googleapis.com/distanceMatrix/v2:")
