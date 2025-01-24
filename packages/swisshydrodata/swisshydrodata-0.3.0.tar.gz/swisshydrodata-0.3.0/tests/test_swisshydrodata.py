import asyncio
from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest
from swisshydrodata import _BASE_URL, SwissHydroApiConnectionError, SwissHydroData


@pytest.mark.asyncio
async def test_async_get_stations_success():
    mock_data = [
        {
            "id": "2232",
            "name": "Adelboden",
            "water-body-name": "Allenbach",
            "water-body-type": "river",
        },
        {
            "id": "2629",
            "name": "Agno",
            "water-body-name": "Vedeggio",
            "water-body-type": "river",
        },
    ]

    mock_session = MagicMock()
    mock_response = AsyncMock()
    mock_response.json = AsyncMock(return_value=mock_data)
    mock_response.status = 200
    mock_session.get = AsyncMock(return_value=mock_response)

    hydro_data = SwissHydroData(session=mock_session)
    stations = await hydro_data.async_get_stations()

    mock_session.get.assert_called_once_with(
        f"{_BASE_URL}/stations", raise_for_status=True
    )
    assert stations == mock_data


@pytest.mark.asyncio
async def test_async_get_stations_timeout_error():
    mock_session = MagicMock()
    mock_session.get = AsyncMock(side_effect=asyncio.TimeoutError)

    hydro_data = SwissHydroData(session=mock_session)

    with pytest.raises(SwissHydroApiConnectionError):
        await hydro_data.async_get_stations()


@pytest.mark.asyncio
async def test_async_get_stations_client_error():
    mock_session = MagicMock()
    mock_session.get = AsyncMock(
        side_effect=aiohttp.ClientError("Client error occurred")
    )

    hydro_data = SwissHydroData(session=mock_session)

    with pytest.raises(SwissHydroApiConnectionError):
        await hydro_data.async_get_stations()


@pytest.mark.asyncio
async def test_async_get_station_success():
    mock_data = {
        "name": "Rekingen",
        "water-body-name": "Rhein",
        "water-body-type": "river",
        "coordinates": {"latitude": 47.57034859100692, "longitude": 8.329828541142797},
        "parameters": {
            "discharge": {
                "unit": "m3/s",
                "datetime": "2021-04-12T06:50:00+01:00",
                "value": 335.749,
                "max-24h": 337.483,
                "mean-24h": 328.097,
                "min-24h": 313.777,
            },
            "level": {
                "unit": "°C",
                "datetime": "2021-04-12T06:50:00+01:00",
                "value": 8.79,
                "max-24h": 9.22,
                "mean-24h": 8.79,
                "min-24h": 8.26,
            },
        },
    }

    mock_session = MagicMock()
    mock_response = AsyncMock()
    mock_response.json = AsyncMock(return_value=mock_data)
    mock_response.status = 200
    mock_session.get = AsyncMock(return_value=mock_response)

    hydro_data = SwissHydroData(session=mock_session)
    stations = await hydro_data.async_get_station(2143)

    mock_session.get.assert_called_once_with(
        f"{_BASE_URL}/station/2143", raise_for_status=True
    )
    assert stations == mock_data


@pytest.mark.asyncio
async def test_async_get_station_timeout_error():
    mock_session = MagicMock()
    mock_session.get = AsyncMock(side_effect=asyncio.TimeoutError)

    hydro_data = SwissHydroData(session=mock_session)

    with pytest.raises(SwissHydroApiConnectionError):
        await hydro_data.async_get_station(2143)


@pytest.mark.asyncio
async def test_async_get_station_client_error():
    mock_session = MagicMock()
    mock_session.get = AsyncMock(
        side_effect=aiohttp.ClientError("Client error occurred")
    )

    hydro_data = SwissHydroData(session=mock_session)

    with pytest.raises(SwissHydroApiConnectionError):
        await hydro_data.async_get_station(2413)
