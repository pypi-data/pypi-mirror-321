import asyncio
import logging

import aiohttp

_LOGGER = logging.getLogger(__name__)
_BASE_URL = "https://swisshydroapi.bouni.de/api/v1"


class SwissHydroApiError(Exception):
    """General SwissHydroApiError exception occurred."""

    pass


class SwissHydroApiConnectionError(SwissHydroApiError):
    """When a connection error is encountered."""

    pass


class SwissHydroData:
    """
    SwissHydroData enables you to fetch data from
    the Federal Office for the Environment FOEN
    """

    def __init__(self, session):
        self._session = session

    async def async_get_stations(self) -> list | None:
        """Return a list of all stations IDs"""
        try:
            response = await self._session.get(
                f"{_BASE_URL}/stations", raise_for_status=True
            )

            _LOGGER.debug("Response from sysisshydroapi.bouni.de: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
        except asyncio.TimeoutError as e:
            _LOGGER.error("Can not load data from sysisshydroapi.bouni.de")
            raise SwissHydroApiConnectionError() from e
        except aiohttp.ClientError as aiohttpClientError:
            _LOGGER.error(
                "Response from sysisshydroapi.bouni.de: %s", aiohttpClientError
            )
            raise SwissHydroApiConnectionError() from aiohttpClientError
        return data

    async def async_get_station(self, station_id: int | str):
        """Return all data for a given station"""
        try:
            response = await self._session.get(
                f"{_BASE_URL}/station/{station_id}", raise_for_status=True
            )

            _LOGGER.debug("Response from sysisshydroapi.bouni.de: %s", response.status)
            data = await response.json()
            _LOGGER.debug(data)
        except asyncio.TimeoutError as e:
            _LOGGER.error("Can not load data from sysisshydroapi.bouni.de")
            raise SwissHydroApiConnectionError() from e
        except aiohttp.ClientError as aiohttpClientError:
            _LOGGER.error(
                "Response from sysisshydroapi.bouni.de: %s", aiohttpClientError
            )
            raise SwissHydroApiConnectionError() from aiohttpClientError
        return data
