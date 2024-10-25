import requests,re
def ghi(data):
    try:
        with open('result.txt','w',encoding='utf-8') as f:
            f.write(data)
            f.close()
        print('Ghi file thành công')
    except:
        print('Không thể ghi file')
class  FACEBOOKIE:
    def __init__(self,cookie) -> None:
        self.cookie = cookie
        self.url='https://mbasic.facebook.com'
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
    def checkLive(self):
        check = requests.get(self.url,headers=self.headFb,allow_redirects=False)
        if "Đăng xuất" in check.text:
            return True
        else:
            return False
    def getUseName(self):
        if self.checkLive() is False:return {'error':'Cookie Die Rồi Lấy Lại Code Để Chạy Nha'}
        url=f'https://mbasic.facebook.com/profile.php?id={self.id}'
        data=requests.get(url,headers=self.headFb)
        checkUs=re.findall('<title>..*?</title>',data.text)[0].replace('<title>','').replace('</title>','')
        return checkUs
    def follow(self,id):
        if self.checkLive() is False:return {'error':'Cookie Die Rồi Lấy Lại Code Để Chạy Nha'}
        url=f'https://mbasic.facebook.com/profile.php?id={id}'
        pr=requests.get(url,headers=self.headFb)
        findBtnFollow=re.findall('/a/subscribe.php?.*?"',pr.text)
        if findBtnFollow == []:return {'error:Không tìm thấy nút theo dõi'}
        linkFollow = findBtnFollow[0].replace('"','').replace('amp;','')
        requests.get(self.url+linkFollow,headers=self.headFb,allow_redirects=False)
        return 'success'
    def reaction(self,id,type):
        choice=0
        if   type.lower() == 'like':choie=0
        elif type.lower() == 'love':choice=1
        elif type.lower() == 'care':choice=2
        elif type.lower() == 'haha':choice=3
        elif type.lower() == 'wow':choice=4
        elif type.lower() == 'sad':choice=5
        else:choice=6
        if self.checkLive() == False:return {'error':"Cookie Die Rồi Lấy Lại Code Để Chạy Lại Nha !"}
        linkVL=f'https://mbasic.facebook.com/{id}'
        getLink=requests.get(linkVL,headers=self.headFb,allow_redirects=False)
        if getLink.status_code != 301:return {'error':'Không thể chuyển hướng'}
        redirect_url = getLink.headers.get('Location')
        dataBtnReact=requests.get(redirect_url,headers=self.headFb)
        findRect = re.findall('/reactions/picker/?.*?"',dataBtnReact.text)
        if findRect == []:return "Không tìm thấy nút bày tỏ cảm xúc"
        rect=findRect[0].replace('"','').replace('amp;','')
        link = self.url+rect        
        dataRect = requests.get(link,headers=self.headFb,allow_redirects=False)
        listrect=re.findall('/ufi/reaction/?.*?"',dataRect.text)
        if len(listrect) != 7:return "Không tìm thấy các nút bày tỏ cảm xúc"
        linkLike=listrect[choice].replace('"','').replace('amp;','')
        requests.get(self.url+linkLike,headers=self.headFb,allow_redirects=False)
        return 'success'
# ck='sb=DkPuZrpl6KPxhWEeqmLtLtgp;datr=DkPuZuNL3p4AivNRqAHBwxcA;ps_l=1;ps_n=1;c_user=100061150001837;m_page_voice=100061150001837;dpr=0.9375;ar_debug=1;xs=36%3AjO9ge87kXq0Nxw%3A2%3A1727053016%3A-1%3A6283%3A%3AAcV_X37Nt-4xN_W4ZLh0R0FfJGXKtBgPdHW4hKU3AG2l;fr=19VMvmdcAcUf0OKJa.AWW_-6zEt91YvsfIN-Xkki5w_ok.BnGPEa..AAA.0.0.BnGPmq.AWWueijZowg;wd=1022x972;presence=C%7B%22t3%22%3A%5B%7B%22o%22%3A0%2C%22i%22%3A%22g.7292462020838376%22%7D%5D%2C%22utc3%22%3A1729690809276%2C%22v%22%3A1%7D;'
# fb=FACEBOOKIE(ck)
# a=fb.reaction('122117103932544510','like')