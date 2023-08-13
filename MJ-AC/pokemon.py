import aiohttp
import requests
import asyncio
import random



url = f'https://pokeapi.co/api/v2/pokemon/ditto'

async def call_pokemon():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return response.json()
            

async def main():
    response_content = await call_pokemon()
    print(response_content)

asyncio.run(main())

    

