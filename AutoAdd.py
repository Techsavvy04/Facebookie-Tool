import re,requests,os
from time import sleep
from bs4 import BeautifulSoup as bs
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
def clear_console():
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux và macOS
        os.system('clear')
# Sử dụng hàm để xóa màn hình
clear_console()
def delay(n):
    for i in range(n,-1,-1):
        print(f"Tiếp tục sau {i}",end='\r')
        sleep(1)
class facebook:
    def __init__(self,cookie) -> None:
        self.url = 'https://mbasic.facebook.com'
        self.cookie=cookie 
        self.headFb = {
            "Host": "mbasic.facebook.com",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "dnt": "1",
            "x-requested-with": "mark.via.gp",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-encoding": "gzip, deflate",
            "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": self.cookie,
        }
        self.id=self.cookie.split('c_user=')[1].split(';')[0]
        
    def checklive(self):
        check =  requests.get(self.url,headers=self.headFb,allow_redirects=False)
        if 'Đăng xuất' in check.text:
            return True
        return False
    def getUseName(self):
        url=f'https://mbasic.facebook.com/profile.php?id={self.id}'
        data=requests.get(url,headers=self.headFb)
        checkUs=re.findall('<title>..*?</title>',data.text)[0].replace('<title>','').replace('</title>','')
        return checkUs
    def autoAddFriend(self,dl):
        url='https://mbasic.facebook.com/friends/center/mbasic/?fb_ref=tn&sr=1&ref_component=mbasic_home_header&ref_page=MFriendsCenterOutgoingRequestsController'
        data=requests.get(url,headers=self.headFb)
        soup = bs(data.content, 'html.parser')
        listFriend = soup.find_all(class_='w t')
        dem=0
        for td in listFriend:
            if 'gợi ý' in td.text or 'Thêm bạn bè' in td.text:
                dem+=1
                name = td.find('a').text
                link = td.find('a').get('href')
                friend_count = td.find('div', class_='cj ck').text if td.find('div', class_='cj ck') else "Không có bạn chung"
                if friend_count == '':friend_count='0'
                actions = [a.text for a in td.find_all('a', class_='z bb cm cn bd ba')]
                dt=requests.get(self.url+link,headers=self.headFb,allow_redirects=False)
                linkadd=re.findall('/a/friends/add/?.*?"',dt.text)[0].replace('"','').replace('amp;','')
                requests.get(self.url+linkadd,headers=self.headFb,allow_redirects=False)
                print(f'Đã gửi lời mời kết bạn đến {name}')
                delay(dl)
       

        
if __name__ == "__main__":
    ck=input("Nhập cookie facebook:")
    dl=int(input("Nhập delay ( Nên để ở 60s hoặc hơn để tránh bị block):"))
    clear_console()
    fb=facebook(ck)
    usname=fb.getUseName()
    id=fb.id
    print(f'FACEBOOK:{usname} | ID {id}')
    while True:
        fb.autoAddFriend(dl)
    