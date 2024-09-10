import os
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.font_manager as fm
import random


def parse_overtime_pay(html_content, random_factor=False):
    """
    解析HTML内容，获取每个超课时费数据
    :param html_content:
    :return:
    """
    pattern = re.compile(
        r'<font face="Arial" color="#15428b" style="font-weight:bold;font-size:9pt">\s*([\d.]+)\s*</font>')
    matches = pattern.findall(html_content)
    if len(matches) >= 3:
        overtime_pay = matches[2]
        if random_factor:
            return float(overtime_pay)
            # return float(overtime_pay) * random.uniform(2, 3)  # 将每个月工资随机乘*倍到*倍，让某人看着高兴，我也高兴高兴，默认False

        else:
            return float(overtime_pay)
    else:
        return None


def analyze_salary_data(salary_data_path):
    """
    解析路径下所有工资html数据文件，获取每个月超课时费数据，并绘制折线图
    :param salary_data_path:
    :return:
    """
    total_overtime_pay = 0.0
    salary_data = []

    # 获取指定路径下所有以"salary_data_"开头的HTML文件
    salary_files = [file for file in os.listdir(salary_data_path) if
                    file.startswith("salary_data_") and file.endswith(".html")]

    for salary_file in salary_files:
        file_path = os.path.join(salary_data_path, salary_file)
        with open(file_path, "r", encoding="gbk") as f:
            html_content = f.read()
            overtime_pay = parse_overtime_pay(html_content, random_factor=True)  # 是否启动每月总工资随机乘以倍数，默认False
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

    # 绘制折线图
    plot_salary_trend(sorted_salary_data)


def plot_salary_trend(salary_data):
    # 设置中文字体
    plt.rcParams['font.family'] = 'SimHei'

    x_labels = [f"{year}年{month}月" for year, month, _ in salary_data]
    y_values = [overtime_pay for _, _, overtime_pay in salary_data]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(x_labels, y_values, marker='o')
    ax.set_xlabel('年月')
    ax.set_ylabel('实际到账工资(元)')
    ax.set_title('每月工资变化趋势')

    # 设置X轴刻度为每个年月
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels, rotation=45, ha='right')

    # 在每个数据点上显示数值
    for i, v in enumerate(y_values):
        ax.text(i, v + 100, f"{v:.2f}", ha='center')

    # 设置X轴刻度间距为1
    ax.xaxis.set_major_locator(MultipleLocator(1))

    plt.tight_layout()
    plt.show()

# # 调用函数，传入工资数据文件所在的路径
# salary_data_path = "./salary_data"
# analyze_salary_data(salary_data_path)
