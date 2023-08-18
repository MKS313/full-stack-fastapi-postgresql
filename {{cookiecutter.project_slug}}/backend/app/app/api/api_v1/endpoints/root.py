from fastapi import status, HTTPException, Depends, APIRouter


#
router = APIRouter()


# Root
@router.get("/")
async def root():
    return {"ok": True, "detail": {}, "data": {'message': "welcome to EZS"}}


