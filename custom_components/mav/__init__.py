"""The MÁV component."""
import logging

from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

DOMAIN = "mav"

def async_setup(hass: HomeAssistant, config: dict):
    """Set up the my_component component."""
    _LOGGER.info("Setting up mav")
    return True
