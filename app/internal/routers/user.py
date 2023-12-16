from fastapi import APIRouter
from app.pkg.redis_tools.tools import RedisTools

router = APIRouter(
    prefix="/api/v1/user"
)


@router.get('/hello')
def user_hello():

    return {
        'hello': 'world'
    }
