# xapi - Unofficial X API client

<div align="center">

[<img src="https://badgen.net/pypi/v/xtwitterapi" alt="version" />](https://pypi.org/project/xtwitterapi)
[<img src="https://badgen.net/pypi/python/xtwitterapi" alt="py versions" />](https://pypi.org/project/xtwitterapi)
[<img src="https://badgen.net/pypi/dm/xtwitterapi" alt="downloads" />](https://pypi.org/project/xtwitterapi)
[<img src="https://badgen.net/github/license/tadasgedgaudas/xapi" alt="license" />](https://github.com/tadasgedgaudas/xapi/blob/main/LICENSE)

</div>

X frontend app reverse engineered and implemented in Python.

ONLY FOR EDUCATIONAL PURPOSES. This repository has no response to any issues for your account

## Install

```bash
pip install xtwitterapi
```

## Features
- Follow, Like, Search, DM, Notifications and more. See `modules` directory for more details.

## Usage

```python

from xapi import X


async def main():

    USERNAME = "your_username"
    PASSWORD = "your_password"

    x = await X.create(username=USERNAME, password=PASSWORD)
    follow_response = await x.follow(username="elonmusk")
    print(follow_response)

    search_response = await x.search(query="elonmusk")
    print(search_response)

    like_response = await x.like(tweet_id="1234567890")
    print(like_response)

    dm_response = await x.send_dm(username="elonmusk", message="Hello from xapi!")
    print(dm_response)

if __name__ == "__main__":
    asyncio.run(main())
```

See more examples in `tests` directory. There will be an example for each available module.

