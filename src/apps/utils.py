import aiohttp


async def get():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            await resp.content.read(n=100000)
            print(resp.status)

            print(await resp.text())
