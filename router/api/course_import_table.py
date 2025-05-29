from io import BytesIO
from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
import polars

from controller import get_course_import_df

course_import_router = APIRouter(prefix="/api/upload", tags=["选课导入文件生成"])


@course_import_router.post("/get_course_import_table")
async def course_import_table(file: UploadFile) -> StreamingResponse:
    """
    将上传的Excel文件生成选课导入文件

    参数:
        file (UploadFile): 上传的 Excel 文件

    返回值:
        StreamingResponse: 包含处理后的选课表文件的流式响应
    """
    try:
        df_origin = polars.read_excel(
            source=file.file.read(),
            raise_if_empty=False,
            infer_schema_length=0,
        )
    finally:
        await file.close()

    df_output = await get_course_import_df(df_origin)

    output = BytesIO()
    df_output.write_excel(output)
    output.seek(0)

    headers = {"Content-Disposition": 'attachment; filename="xuanke.xlsx"'}
    return StreamingResponse(
        content=output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers,
    )
