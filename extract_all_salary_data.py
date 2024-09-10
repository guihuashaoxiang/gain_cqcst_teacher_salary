import re
import os
import pandas as pd


def get_salary_data(html_content):
    # 定义正则表达式模式
    pattern = re.compile(r'<font[^>]*>\s*([\s\S]*?)\s*</font>', re.IGNORECASE)

    # 使用 findall 查找所有匹配项
    matches = pattern.findall(html_content)

    # 输出所有匹配到的内容
    if matches:
        odd_index_data = matches[1::2]
        even_index_data = matches[0::2]
        return odd_index_data, even_index_data
    else:
        print("没有找到匹配的内容")


def get_sorted_files(salary_data_path):
    # 获取指定路径下所有以"salary_data_"开头的HTML文件
    salary_files = [file for file in os.listdir(salary_data_path) if
                    file.startswith("salary_data_") and file.endswith(".html")]
    # 定义提取年份和月份的正则表达式
    pattern = re.compile(r'salary_data_(\d{4})_(\d{1,2})\.html')

    # 解析文件名中的年份和月份，并按年份和月份升序排序
    def parse_filename(filename):
        match = pattern.match(filename)
        if match:
            year, month = map(int, match.groups())
            return (year, month)
        return (0, 0)

    # 按年份和月份排序文件列表
    sorted_files = sorted(salary_files, key=parse_filename)
    return sorted_files


# 逐一打开并处理文件
def path_read_extraction(salary_data_path):
    sorted_files = get_sorted_files(salary_data_path)
    all_salary_data = []
    for filename in sorted_files:
        file_path = os.path.join(salary_data_path, filename)
        with open(file_path, 'r', encoding='gbk') as file:
            html_content = file.read()
            odd_index_data, even_index_data = get_salary_data(html_content)
        all_salary_data.append(even_index_data)
        all_salary_data.append(odd_index_data)
    # 从第二行开始，每隔一行删除
    result = [row for index, row in enumerate(all_salary_data) if index < 2 or (index - 2) % 2 != 0]
    df = pd.DataFrame(result)
    # 保存 DataFrame 到 Excel 文件
    df.to_excel('doc/output.xlsx', index=False, header=False)


if __name__ == '__main__':
    path_read_extraction('./salary_data')
