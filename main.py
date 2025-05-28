from fastapi import FastAPI
import uvicorn
from router import upload_file
from router import get_page

app = FastAPI()

app.include_router(router=upload_file, tags=["formdata test"])  # 上传表格文件的api路由
app.include_router(router=get_page, tags=["Get Page"])  # 获取前端页面

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=3030, reload=True)
