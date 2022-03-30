from fastapi.routing import APIRouter
from fastapi.param_functions import Depends
from fastapi.requests import Request
from databases.core import Database

# from search.schema import SearchCreate
# from search.model import search_keyword

search_router = APIRouter()


def get_db_conn(request: Request):
    return request.state.db_conn


# @search_router.post('/search')
# async def search_create(req: SearchCreate, db: Database = Depends(get_db_conn())):
#     query = search_keyword.inset()
#
#     await db.execute(query, req)
