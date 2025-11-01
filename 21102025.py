# # 1  masala
# # bal = int(input("balni kiriting "))
# # if bal < 0 or bal >100 :
# #     print("Xato: Ball 0 dan 100 gacha bo‘lishi kerak." )
# # else:
# #     if bal >= 90 :
# #         print("A")
# #     elif bal >= 80 :
# #         print("B")
# #     elif bal >= 70 :
# #         print("C")
# #     elif bal >= 60 :
# #         print("D")
# #     else:
# #         print("F")
#
# # 2 - masala
#
#
# # yosh = int(input("yoshni kiriting"))
# # daromat = int(input('daromatni kiriting '))
# #
# # if yosh <0 or yosh> 120 or daromat <0:
# #     print("Xato: Yosh 0-120 oralig‘ida, daromad musbat bo‘lishi kerak.")
# # else:
# #     if yosh < 18 :
# #         print('soliq 0%')
# #     elif yosh <= 60 :
# #         if daromat >5000 :
# #             print("soliq 20%")
# #         else:
# #             print("soliq 10%")
# #     else:
# #         print("5%")
#
#
#
# # 3- masala
# # kun = int(input("hafta kunini kiriting (1-7)"))
# # soat = int(input("soatni kiriting "))
# #
# # if kun < 1 or kun >7 or soat  < 0 or soat >23 :
# #     print("Xato: Kun 1-7, soat 0-23 oralig‘ida bo‘lishi kerak.")
# # else:
# #     if kun == 6 or kun == 7 :
# #         print("dam oliw ")
# #     else:
# #         if 9<= soat <= 17 :
# #             print("iw vahti ")
# #         else:
# #             print("iw vahtidan tawqari ")
#
# # 4 - masala
# #
# # harorat = int(input("haroratni kiriitng(C) "))
# # yomgir = input("yomgirli kun mu ? (ha, yoq.  ")
# # if -50 <=  harorat  > 60:
# #     print("Xato:")
# # elif harorat<0:
# #     print("qor yogiwi mumkin ")
# # elif harorat <= 20 and yomgir == "ha" :
# #         print("yogirli va sovuq ")
# # elif yomgir <= 20 and yomgir == "yoq ":
# #         print("sovuq lekn quruq ")
# # else:
# #     print("issiq ")
# #
# #
# # 5- masala
# masofa = int(input("masofani kiriting (km)"))
# vaht = int(input("vahtni kiriting "))
# if masofa <0 or vaht < 0 :
#     print("Xato: Masofa va vaqt manfiy bo‘lmasligi kerak.")
# else:
#     if masofa < 5 :
#         print("piyoda boring ")
#     elif masofa <= 50 :
#         if vaht > 1:
#             print("avtabusda boring ")
#         else:
#             print("velikda ")
#     else:
#         print("samalotta ")
#

# 6 - masala

# yow = int(input("yowni kiriting "))
# daromat = int(input("daromatni kiriting "))
# kiridit = int(input("kiridit summasini kiriting "))
# if yow < 18 or yow>100 or daromat <0 or kiridit <=0:
#     print("Xato: Yosh 18-100 oralig'ida, daromad va kredit summasi musbat bo'lishi kerak.")
# else:
#     if yow <21 :
#         print("berilmaydi ")
#     elif yow <= 60 :
#         if daromat>kiridit *0.2:
#             print("bariladi ")
#         else:
#             print("kiridit rad etildi ")
#     else:
#         print("kiridt faqat wart blan baeriladi ")


# 7 - masala

# ovqat = input("ovqat turini kiriting(Premium goshtli , odiy gowtli , baliqli , vigitiryan , odiy vigiritiryan  ) ")
# narx = int(input("narhini kiriting "))
#
# if narx <= 0:
#     print("Xato: Narx musbat bo'lishi kerak.")
# else:
#     if  ovqat == "Premium gowtli":
#         if narx >50 :
#             print("Premium goshtli taom")
#         else:
#             print("odiygowli taom")
#     elif ovqat == "baliq ":
#         print("baliqli taom ")
#     elif ovqat == "vigitiryan":
#         if narx <30 :
#             print("Premium vegetarian")
#         else:
#             print("Oddiy vegetarian")
#     else:
#         print("Xato: Noto'g'ri ovqat turi.")



# 8 - masla

# baxo = int(input("bxoni kiriting "))
# daromat = int(input("daromatni kiriting "))
# if baxo <0 or baxo >5 or daromat <0:
#     print("Xato: Baho 0-5.0 oraligida, daromad musbat bolishi kerak.")
# else:
#     if baxo < 3 :
#         print("Stipendiya yo'q")
#     elif baxo< 4 :
#         if daromat < 1000 :
#             print("Oddiy stipendiya")
#         else:
#             print("Stipendiya yo'q")
#     else:
#         if daromat <2000 :
#             print("Yuqori stipendiya")
#         else:
#             print("Stipendiya yo'q")

