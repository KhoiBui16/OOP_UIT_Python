class CChiTiet:
    def __init__(self):
        self._MaSo = 0

    def Nhap(self):
        self._MaSo = input("Nhap ma so chi tiet: ")

    def Xuat(self):
        print("Ma so chi tiet:", self._MaSo)

    def TinhTien(self):
        return 0

    def TimKiem(self, ms: str):
        if self._MaSo == ms:
            return self
        else:
            return None

class CChiTietDon(CChiTiet):
    def __init__(self):
        super().__init__()
        self.__GiaTien = 0

    def Nhap(self):
        super().Nhap()
        self.__GiaTien = float(input("Nhap gia tien chi tiet don: "))

    def Xuat(self):
        print("La chi tiet don.")
        super().Xuat()
        print("Gia tien chi tiet don:", self.__GiaTien)

    def TinhTien(self):
        return self.__GiaTien

    def TimKiem(self, ms):
        return super().TimKiem(ms)


class CChiTietPhuc(CChiTiet):
    def __init__(self):
        super().__init__()
        self.__n = 0
        self.__ds = []

    def Nhap(self):
        super().Nhap()
        self.__n = int(input("Nhap so luong chi tiet thanh phan: "))
        for _ in range(self.__n):
            type = int(input("Nhap loai (0. Don, 1. Phuc): "))
            temp = None
            if type == 0:
                temp = CChiTietDon()
            else:
                temp = CChiTietPhuc()
            temp.Nhap()
            self.__ds.append(temp)

    def Xuat(self):
        print("La chi tiet phuc.")
        super().Xuat()
        print("So luong chi tiet thanh phan cua chi tiet phuc:", self.__n)
        for i,x in enumerate(self.__ds):
            print(f"Chi tiet thanh phan thu {i + 1} cua chi tiet phuc:", end = ' ')
            x.Xuat()

    def TinhTien(self):
        s = 0
        for x in self.__ds:
            s += x.TinhTien()
        return s

    def TimKiem(self, ms: str):
        if self._MaSo == ms:
            return self
        for x in self.__ds:
            if x.TimKiem(ms) != None:
                return x.TimKiem(ms)
        return None


class CMay:
    def __init__(self):
        self.__n = 0
        self.__ds = []

    def Nhap(self):
        self.__n = int(input("Nhap so luong thanh phan: "))
        for _ in range(self.__n):
            temp = None
            type = int(input("Nhap loai (0. Don, 1. Phuc): "))
            if type == 0:
                temp = CChiTietDon()
            else:
                temp = CChiTietPhuc()
            temp.Nhap()
            self.__ds.append(temp)

    def Xuat(self):
        print("So luong chi tiet thanh phan cua may:", self.__n)
        for i, x in enumerate(self.__ds):
            print(f"Chi tiet thanh phan thu {i + 1} cua chi tiet may:", end = ' ')
            x.Xuat()

    def TinhTien(self):
        s = 0
        for x in self.__ds:
            s += x.TinhTien()
        return s

    def TimKiem(self, ms: str):
        for x in self.__ds:
            if x.TimKiem(ms) != None:
                return x.TimKiem(ms)
        else:
            return None


def main():
    May = CMay()
    print("Nhap thong tin may:")
    May.Nhap()
    print("\nThong tin cua may:")
    May.Xuat()
    gia_tri_may = May.TinhTien()
    print("\nGia tri cua may:", gia_tri_may)
    ma_so_tim_kiem = input("\nNhap ma so chi tiet may can tim: ")
    kq = May.TimKiem(ma_so_tim_kiem)
    if kq != None:
        print(f"Tim thay ma chi tiet: {ma_so_tim_kiem} trong may.")
    else:
        print(f"Khong tim thay ma chi tiet {ma_so_tim_kiem} trong may.")


if __name__ == "__main__":
    main()
