from decouple import config

# TODO: Defaults should be production
HOST_URL = config("HOMELINK_HOST_URL", default="homelinkcloud.com")
DISCOVER_URL = config(
    "HOMELINK_DISCOVER_URL",
    default=f"https://{HOST_URL}/services/v2/home-assistant/fulfillment",
)
ENABLE_URL = config(
    "HOMELINK_ENABLE_URL",
    default=f"https://{HOST_URL}/services/v2/home-assistant/fulfillment",
)
STATE_URL = config(
    "HOMELINK_STATE_URL", default=f"https://state.{HOST_URL}/services/v2/home-assistant"
)

COGNITO_POOL_ID = config("COGNITO_POOL_ID", default="us-east-2_sBYr2OD1J")
COGNITO_CLIENT_ID = config("COGNITO_CLIENT_ID", default="701cln3h6bgqfldh61rcf21ko0")
