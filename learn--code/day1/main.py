# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import numpy as np
import json
import os
import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def download():
    # 设置请求头
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    ,'Cookie':'NMTID=00OxXPTM1vZ3eJk9UCYh-U6L7uWPFgAAAGVjm6L3A; _iuqxldmzr_=32; _ntes_nnid=f03bded6e9301d9bf83f131666b8d228,1741851363395; _ntes_nuid=f03bded6e9301d9bf83f131666b8d228; WEVNSM=1.0.0; WNMCID=rzrwct.1741851364408.01.0; __snaker__id=WiyHNtNSofVeR1tH; WM_TID=7YOsYmoJKrZBQAFRRRbEMCXbumneNOn0; ntes_utid=tid._.PsuvflC5Ok1FAwAVVVeU1dXGah4japFT._.0; sDeviceId=YD-jCdCPGxNDjpAA1EUEFaUfdH1MD5pW51t; __remember_me=true; ntes_kaola_ad=1; __csrf=b0da8cfcc90a7abdfa902c375850198a; gdxidpyhxdE=NqD%5CtnwoYDXwcnz%5CxBDx5nZqSJbwagGExwyfYxR%2Ba%2BCQLKBVaav4gNIo0MqB4vgokxlYwKSJ%2F26pZW0NWRk%2BD9v4LccnGTxv%5CbAYWLNSqMjdhkeX3dRV1f1y6IgU5bUecvl8QP7TyJjruKM%2F3E0GvIoaNkNzNGV%2BaQV%5C7jItZ%2BLnU1RR%3A1743243130333; MUSIC_U=00D7681E108A7629674577F8D9CBEF908C1F6DD3DB9BB8232E4B8885D976D2C3626CF55919EC8CDB62AEA75496A695CE7619330AF8E9319E07BAE0D0B8DED1B5A283EE17B6A73DA136E1234C9E16D9B8B787B3E0176494E325FD137899E28D4F87150D597D0752EEAF276058A6C6D9D0499FEABB6295EF9D3B591BEEFF2FAC442D093C79E01DA8935CB0FF09B263FF3AA1F604DC7D263B9A5DBBBE94C6041905070A82E44731CCEA8D614C1846B5E4542A6E0919891341CD42E9F936AB2FDF86149464EC250374807C992D3E8AA6B394CCC6EACD6EE88D81948224AC0DDC061720F6762253B6C3CE2384A654EDD4A10F634F756220709275A112EAC91B86EE7F088083C37E94E0165ECDA96AC78D6D3DF87FBFC1F9208495DBAD03EC71DB79A41150DC0A90D1C0AC6B4489537C40A41C54273B262252C4D5F30859646495B8B374C6525824B2FF6534B808798FD36723524CD2C9357F2C11B9CA8A0A29A5FE8A8A; __csrf=2d5fb8300bd569ba7b10f0d8a20a4f70; WM_NI=4lvXDiSzo%2BeK5f5z0hHdOxt%2B1sG6eD9nUbAsLStgmoQi2BIegB07pA6eqrmGOGY8zx1rKrHSkob%2FWyDErn9cw4hk542JPhHhr%2FV%2FWMW2FZBeu8LOkpbEQClpXnvmEmdVb1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6d46ea3f5fdadb14b88b08eb6d54f968e9a82d643f5b9bd86d6438fabfcd1b62af0fea7c3b92af8b4bab9c76391a6a1cce841f7bafb9bb3648cbc8199f721f3ad89d7e850fbb29b83c479908dbc88f06593b7fea3cc6fa59e00d8f34bf6bbbf93f04d8d9997d9f974f3ae8593cb59a9b1aed0d673889bbe8fbc69b5eca88cb840f296a089cb64b2f19ad0d64795ee8abbc16fb7e884b0ea7ca29b9fa4ef7c9cb2ba8ec867a88aaed2d837e2a3; JSESSIONID-WYYY=ctsIRtbJuJnu1C2RFb2xB%5CxAg6YnzyNB20ceG%2Fj4Vtt%5C1NJsnVHl6JAMJ5jcPeOt2hjxbwCJlSY9rJGrWaVJjCj0%2Ft%2B7sBPHd4rlcGy2cbY%2FAPxXB7ey%2FOarCszYiJxvhS0s4tE92gOvpPlW%2F53UXzTbs%2Fro2MnSNyP8MWQvsx%2FDhc%2Fe%3A1743350855071; playerid=49714531'
            }
    url='http://m704.music.126.net/20250331002459/d2f939c6cb121b982b5fa857086c0abc/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/31076613864/2453/0719/5c1b/41b1a50a67e3bd4a58fd2b40b119ad05.m4a?vuutv=Y7CWrPGecpNIacWNgXpdkPgcO0UtGRF0hFyV1Lgs47PJ3GbaIX3I8Vmo61uQxiz/F8tYFBpgpvARybfYFWkGAc7WnpTDUopBivnuQ3M4MDw=&authSecret=00000195e7c800d118780a3084b0131a"'
    save_dir = '陈奕迅歌曲'  # 保存目录
    song_name= '001'
    # save_path = os.path.join(save_dir, '{}.mp3'.format(song_name))  # 拼接保存路径和文件名


    response = requests.get(url, headers=headers,allow_redirects=True)
    with open('001.mp3', 'wb') as f:  # 以二进制写入模式打开文件
            f.write(response.content)

    print('下载成功')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(sys.version)
    download()


