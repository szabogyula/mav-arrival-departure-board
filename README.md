# My Home Assistant Component

This is a custom component for Home Assistant. It provides a sensor and a service that can be used in your Home Assistant configuration.

## Installation

To install this component, follow these steps:

1. Copy the `custom_components/my_component` directory to your Home Assistant `custom_components` directory. If you don't have a `custom_components` directory, you can create one in the same directory as your `configuration.yaml` file.

2. Add the following to your `configuration.yaml` file:

To configure this component, you need to add the following to your `configuration.yaml` file in the `sensor` domain:

```yaml
sensor:
  - platform: mav
    name: Martonvásár Arrival Department Board
    state: 0
    station: 005503178 # Martonvasar
```

3. Restart Home Assistant.

## Usage

### Sensor

This component provides a sensor called `my_component`. The state of the sensor is updated every time Home Assistant starts or the sensor is manually updated.

You can display the sensor in your Home Assistant frontend by adding the following to your `ui-lovelace.yaml` file:

```yaml
entities:
  - entity: sensor.my_component
```

### Service

This component provides a service called `my_component.update`. You can call this service to manually update the sensor.

Here is an example of how to call the service in an automation:

```yaml
automation:
  - alias: Update My Component
    trigger:
      platform: time
      at: '00:00:00'
    action:
      service: my_component.update
```

## Support

If you have any issues with this component, please open an issue on GitHub.