from aiohttp import ClientSession as Session
from colorgram_rs import get_dominant_color
from asyncio import run
from PIL import Image
from io import BytesIO
from tools import timeit
async def r():
    url = "https://cdn.discordapp.com/embed/avatars/0.png"
#    url = "https://cdn.discordapp.com/avatars/1109861649910874274/946588e6d2e8ea2d46ec6e89eb466321.png?size=1024"
    async with Session() as session:
        async with session.get(url) as req:
            d = await req.read()
    async with timeit() as timer:
        dom = get_dominant_color(url, True)
    async with timeit() as timer2:
        ddom = get_dominant_color(d)
    print(f"ddom: {dir(dom)}")
    print(f"finished in {timer.elapsed} seconds")
    bttes = dom.bytes
    print(type(bttes))
    with open("imae.png", "wb") as d: d.write(bttes)
    i = Image.open(BytesIO(bttes))
    print(f"{ddom} {dom} {i}")
    return dom

run(r())
