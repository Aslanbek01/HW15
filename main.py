import aiohttp
import asyncio
import aiofiles
import os

folders = [f'folder_{i}' for i in range(10)]

async def create_folder(folder):
    os.makedirs(folder, exist_ok=True)

async def download_image(session, url, folder):
    async with session.get(url) as response:
        if response.status == 200:
            async with aiofiles.open(os.path.join(folder, 'image.png'), mode='wb') as f:
                await f.write(await response.read())

async def main():

    await asyncio.gather(*(create_folder(folder) for folder in folders))

    image_urls = [

        'http://example.com/image1.jpg',
        'http://example.com/image2.jpg',

        'http://example.com/image10.jpg'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, image_urls[i], folders[i]) for i in range(len(image_urls))]
        await asyncio.gather(*tasks)

asyncio.run(main())