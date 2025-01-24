# swisshydrodata

swisshydrodata is a library that allow you to get data from the
[Swiss Federal Office for the Environment FOEN](https://www.hydrodaten.admin.ch/en/).
To find a station near to you, use the
[list of stations](https://www.hydrodaten.admin.ch/en/messstationen-vorhersage)
on the FEON website.

The library uses a REST API which hands out the data because the FEON
does not allow to use their data service as backend.

The data update interval is limited to onece every 10 minutes by FEON,
so thats how often the API has new data available.

## Example

```python
import aiohttp
import asyncio
from swisshydrodata import SwissHydroData


async def main():
    async with aiohttp.ClientSession() as session:
        shd = SwissHydroData(session)
        # returns a list of station numbers
        data = await shd.async_get_stations()
        print(data)

        # returns all data available for station #2143
        data = await shd.async_get_station(2143)
        print(data)

asyncio.run(main())
```
