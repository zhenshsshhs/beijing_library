import mail
import chapiao
import json, datetime, time
import pandas as pd
import 抢票
from threading import Thread
import file
have_tick = 0
need = file.readfile("need.txt", 'r')

needed = file.readfile("needed.txt", 'r')


def weekday_stick_status(fp, up_week=0):
    global needed
    print("-" * 20)
    print("step2--时间为", end=':')
    print(datetime.datetime.today())

    note = 0
    #
    # with open('1.json', 'r', encoding='utf8')as fp:
    #     json_data = json.load(fp)
    #     # print('这是文件中的json数据：',json_data)
    #     # print('这是读取到文件数据的数据类型：', type(json_data))

    json_data = json.loads(fp)
    tick_status = json_data.get("content").get("Lists")
    inintation()

    result = []
    for day_status in tick_status:
        # print(day_status['DayCode'])
        # 将日期转换为星期几
        week = pd.to_datetime(str(day_status['DayCode'])).weekday() + 1
        # 打印每日的余票
        tick_left = day_status['Secent'][0]['TicketNumber'] - day_status['Secent'][0]['PeopleNumber']
        print(day_status['DayName'] + "\t余票:" + str(tick_left))

        if week >= up_week and tick_left > 0:
            result.append(day_status['DayName'] + "\t余票:" + str(tick_left))
            # print(day_status['DayName']+"\t余票:"+str(tick_left))

            # 检查当前日期是否在已经抢到的日期内,若有则删除
            # print(day_status['DayCode'] in needed)
            if (day_status['DayCode'] in need) and (day_status['DayCode'] in needed):
                need.remove(day_status['DayCode'])

            # 检查有无票,由此决定要不要发邮件
            if (day_status['DayCode'] in need) and (day_status['DayCode'] not in needed):
                SceneId = day_status['Secent'][0]['Id']

                if 抢票.qiangpiao(SceneId):
                    print("step3")
                    # needed.append(day_status['DayCode'])
                    needed = file.writefile("needed.txt", "a",day_status['DayCode'])
                    need.remove(day_status['DayCode'])
                    end = "抢票成功:\n" + "\n".join('%s' % id for id in needed) + "\n还在抢:\n" + "\n".join(
                        '%s' % id for id in need)
                    mail.send_mail(msg_to="2439228606@qq.com", subject="石景山图书馆抢到票了", content=end)

                else:
                    print("有票,未抢到票")
                    end = "抢票失败:" + day_status['DayCode']
                    mail.send_mail(msg_to="2439228606@qq.com", subject="石景山图书馆有票,但未抢到,注意手动操作", content=end)
            else:
                # 提示是否要抢票
                note = 1

    result_string = "\n".join(result)

    if note == 1:
        print("指定日期无票,无需抢票")
        print("-" * 20)
    return result_string


def thd1():
    fp = chapiao.check_libary_site()
    str1 = weekday_stick_status(fp)


def tf():
    end = "已经抢到:\n" + "\t".join('%s' % id for id in needed) + "\n正在抢:\n" + "\t".join(
        '%s' % id for id in need)
    print(end + '\n' + "*" * 20)
    print("输入你要抢的日期(在五分钟内结束)---例如:\n20220101")
    while (True):
        a = input()
        if len(a) != 8:
            print("输入不合法\n")
        else:
            need.append(int(a))

def inintation():
    needed.sort()
    for i in need:

        if i in needed:
            need.remove(i)
    print(need)

if __name__ == '__main__':
    while True:
        try:
            for i in range(3):
                print("*" * 20)
            thd1()
            thd = Thread(target=tf)
            thd.daemon = True
            thd.start()
            time.sleep(300)


        except:
            print("出错!")
            time.sleep(300)
