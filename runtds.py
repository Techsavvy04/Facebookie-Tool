from random import *
import requests,re,os,sys
from time import sleep
from FACEBOOKIE import *
from TDS import *
def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux và macOS
        os.system('clear')
# Sử dụng hàm để xóa màn hình
clear_console()
ck='sb=9rUCZ46kRRnmou6EWWlp7EKu;datr=9rUCZ5m_KHOnxzfktIv-Uo-d;dpr=1.25;ps_l=1;ps_n=1;locale=vi_VN;wd=1536x730;c_user=100089801793694;fr=1wK05j3klt51MePDW.AWW8BDMugtZFiBpKx9QX89zokOg.BnG7EW..AAA.0.0.BnG7EW.AWWrmeTWPqQ;xs=44%3AbFBGoFv6kOIKwQ%3A2%3A1729868044%3A-1%3A6283%3A%3AAcWOVamQy_Imzq1Jsmm4bj4WyXyu6Yxosoehb8giyQ;'
fb=(FACEBOOKIE(ck))
token='TDSQfiYjclZXZzJiOiIXZ2V2ciwiI5JXZt9meiojIyV2c1Jye'
tds=TDS(token)
infoTds=tds.getInfoTds()
xu=infoTds['data']['xu']
user=infoTds['data']['user']
listNv=['like','follow','reaction']
# listNv=['reaction']
print(f'Tài khoản {user} | Số xu hiện có {xu} | SUCCESS')
while True:
    nv=choice(listNv)
    if nv=="reaction":
        listJob=tds.getTaskList("reaction")
        print(f"Đã tìm thấy {len(listJob)} reaction")
        for i in listJob:
            id=idJob=i["id"]
            type=i['type']
            ##  làm nhiệm vụ reactiom 
            lam=fb.reaction(id,type)
            if 'error' in lam:
                xu=tds.getInfoTds()["data"]['xu']
                print(f"msg => {lam['error']} | Số xu hiện tại:{xu}")
                sleep(30)
                continue
            else:
                nhan=tds.claimCoin(type,idJob)
                if 'error' in nhan or "Thất bại! Bạn chưa like ID này!" in nhan:
                    xu=tds.getInfoTds()["data"]["xu"]
                    err="Thất bại"
                    print(f"msg => {err} | Số xu hiện tại:{xu}")
                    sleep(30)
                    continue
                else:
                    print(nhan)
                    xu=tds.getInfoTds()["data"]["xu"]
                    print(f"msg => Làm nhiệm vụ reaction thành công | Số xu hiện tại {xu}")
                    sleep(30)  
    if nv=="follow":
        listJob=tds.getTaskList('follow')
        print(f'Đã tìm thấy {len(listJob)} nhiệm vụ follow')
        for i in listJob:
            id=idJob=i['id']
            print(idJob)
            ## Làm nhiệm vụ follow
            lam=fb.follow(id)
            if 'error' in lam:
                xu=tds.getInfoTds()["data"]['xu']
                print(f"msg => {lam['error']} | Số xu hiện tại:{xu}")
                sleep(30)
                continue
            else:
                nhan=tds.claimCoin('follow',idJob)
                if 'error' in nhan or "Thất bại! Bạn chưa like ID này!" in nhan:
                    xu=tds.getInfoTds()["data"]["xu"]
                    err="Thất bại"
                    print(f"msg => {err} | Số xu hiện tại:{xu}")
                    sleep(30)
                    continue
                else:
                    print(nhan)
                    xu=tds.getInfoTds()["data"]["xu"]
                    print(f"msg => Làm nhiệm vụ theo dõi thành công | Số xu hiện tại {xu}")
                    sleep(30)
    if nv=="like":
        listJob=tds.getTaskList('like')
        print(f'Tìm Thấy {len(listJob)} nhiệm vụ like')
        for i in listJob:
            
            idJob=i['id']
            if len(idJob.split('_'))==2:id=idJob.split("_")[1]
            else:id=idJob.split("_")[0]
            ## Làm nhiệm vụ like
            lam=fb.reaction(id,"like")
            if 'error' in lam:
                xu=tds.getInfoTds()["data"]['xu']
                print(f"msg => {lam['error']} | Số xu hiện tại:{xu}")
                sleep(30)
                continue
            else:
                nhan=tds.claimCoin('like',idJob)
                if 'error' in nhan:
                    xu=tds.getInfoTds()["data"]["xu"]
                    err=nhan["error"]
                    print(f"msg => {err} | Số xu hiện tại:{xu}")
                    sleep(30)
                    continue
                else:
                    xu=tds.getInfoTds()["data"]["xu"]
                    print(f"msg => Like thành công | Số xu hiện tại {xu}")
                    sleep(30)

            
    