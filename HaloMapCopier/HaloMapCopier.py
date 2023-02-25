import shutil
import os
print("This Program Can Help You To Install Your Map. Thanks By Miste Lee")
file=input(r"What's The Map Name? Type the full name print: ")
target=input(r"Now Tell Me The Drive Letter That Installed The Game MCC: ")
game=(":\\SteamLibrary\\steamapps\\common\\Halo The Master Chief Collection")
gen=int(input("Now Tell Me The Gen of Halo "))
if (gen == 1):
    halo=("\\halo1\maps")
elif (gen == 2):
    halo=("\\halo2\h2_maps_win64_dx11")
elif (gen == 3):
    halo=("\\halo3\maps")
elif (gen == 4):
    halo=("\\halo4\maps")
else:
    print("What? Lazy. Exit!")
    os.system("pause")

shutil.copy (file, target+game+halo)
print ("Done :DDDD")
os.system("pause")