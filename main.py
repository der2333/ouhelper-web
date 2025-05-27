from fastapi import FastAPI
import uvicorn
from router import upload_file
from router import get_page

app = FastAPI()

app.include_router(router=upload_file, tags=["formdata test"])
app.include_router(router=get_page, tags=["Get Page"])

    
if __name__ == "__main__":
    uvicorn.run(app="main:app", port=3030, reload=True)
