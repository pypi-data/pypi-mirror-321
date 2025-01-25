async def get_next_id(collection, self = None) -> int:
    last_document = await collection.find_one(sort=[("_id", -1)])
    return (last_document.get("_id", 0) + 1) if last_document else 1

async def visit(request, database, self = None) -> None:
    client_ip = request.headers.get("X-Forwarded-For", request.client.host)
    await database["visits"].insert_one({
        "_id": await get_next_id(database["visits"]),
        "url": str(request.url),
        "method": request.method,
        "headers": dict(request.headers),
        "ip": client_ip,
    })

async def check_auth(request, database, self = None) -> bool:
    login = request.cookies.get('login')
    if not login:
        return False
    user = await database["users"].find_one({"login": login})
    if not user:
        return False
    tokens = user.get("tokens", {})
    if not tokens:
        return False
    for token_key, token_value in tokens.items():
        cookie_value = request.cookies.get(token_key)
        if cookie_value != token_value:
            return False
    return True

async def check_permissions(request, permission, database, self = None) -> bool:
    auth = await check_auth(request=request, database=database)
    if auth:
        token = request.cookies.get('token')
        user = await database["users"].find_one({"token": token})
        try:
            permission_value = user["permissions"][permission]
            return permission_value
        except KeyError:
            return False
    else:
        return False
