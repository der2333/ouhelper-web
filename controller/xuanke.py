from polars import DataFrame


async def generate_xuanke_df(df_origin: DataFrame) -> DataFrame:
    """
    查找DataFrame中包含特定符号（例如#）的单元格位置，并返回包含行号、列号的DataFrame

    参数:
        df_origin: 输入的polars DataFrame

    返回值:
        df_output: 包含行号、列号的DataFrame
    """
    output = []  # 初始化输出列表，用于存储包含特定符号的单元格信息
    columns = df_origin.columns  # 获取DataFrame的所有列名

    for row_idx in range(df_origin.height):  # 遍历每一行
        for col_idx, _ in enumerate(columns):  # 遍历每一列
            value = df_origin[row_idx, col_idx]  # 获取当前单元格的值

            # 检查单元格是否为字符串类型，并且包含"#"符号
            if isinstance(value, str) and "+" in value:
                name: str = df_origin[row_idx, 0]  # 获取第1列的值作为姓名
                student_id: str = df_origin[row_idx, 1]  # 获取第2列的值作为学号
                course_id: str = df_origin[5, col_idx]  # 获取第5行的值作为课程代码
                course_name: str = df_origin[7, col_idx]  # 获取课程名
                output.append(
                    {
                        "学号": student_id,
                        "姓名": name,
                        "课程代码": course_id,
                        "课程名称": course_name,
                    }
                )

    return DataFrame(output)
