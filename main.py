import fetch_data
import total_salary
import overtime_salary_details
import extract_all_salary_data

if __name__ == '__main__':
    salary_data_path = "./salary_data"
    select_fetch_data = input(
        "请输入要执行的功能：\n1.获取工资数据\n2.绘制总工资图\n3.超时工资\n4.提取所有工资数据\n输入其它拜拜：")
    if select_fetch_data == '1':
        """登录获取jesssionid暂未完善，因为我没有正确的密码"""
        # 查看readme.md获取jsessionid的获取方法
        # 登录信息，如果自己传入jsessionid，则不需要输入用户名和密码
        user_id = ""
        password = ""

        # 获取用户输入的JSESSIONID, 用于请求头的cookie
        jsessionid = input("请输入JSESSIONID: ")
        # 手动指定jsessionid
        # jsessionid = ""

        # 获取用户输入的起始年月和结束年月
        start_year, start_month = map(int, input("请输入起始年份和月份,以空格分隔: ").split())
        end_year, end_month = map(int, input("请输入结束年份和月份,以空格分隔: ").split())

        # 调试用，也可指定日期
        # start_year, start_month = 2023, 9
        # end_year, end_month = 2024, 9

        salary_data = "./salary_data"  # 存放在当前路径下的salary_data文件夹下，可自行修改
        # 获取指定年份月份到指定年份月份的每月工资数据
        fetch_data.get_monthly_salary_details(user_id, password, start_year, start_month, end_year, end_month,
                                              jsessionid,
                                              "salary_data", overwrite_existing=False)

    elif select_fetch_data == '2':
        """提取出每个月总工资并绘图"""
        total_salary.analyze_salary_data(salary_data_path)

    elif select_fetch_data == '3':
        """每个月超时工资"""
        overtime_salary_details.calculate_total_overtime_pay(salary_data_path)

    elif select_fetch_data == '4':
        """提取出文件保存路径下所有工资数据"""
        extract_all_salary_data.path_read_extraction(salary_data_path)
    else:
        print("请输入正确的数字,拜拜啦~")
