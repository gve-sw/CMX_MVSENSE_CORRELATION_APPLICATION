# this config file contains multiple variables utilized throughout the functionality of this code

MERAKI_API_KEY = "<MERAKI_API_KEY>"
NETWORK_ID = "<MERAKI_NETWORK_ID"

# ------------Variables utilized in mvSense.py-----------------------------------
# MQTT_SERVER = "iot.eclipse.org"
MQTT_SERVER = "MQTT_IP_DOMAIN"
MQTT_PORT = 1883
MQTT_TOPIC = "/merakimv/#"

# Array of cameras serial numbers
COLLECT_CAMERAS_SERIAL_NUMBERS = ["*"]
# Array of zone id, all is *. eg ["*"]
COLLECT_ZONE_IDS = ["*"]

# motion trigger setting
MOTION_ALERT_PEOPLE_COUNT_THRESHOLD = 1
# message count to trigger an action
MOTION_ALERT_ITERATE_COUNT = 50
# least number of people to send action
MOTION_ALERT_TRIGGER_PEOPLE_COUNT = 1
# pause time after alert finished triggering
MOTION_ALERT_PAUSE_TIME = 5
# number of messages until action time out
TIMEOUT = 20


# -------------Variabbles utilized in cmxreceiver.py------------------

validator = "<MERAKI_CMX_VALIDATOR_KEY>"
# rssi value needed to be registered as a "visitor" to be stored in database in cmxreceiver
_RSSI_THRESHOLD = 15

# Mac address of desired access point
_APMACADDR="<MERAKI_ACCESS_POINT_MAC_ADDRESS"


# --------Variables utilized in compute.py----------------------

# number of seconds to filter out in cmxFilterHours()
# will remove MAC addresses that have been seen for over this given amount of time
_FILTER_TIME = 3600

# number of seconds between timestamps in getCMXHours() which still constitutes a session
# if a device is not seen for longer that this time threshold, the "session" will end
# and this will be logged as a visit.
# if the same device is seen again outside of this threshold, it will start a new visit session
_SESSION_TIME = 300

# utilized in correlation()
# defines a leeway period before inTime and after outTime of mvSense data in which cmx data should still be considered, as the times may not exactly match up due to granularity differences
timeWindow = 30

# utilized in correlation()
# defines threshold of signal strength that will be considered
# the closer the device, the larger the rssiThreshold
# tesing shows 45 and above is about 1 meter away from access point
rssiThreshold = 45
