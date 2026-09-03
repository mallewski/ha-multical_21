"""Constants for multical 21."""

from typing import Final

# Base component constants
NAME: Final = "multical 21"
DOMAIN: Final = "multical_21"
VERSION: Final = "2.2.5"
MODEL: Final = "Multical 21"
MANUFACTURER: Final = "Kamstrup"
ATTRIBUTION: Final = "Data provided by multical 21 meter"

# Config keys not covered by homeassistant.const
CONF_BAUDRATE: Final = "baudrate"

# Defaults
DEFAULT_NAME: Final = NAME
DEFAULT_BAUDRATE: Final = 1200
DEFAULT_SCAN_INTERVAL: Final = 60
DEFAULT_TIMEOUT: Final = 1.0

# Baud rates the Kamstrup optical IR head can be configured to use.
# 1200 is the factory/protocol default for the Multical 21 IR eye,
# but some third-party USB adapters allow/require a different rate.
SUPPORTED_BAUDRATES: Final = [300, 1200, 2400, 4800, 9600, 19200]

# Sentinel value used in the config flow port-picker to let the user
# type a path manually instead of choosing an auto-detected device.
CONF_MANUAL_PATH: Final = "manual"

# Platforms
SENSOR: Final = "sensor"
PLATFORMS: Final = [SENSOR]
