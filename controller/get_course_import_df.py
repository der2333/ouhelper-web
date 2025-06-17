from polars import DataFrame


async def get_course_import_df(df_origin: DataFrame) -> DataFrame:
    """
    从 Polars DataFrame 中查找包含特定符号 "+" 的单元格，提取学生选课信息

    该函数遍历 DataFrame 的每个单元格，如果单元格中包含 "+" 符号，则提取该学生对应的学号、姓名以及所选课程的课程代码和课程名称，并将这些信息以 DataFrame 的形式返回

    参数：
        df_origin: 包含选课信息的 Polars DataFrame

    返回值：
        选课导入模板的 Polars DataFrame，列包括 "学号", "姓名", "课程代码", "课程名称"
    """

    # 初始化输出列表，用于存储包含特定符号的单元格信息
    output: list[dict[str, str]] = []

    columns = len(df_origin.columns)  # 获取DataFrame的所有列名

    for row_idx in range(8, df_origin.height):  # 遍历每一行
        for col_idx in range(3, columns):  # 遍历每一列
            value = df_origin[row_idx, col_idx]  # 获取当前单元格的值

            name: str = df_origin[row_idx, 0]  # 获取第1列的值作为姓名
            student_id: str = df_origin[row_idx, 1]  # 获取第2列的值作为学号
            course_id: str = df_origin[5, col_idx]  # 获取第5行的值作为课程代码
            course_name: str = df_origin[7, col_idx]  # 获取课程名

            # 检查单元格是否为字符串类型，并且包含"+"符号
            if (
                isinstance(value, str)
                and (value == "+" or int(value) < 60)
                and course_id is not None
            ):
                output.append(
                    {
                        "学号": student_id,
                        "姓名": name,
                        "课程代码": course_id,
                        "课程名称": course_name,
                    }
                )

    return DataFrame(output)
