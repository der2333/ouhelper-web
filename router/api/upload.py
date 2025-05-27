from io import BytesIO
from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse
import polars
from controller import generate_xuanke_df

upload_file = APIRouter()


@upload_file.post("/api/upload/xuanke")
async def xuanke_file(file: UploadFile) -> StreamingResponse:
    try:
        df_origin = polars.read_excel(
            source=file.file,
            raise_if_empty=False,
            infer_schema_length=0,
        )
    finally:
        await file.close()

    df_output = await generate_xuanke_df(df_origin)

    output = BytesIO()
    df_output.write_excel(output)
    output.seek(0)

    headers = {"Content-Disposition": 'attachment; filename="xuanke.xlsx"'}
    return StreamingResponse(
        content=output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers,
    )
