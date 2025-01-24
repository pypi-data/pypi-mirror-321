from functools import wraps
from typing import List
import asyncio
from fastapi import HTTPException, Request
from .auth import KeycloakAuth
from .config import keycloak_config
from functools import wraps
from fastapi import Request, HTTPException

def get_keycloak_token(func):
    """Decorator to fetch Keycloak token based on request."""
    @wraps(func)
    def wrapper(request: Request, *args, **kwargs):
        body = asyncio.run(request.json())
        username = body.get("username")
        password = body.get("password")

        if not username or not password:
            raise HTTPException(
                status_code=400,
                detail="Username or password not provided in the request body."
            )
        token = KeycloakAuth(keycloak_config,username=username, password=password).obtain_keycloak_token()

        kwargs['token'] = token
        return  func(request=request, *args, **kwargs)

    return wrapper




def verify_roles(required_roles: List[str]):
    """Decorator to verify JWT token and required roles."""
    def decorator(func):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header:
                raise HTTPException(status_code=401, detail="Authorization token is missing.")

            if not auth_header.startswith("Bearer "):
                raise HTTPException(
                    status_code=401,
                    detail="Invalid Authorization header format. Expected 'Bearer <token>'."
                )

            token = auth_header.split(" ")[1]
            try:
                decoded_token = KeycloakAuth(keycloak_config).verify_token(token, required_roles)
            except Exception as e:
                raise HTTPException(status_code=403, detail=str(e))

            kwargs["decoded_token"] = decoded_token
            return await func(request, *args, **kwargs)

        return wrapper
    return decorator