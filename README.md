# Multical 21

Multical 21 custom component for Home Assistant.
![image](https://user-images.githubusercontent.com/6593720/220913633-3daa874f-3ed3-4e39-b827-ec7a1ce1f6dd.png)

**Languages:** English | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Italiano](README.it.md) | [Polski](README.pl.md) | [Dansk](README.da.md) | [Svenska](README.sv.md) | [Nederlands](README.nl.md)

## Requirements

To use this custom component, you'll need an optical eye and connect your machine running Home Assistant directly with the optical eye to the Kamstrup Multical 21 meter.
The integration works with any generic USB-to-serial optical read head — it isn't tied to a specific brand or USB chipset.
The optical eye looks like this:<br>
![image](https://user-images.githubusercontent.com/6593720/220914030-3ca8bec3-b302-4ed7-a0b8-c4858b0c8120.png)
I ordered it from [here](https://www.aliexpress.com/item/1005004567409202.html?spm=a2g0o.order_list.order_list_main.18.43e81802zaII7n)
You can also 3d print [this mount](https://makerworld.com/en/models/490708#profileId-404169)

## Installation

### HACS

This component can be installed directly via HACS. Search for "Multical 21" in the HACS integration list and click "Download".

### Manual

1. Open the directory for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory, create it.
3. Download the `custom_components/multical_21/` directory from this repository as a ZIP and extract it, or clone the repository.
4. Copy the `multical_21` folder into your `custom_components` directory.
5. Restart Home Assistant.
6. In the HA UI go to "Settings" → "Devices & Services", click "Add Integration" and search for "Multical 21".

## Configuration is done in the UI

When adding the integration you'll be asked for:

- **Serial port** — pick your read head from the list of detected serial devices, or type a path manually. The picker prefers stable identifiers automatically; if you do enter a path by hand, prefer `/dev/serial/by-id/...` over `/dev/ttyUSB1`, since the former doesn't change when USB devices are added/removed or the system reboots. A `/dev/serial/by-id` path looks like this: `/dev/serial/by-id/usb-FTDI_FT230X_Basic_UART_D307PBVY-if00-port0`.
- **Name** — an optional friendly name, useful if you're reading more than one meter.

### Multiple meters

You can add the integration more than once — for example, if you read both a cold and a hot water meter. Just repeat the "Add Integration" step for each additional read head.

### Changing the serial port later

If you swap the USB adapter, or its device path changes, you don't need to delete and re-add the integration. Open the integration's entry, choose **Reconfigure**, and select the new port. Your entities, history and automations stay intact.

### Options

Press "Configure" on the Integrations page to adjust:

- **Scan interval** (seconds, default `60`) — some meters contain a battery, and communicating with the meter impacts battery life. Increase this if you want to poll less often.
- **Serial read timeout** (seconds, default `1.0`) — if you get the error `Finished update, No readings from the meter. Please check the IR connection`, try increasing this value. Fractional numbers are allowed (e.g. `0.5`).
- **Baud rate** (default `1200`) — this is the Multical 21's protocol default and normally doesn't need to change. Only adjust it if your specific USB adapter requires a different rate.

## Collect logs

When you want to report an issue, please add logs from this component. You can enable logging for this component by configuring the logger in Home Assistant as follows:
```yaml
logger:
  default: warn
  logs:
    custom_components.multical_21: debug
```
More info can be found on the [Home Assistant logger integration page](https://www.home-assistant.io/integrations/logger)
