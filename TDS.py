import requests
class TDS:
    def __init__(self,token):
        self.token=token
    def getInfoTds(self):
        url=f"https://traodoisub.com/api/?fields=profile&access_token={self.token}"
        dataInfo=requests.get(url)
        if 'success' in dataInfo.json():
            data=dataInfo.json()
            user=data["data"]["user"]
            xu=data["data"]["xu"]
            xudie=data["data"]["xudie"]
            return data
        elif "error" in dataInfo.json():
            return (dataInfo.json()["error"])
        return ''
    def setConfigAccount(self,id):
        url=f'https://traodoisub.com/api/?fields=run&id={id}&access_token={self.token}'
        dataSetNick=requests.get(url)
        print(dataSetNick.json())
        if 'success' in dataSetNick.json():
            return  dataSetNick.json()["data"]["msg"]
        elif "error" in dataSetNick.json():
            return  dataSetNick.json()["error"]
        return ''
    def getTaskList(self,type):
        url=f'https://traodoisub.com/api/?fields={type}&access_token={self.token}'
        dataGetTaskList = requests.get(url)
        try:
            return dataGetTaskList.json()
        except:return 'Không thể lấy danh sách nhiệm vụ'
    def claimCoin(self,type,idJob):
        url=f'https://traodoisub.com/api/coin/?type={type}&id={idJob}&access_token={self.token}'
        dataCliamCoin=requests.get(url)
        if 'error' in dataCliamCoin.json():
            return (dataCliamCoin.json()['error'])
        return(dataCliamCoin.json())
# #100012111467811_1980452645701765
# token='TDSQfiYjclZXZzJiOiIXZ2V2ciwiI5JXZt9meiojIyV2c1Jye'
# tds=TDS(token)
# like=tds.getTaskList('like')
# print(like)
