import re
import requests


def check_login_status(html_content):
    patterns = [
        r'<input type="text" name="username"',
        r'<input  type="password" name="password"',
        r'<input type="text" name="appdate"'
    ]

    for pattern in patterns:
        if re.search(pattern, html_content):
            print("web页面需要重新登录")
            return False  # 需要重新登录
    print("web页面已登录")
    return True  # 已登录


def get_jsessionid(username, password):
    """
    获取jsessionid
    :param username:
    :param password:
    :return:
    """
    url = "http://222.179.90.230:7002/logon/logonService"
    headers = {
        "Host": "222.179.90.230:7002",
        "Connection": "keep-alive",
        "Content-Length": "60",
        "Cache-Control": "max-age=0",
        "Origin": "http://portal.cqucc.com.cn:8017",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "http://portal.cqucc.com.cn:8017/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    data = {
        "flag": "25",
        "validatepwd": "false",
        "user_ID": username,
        "password": password
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        jsessionid = response.cookies.get("JSESSIONID")
        print("jsessionid获取成功:", jsessionid)
        return jsessionid
    else:
        print("获取jsessionid失败")
        return None


def refactor_headers(base_url, jsessionid):
    # 构造请求头
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "pragma": "no-cache",
        "proxy-connection": "keep-alive",
        "upgrade-insecure-requests": "1",
        "cookie": f"bosflag=el4; JSESSIONID={jsessionid}",
        "Referer": f"{base_url}",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }
    print("请求头构造完成")
    return headers


if __name__ == '__main__':
    with open("./salary_data/salary_data_2023_10.html", "r", encoding="gbk") as f:
        html_content = f.read()
        check_login_status(html_content)
