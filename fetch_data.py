import os
import datetime
import requests
import login


def get_monthly_salary_details(user_id, password, start_year, start_month, end_year, end_month, jsessionid, save_path,
                               overwrite_existing=False):
    """
    获取指定月份的工资数据,并保存到单独的文件中html文件中，默认覆盖刷新已存在的文件
    :param user_id: 用户ID
    :param password: 密码
    :param start_year: 起始年份
    :param start_month: 起始月份
    :param end_year: 结束年份
    :param end_month: 结束月份
    :param jsessionid: 用户的JSESSIONID
    :param save_path: 保存路径
    :param overwrite_existing: 是否覆盖已存在的文件，默认覆盖
    :return:
    """
    # 判断保存路径是否存在，不存在则创建
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # 请求的基本URL
    base_url = "http://222.179.90.230:7002/ykcard/employeeselfcard.do"

    # 构造请求头
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "pragma": "no-cache",
        "upgrade-insecure-requests": "1",
        "cookie": f"bosflag=el4; appdate=2024.09.03; JSESSIONID={jsessionid}",
        "Referer": base_url,
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    # 循环获取指定范围内的工资数据
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            if year == start_year and month < start_month:
                continue
            if year == end_year and month > end_month:
                break

            # 构造文件路径
            file_path = os.path.join(save_path, f"salary_data_{year}_{month}.html")

            # 判断文件是否已存在
            if overwrite_existing and os.path.exists(file_path):
                print(f"文件 {file_path} 已存在,跳过获取数据")
                continue

            # 构造请求体
            current_date = datetime.date.today().strftime("%Y-%m-%d")
            body = f"isMobile=null&isIOS=null&return=null&a0100=00003090&cardparam.queryflagtype=1&cardparam.cyyear={year}&cardparam.cymonth={month}&cardparam.cyear={year}&cardparam.cmonth={month}&cardparam.cdatestart={current_date}&cardparam.cdateend={current_date}&cardparam.csyear={year}&cardparam.season=1&cardparam.disting_pt=-1&cardparam.pageid=-1"

            # 发送POST请求
            response = requests.post(base_url, headers=headers, data=body)
            # 检查请求是否成功
            if response.status_code == 200:
                response.encoding = 'GBK'
                html_content = response.text
                # 检查登录状态
                if not login.check_login_status(html_content):
                    new_jsessionid = login.get_jsessionid(user_id, password)
                    headers = login.refactor_headers(base_url, new_jsessionid)  # 更新请求头
                    response = requests.post(base_url, headers=headers, data=body)  # 重新发送请求
                    response.encoding = 'GBK'
                    html_content = response.text

                with open(file_path, "w", encoding="GBK") as f:
                    f.write(html_content)
            else:
                print(f"获取工资数据失败: {year}年{month}月. 响应状态码: {response.status_code}")