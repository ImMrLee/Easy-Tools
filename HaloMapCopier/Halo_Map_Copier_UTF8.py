
import shutil
import os
print("这个程序能帮助你快速把你下载的光环地图文件导入到游戏内，保证地图文件和该程序在同一文件夹")
file=input(r"地图文件名叫什么，打出完整文件名: ")
target=input(r"告诉我你安装MCC的磁盘盘符，打出相应字母: ")
game=(":\\SteamLibrary\\steamapps\\common\\Halo The Master Chief Collection")
gen=int(input("告诉我目标光环游戏代数，打出相应数字就行 "))
if (gen == 1):
    halo=("\\halo1\maps")
elif (gen == 2):
    halo=("\\halo2\h2_maps_win64_dx11")
elif (gen == 3):
    halo=("\\halo3\maps")
elif (gen == 4):
    halo=("\\halo4\maps")
else:
    print("光环10出来了都不一定管，退出重进")
    os.system("pause")

shutil.copy (file, target+game+halo)
print ("完事 :DDDD")
os.system("pause")