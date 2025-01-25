import string
import random
from secrets import token_urlsafe

async def generate_random_word(length: int) -> str:
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

async def create_random(response, count: int = 20):
    for _ in range(count):
        key = await generate_random_word(length=15)
        value = token_urlsafe(64)
        response.set_cookie(key=key, value=value)
    return response