# 9 - masla
# daqiqa = int(input("daqqani kiriting "))
# internet = int(input("mbni kiting "))
# if daqiqa <0 or internet <0 :
#     print("Xato: Daqiqalar va internet manfiy bo'lmasligi kerak.")
# else:
#     if daqiqa <100 :
#         print("mini tarif ")
#     elif daqiqa <= 500:
#         if internet >5 :
#             print("standart tarif ")
#         else:
#             print("ekanom tarif ")
#     else:
#         print("perumum tarif ")


# 10 - masla

# harorat = int(input("haroratni kiriting (C)"))
# shamol = int(input("shamol tezligini kiriting "))
#
# if harorat <- 50 or harorat >50 or shamol <0 :
#     print("Xato: Harorat –50°C dan 50°C gacha, shamol manfiy emas.")
# else:
#     if harorat <10 or shamol >10 :
#         print("uyda otir ")
#     elif harorat <= 25 :
#         if shamol <5 :
#             print("sayr qiling ")
#         else:
#             print("ehtiyot boling ")
#     else:
#         print("buzdin buzdin flew iching ")

# 11 - masala
#
# soti = int(input("iw soatini kiriting "))
# tarjiba = int(input("tarjibani kiriting yil (1, 2, 3,)"))
# if soti <0 or tarjiba <0 :
#     print("Xato: Soat va tajriba manfiy bo'lmasligi kerak.")
# else:
#     if tarjiba <1  :
#         ish_haq = soti *10
#     elif  tarjiba <= 5:
#         if soti >40 :
#             ish_haq = soti* 15
#         else: ish_haq = soti *12
#     else: ish_haq = soti *20
#     print(f"umumiy ish haqi :${ish_haq }")
#

# 12 - masala

# oy = int(input("oy raqamini kiritring [1:12]"))
# harorat = int(input("haroratni kiriting "))
#
# if oy <1 or oy >12 or harorat <- 50 or harorat >50 :
#     print(- "Xato: Oy 1-12, harorat –50°C dan 50°C gacha bolishi kerak.")
# else:
#     if oy == 12 or oy == 1 or oy == 2 :
#         print("qish ")
#     elif oy >= 3 or oy <= 5 :
#         if harorat >15 :
#             print("iliq bahor ")
#         else:
#             print("sovuq bahor ")
#     elif oy >= 6 or oy <= 8 :
#         print("yoz")
#     else:
#         print("kuz ")

# 13 - masla


# summa = int(input("xarid summasini kiriting "))
# doimiy_mijos = input('doimiy_mijos (ha,yoq )')
# if summa <100 :
#     print("cegirma yoq ")
# elif summa<= 500 :
#     if doimiy_mijos == "ha":chegirma = 10
#     else: chegirma = 5
# else: chegirma = 15
# print(f"chegirma :{chegirma}%")


# 14 - masala
# tezlik = int(input("tezlikni kiriting"))
# hajm  = int(input("hajmini kiriting"))
# if tezlik  <= 0 or hajm <= 0 :
#     print("Xato: Tezlik va hajm musbat bo'lishi kerak.")
# else:
#     if tezlik < 10 :
#         print("yuklash sekn")
#     elif tezlik <= 50 :
#         if hajm > 1000 :
#             print("ortacha yuklash")
#         else:
#             print("tez yuklaw ")
#     else:
#         print("juda sekn ")


# 15 - masala

# ball = int(input("ballni kiriting "))
# jinsi = input("jinsini kiriting (erkak, ayol )")
# if ball <0 or ball >100 :
#     print("Xato: Ball 0 dan 100 gacha bo'lishi kerak.")
# else:
#     if jinsi == "erkak":
#         if ball >80 :
#             print('finalga chiqdi')
#         else:
#             print("saralawdan otmadi ")
#     elif jinsi == "ayol ":
#         if ball >75 :
#             print("finalga chiqdi ")
#         else:
#             print("saralashdan otib blmadi ")
#     else:
#         print("no togri jins kiritilgan ")

# 16 - masala

# istemol = int(input("istemolni kiriting"))
# vaht = input("vahtni kiriting (kecha , kunduz:)")
# tolov = int(input("tolovni kiriting"))
# if istemol <0 :
#     print("Xato: Iste'mol manfiy bo'lmasligi kerak.")
# else:
#     if vaht == "kecha ": tolov = istemol  * 0.05
#     elif vaht == "kunduz ":
#         if istemol> 100 : tolov = istemol *0.1
#         else: tolov = istemol *0.08
#     else:
#         print("Xato: Vaqt faqat 'kecha' yoki 'kunduz' bo'lishi kerak.")
#     print(f"elektr energiyasi:${tolov}")

# 17 - masala

# fan1 = int(input(" fan1 ballni kiriting "))
# fan2 = int(input('fan2 ballni kiriting '))
#
# if fan1 <0 or fan1 >100 or fan2 < 0 or fan2 >100 :
#     print("Xato: Ballar 0 dan 100 gacha bo'lishi kerak.")
# else:
#     if fan1 >80 or fan2 >80 :
#         print("alo ")
#     elif (fan1 > 80 or fan2 >60 ) or (fan2 >80 or fan1 >60 ):
#         print("yahshi ")
#     else:
#         print("qoniqrli")