# 重庆城市科技学院教师“我的薪酬”每月工资查询汇总分析

## 2024年9月10日教师节送某人的礼物![0CFA599B](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/0CFA599B.png?raw=true)让工资不在糊涂

## 联系邮箱：guihuashaoxiang78@gmail.com，建议或者需要功能联系

### Python环境和安装几个库

可以直接手动安装，命令如下`pip install pandas requests matplotlib`

### 如何获取`JSESSIONID`

- 浏览器进入**`我的薪酬`**查询页面

![image-20240910201723640](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/image-20240910201723640.png?raw=true)

- 浏览器`F12`打开调试页面，如下图切换到**`网络`**，然后如上图更换不为当前的日期，点击**`确定`**，找到**`employeeself.do`**,然后就能看见`JSESSIONID`，复制到Python项目`main.py`,后面就可以运行了

![image-20240910201610396](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/image-20240910201610396.png?raw=true)

将`JSESSIONID`复制到`main.py`中如下图区域，可以运行`main.py`输入`JSESSIONID`，也可以直接取消下面注释直接写死，下次过期了再改

![image-20240910204324405](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/image-20240910204324405.png?raw=true) 

## 当前功能

指定年月到指定年月的所有工资详细信息到本地，然后可选解析出Excel

![Snipaste_2024-09-10](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/%E6%8F%90%E5%8F%96%E5%87%BA%E6%89%80%E6%9C%89%E4%BF%A1%E6%81%AF.png?raw=true) 

![提取出所有信息]()

每月工资变化趋势，***下图仅作参考*** 

![每月工资变化趋势](https://github.com/guihuashaoxiang/gain_cqcst_teacher_salary/blob/main/readme.assets/%E6%AF%8F%E6%9C%88%E5%B7%A5%E8%B5%84%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true)

超时工资每月提取统计 
