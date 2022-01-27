##
# 北京图书馆抢票 
目前运行正常,使用过程中无异常,稳定运行一星期
##
## 各功能模块介绍:

  1.chaopiao.py 

    使用requests访问预约网站,访问成功后将其网站内容返回.

  2.file.py 

    函数readfile为一个读入文件,并将其转换为列表.

    函数readfile为将成功预约日期写入needed.txt文件
    
  3.mail.py
  
    负责发送邮件,可指定内容和收件人
    
  4.main.py
 
  5.抢票.py
  
    当需要预约时,发送post请求并检查预约情况
    

##
## 主要功能

1.对指定日期的票,每隔五分钟检查每天的余票情况,并支持在运行中添加预约日期.

<img src=picture/运行截图.png>

2.通过mail.py邮箱通知预约成功

<img src=picture/邮箱发送.PNG>

网站效果:

<img src=picture/预约效果2.jpeg>
