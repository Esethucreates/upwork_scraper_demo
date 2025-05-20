import json

import nodriver as uc
from nodriver.cdp.network import Cookie

base_url: str = "https://www.upwork.com/nx/search/jobs/"


async def main():
    browser = await uc.start()
    tab = await browser.get(url=base_url)
    await tab.wait(10)

    # Handle the cookie nag as well. Basically that allow cookies thing
    print("Handling cookies...")
    cookies_bar_accept = await tab.find(text="accept all", best_match=True)
    if cookies_bar_accept:
        await cookies_bar_accept.click()

    print("Window is waiting...")
    await browser.wait(10)

    print("Page is scrolling...")
    await tab.scroll_down(30)

    print("Saving cookies...")
    cookies_list = await browser.cookies.get_all(requests_cookie_format=False)

    file_path = "./cookies/cookies.json"
    with open(file_path, "w+") as f:
        json.dump([Cookie.to_json(cookie) for cookie in cookies_list],
                  f,
                  indent=4)

    print("Stopping browser...")
    await tab.close()


if __name__ == '__main__':
    uc.loop().run_until_complete(main())
