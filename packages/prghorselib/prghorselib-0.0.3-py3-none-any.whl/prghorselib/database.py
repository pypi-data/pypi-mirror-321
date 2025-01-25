from prghorselib.hash import create_hash
from prghorselib.random import generate_random_word, create_random
from secrets import token_urlsafe
from fastapi.responses import JSONResponse
from fastapi import HTTPException

async def get_next_id(collection) -> int:
    last_document = await collection.find_one(sort=[("_id", -1)])
    return (last_document.get("_id", 0) + 1) if last_document else 1

async def visit(request, database) -> None:
    client_ip = request.headers.get("X-Forwarded-For", request.client.host)
    await database["visits"].insert_one({
        "_id": await get_next_id(database["visits"]),
        "url": str(request.url),
        "method": request.method,
        "headers": dict(request.headers),
        "ip": client_ip,
    })

async def check_auth(request, database) -> bool:
    login = request.cookies.get('login')
    if not login:
        return False
    user = await database["users"].find_one({"login": login})
    if not user:
        return False
    tokens = user.get("tokens", {})
    for token_key, token_value in tokens.items():
        cookie_value = request.cookies.get(token_key)
        if cookie_value != token_value:
            return False
    return True

async def check_permissions(request, permission, database) -> bool:
    auth = await check_auth(request=request, database=database)
    if auth:
        token = request.cookies.get('token')
        user = await database["users"].find_one({"token": token})
        return user.get("permissions", {}).get(permission, False)
    return False

async def create_new_user(login, password, mail, db):
    if await db.find_one({"login": login}):
        raise HTTPException(status_code=400, detail="Пользователь с таким логином уже зарегистрирован.")

    if await db.find_one({"mail": mail}):
        raise HTTPException(status_code=400, detail="Пользователь с такой почтой уже зарегистрирован.")

    hashed_password = create_hash(text=password)
    tokens = {await generate_random_word(15): token_urlsafe(64) for _ in range(5)}

    await db.insert_one({
        "login": login,
        "mail": mail,
        "password": hashed_password,
        "tokens": tokens,
        "permissions": {
            "user": True,
            "administrator": False,
            "Developer": False
        }
    })
    
    response = JSONResponse({"status": True, "message": "Успешная регистрация."}, status_code=200)
    response.set_cookie("login", login)
    
    for key, value in tokens.items():
        response.set_cookie(key, value)
    
    response = await create_random(response=response)
    return response
