import requests,json
import mail

url = "https://www.sjsggwh.com/yuyue/SubmitBook"


def qiangpiao(SceneId):
    # payload = {
    #     "Name": "郑帅杰",
    #     "IdType": "1",
    #     "IdNumber": "330683199902062819",
    #     "Mobile": "15201682934",
    #     # "SceneId": "46369",
    #     "SceneId": str(SceneId),
    #     "FacilitiesId": 4,
    #     "SpaceId": 2,
    #     "ExtMember": []
    # }
    payload={"Name":"罗奕颖","IdType":"1","IdNumber":"110101199811244526","Mobile":"18511807825","SceneId":str(SceneId),"FacilitiesId":4,"SpaceId":2,"ExtMember":[]}
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'Cookie: culsid=b39a5d627623050; edu_plt=CgpGC2HqDXFrSlGaFPbpAg==; cul=userid=426020&password=dKCvu05VlAzHYmIjPGwLGdnXebeHdFHsLxnMZQgbYmcl2Mf8HH2khKzU0OCJ0dr1',
        'Origin': 'https://www.sjsggwh.com',
        'Referer': 'https://www.sjsggwh.com/yuyue/book?id=4&spaceId=2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
    }
    proxies = {"http": None, "https": None}

    response = requests.request("POST", url, headers=headers, json=payload, proxies=proxies)

    if response.status_code == 200:
        print("访问抢票api成功")

        ret_res = json.loads(response.text)
        print(ret_res)
        if ret_res.get('state') == "-1":
            print("未抢到")
            return 0
        elif ret_res.get('state') == "1":
            print("抢到了")
            return 1
        elif ret_res.get('state') == "-104":
            print("已经抢了")
            return 1
        else:
            mail.send_mail(msg_to="352326430@qq.com", subject="石景山图书馆抢票有问题", content=ret_res)
            return 0
    else:
        print("访问抢票api失败")





    print(response.text)


if __name__ == '__main__':
    qiangpiao(46523)
