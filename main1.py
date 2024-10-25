# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next = None
# class HangDoi:
#     def __init__(self):
#         self.Head = None
#         self.pTai = None
#     def isRong(self):
#         if self.Head is None:
#             return True
#         return False
#     def themPhanTu(self,data):
#         newNode=node(data)
#         if self.isRong():
#             self.Head = self.pTai = newNode
#         else:
#             self.pTai.next = newNode
#             self.pTai = newNode
#     def xoaphanttu(self):
#         if self.isRong():
#             return "Không có phẩn tử nào để xóa"
#         temp = self.Head
#         self.Head = self.Head.next
#         if self.Head is None:
#             self.pTai = None
#         return temp.data
#     def peek(self):
#         if self.isRong():
#             return 'Không có phần tử nào có trong hàng đợi'
#         return self.Head.data
#     def showHangDoi(self):
#         if self.isRong():
#             print("Không có phần tửu để hiển thị")
#         else:
#             curent=self.Head
#             while curent:
#                 print(f'{curent.data}',end='->')
#                 curent=curent.next
#             print('None')
# hangdoi=HangDoi()
# hangdoi.themPhanTu(10)
# hangdoi.themPhanTu(10)
# hangdoi.themPhanTu(10)
# hangdoi.themPhanTu(10)
# hangdoi.showHangDoi()
class Node:
    def __init__(self,tenhang,soluong):
        self.tenhang = tenhang
        self.soluong = soluong
        self.next =None
class QuanLyKhoHang:
    def __init__(self):
        self.Head = None
        self.pTai = None
    def isRong(self):
        return self.Head is None
    def ThemHang(self,tenHang,soLuong):
        hangMoi = Node(tenHang,soLuong)
        if self.isRong():
            self.Head = self.Head.next = hangMoi
        else:
            self.Head.next = hangMoi
            self.pTai = hangMoi
    def xoaMatHangDau(self):
        if self.isRong():
            return 'Không có mặt hàng nào để xóa'
        temp = self.Head
        self.Head = self.Head.next
        if self.Head is None:
            self.pTai = None
        return temp.tenhang
    ### Tìm kiếm mặt hàng theo tên 
    def timkiem(self,tenhang):
        tenhang = tenhang.lower()
        if self.isRong():
            print("Không có mặt hàng nào để tìm kiếm")
        else:
            current = self.Head
            while current:
                if current.tenhang.lower() == tenhang:
                    print(f"Tìm thấy mặt hàng {current.tenhang} có số lượng {current.soluong}")
                current=current.next
    def hienThi(self):
        if self.isRong():
            print("không có mặt hàng nào để hiển thị")
        else:
            current=self.Head
            while current:
                print(f'Mặt hàng {current.tenhang} có số lượng {current.soluong}')
                current = current.next
if __name__ == "__main__":
    if __name__ == "__main__":
        kho = QuanLyKhoHang()
        kho.ThemHang("Gạo", 50)
        kho.ThemHang("Đường", 30)
        kho.hienThi()
        kho.xoaMatHangDau()
        kho.hienThi()
        kho.timkiem("Đường")