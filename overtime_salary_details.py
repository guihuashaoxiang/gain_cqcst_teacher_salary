import os
import re


def parse_overtime_pay(html_content):
    pattern = re.compile(
        r'<font face="Arial" color="#15428b" style="font-weight:normal;font-size:9pt">\s*([\d.]+)\s*</font>')
    matches = pattern.findall(html_content)
    if len(matches) >= 9:
        overtime_pay = matches[8]
        return float(overtime_pay)
    else:
        return None


def calculate_total_overtime_pay(salary_data_path):
    total_overtime_pay = 0.0
    salary_data = []

    # 获取指定路径下所有以"salary_data_"开头的HTML文件
    salary_files = [file for file in os.listdir(salary_data_path) if
                    file.startswith("salary_data_") and file.endswith(".html")]

    for salary_file in salary_files:
        file_path = os.path.join(salary_data_path, salary_file)
        with open(file_path, "r", encoding="gbk") as f:
            html_content = f.read()
            overtime_pay = parse_overtime_pay(html_content)
            if overtime_pay is not None:
                year, month = salary_file.split(".")[0].split("_")[2:4]
                salary_data.append((int(year), int(month), overtime_pay))  # 将年份和月份转换为整数
                total_overtime_pay += overtime_pay
            else:
                print(f"在文件 {salary_file} 中没有找到超课时费数据")

    # 按照年份和月份排序
    sorted_salary_data = sorted(salary_data, key=lambda x: (x[0], x[1]))

    # 打印排序后的结果
    for year, month, overtime_pay in sorted_salary_data:
        print(f"{year}年{month}月\t超课时费为: {overtime_pay:.2f}")

    print(f"总超课时费为: {total_overtime_pay:.2f}")


# 调用函数，传入工资数据文件所在的路径
# salary_data_path = "salary_data"
# calculate_total_overtime_pay(salary_data_path)
