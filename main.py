from fastapi import FastAPI
import uvicorn
from router import course_import_router, get_page

app = FastAPI()

# 生成选课导入文件的路由
app.include_router(router=course_import_router)

# 获取前端页面
app.include_router(router=get_page)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=80, reload=True)
