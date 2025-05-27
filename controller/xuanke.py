from polars import DataFrame


async def generate_xuanke_df(df_origin: DataFrame) -> DataFrame:
    """
    todo)) 查找DataFrame中包含#符号的单元格位置
    Args:
        df_origin: 输入的polars DataFrame
    Returns:
        包含行号、列号的DataFrame
    """
    results = []
    columns = df_origin.columns

    for row_idx in range(df_origin.height):
        for col_idx, _ in enumerate(columns):
            value = df_origin[row_idx, col_idx]
            if isinstance(value, str) and "#" in value:
                results.append({"row": row_idx, "column": col_idx})

    return DataFrame(results)
