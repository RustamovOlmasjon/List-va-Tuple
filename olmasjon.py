#8 - masala  foydalanuvchining loginini tekshiring

login = "User_2025"

#1. vazifa: isalnum() bilan login faqat harf va raqamlardan iboratligini tekshiring


result1 = login.isalnum()

print("1 - vazifa natijasi ",result1)

#2 - vazifa
#isidentifier() bilan bu Pythonda identifikator bola olishini tekshiring

result2 = login.isidentifier()
print("2- vazifa natijasi",result2)

# 3 - vazifa
#startswith() bilan "user" bilan boshlanishini tekshiring

result3 = login.startswith("user")

print("3 vazifa natijasi",result3)

# 4 - vazifa natijasi
# endswith() bilan 2025 bilan tugashini tekshiring
result4 = login.endswith("2025")
print("4  - vazifa natijasini tekshiring",result4)


# 5 - vazifa natijasi
# replace() bilan userni admin bilan almashtiring
result5 = login.replace("user","admin")
print("5 - vazifa natijasi ",result5)

# 6 - vazifa
# count() yordamida r harfi necha marta qatnashganini toping
result6 = login.count("r")
print("6 - vazifa natijasi",result6)

# 7 - vazifa natijasi
# in operatori bilan "_" belgisi borligini tekshiring
result7 = "_" in login
print("7 - vazifa natijasi",result7)

# 8 - vzifa
# swapcase() yordamida katta harflarni kichikka va aksincha aylantiring
result8 = login.swapcase()
print("8 - vazifa natijasi",result8)
# 9 - vazifa
# isalpha() yordamida faqat harflardan iboratligini tekshiring
result9 = login.isalpha()
print("9 - vazifa natijasi",result9)

# 10 - vazifa
# len() yordamida login uzunligini aniqlang
result10 = len(login)
print("10 - vazifa natijasi",result10)

# 9-Masala: Foydalanuvchi izohi ustida ishlash

comment = "  bu dars juda foydali edi!    "

# 1.strip() yordamida bo‘sh joylarni olib tashlang
result1 = comment.strip()
print("1 - vazifa natijasi",result1)

# 2.capitalize() bilan birinchi harfni katta qilgan holda chiqarilsin
result2 = comment.capitalize()
print("2 - vazifa natijasi",result2)

# 3.upper() yordamida izohni katta harflarga o‘tkazing
result3 = comment.upper()
print("3 - vazifanatijasi",result3)

# 4.count() yordamida a harfi necha marta qatnashganini aniqlang
result4 = comment.count("a")
print("4 - vazifa natijasi",result4)

# 5.replace() yordamida foydali so‘zini muhimga almashtiring
result5 = comment.replace("foydali","muhim")
print(" 5 - vzifa natijasi ",result5)

# 6.endswith("!") orqali izoh hayrat belgisi bilan tugashini tekshiring
result6 = comment.endswith("!")
print("6 - vzifa natijasi ",result6)

# 7.split() orqali izohdagi so‘zlarni ajrating
result7 = comment.split()
print("7 - vazifa natijasi",result7)

# 8.title() yordamida har bir so‘z bosh harf bilan yozilsin
result8 = comment.title()
print("8 - vazifa natijasi",result8)

# 9.find("dars") yordamida dars so‘zining indeksini toping
result9 = comment.find("dars")
print("9 - vazifa natijasi",result9)

# 10.len() yordamida izoh uzunligini o‘lchang
result10 = len(comment)
print("10 - vqzifa natijasi",result10)

# 10-Masala: Foydalanuvchi email manzili bilan ishlash

email = "  johndoe2025@gmail.com   "

# vazifalar

# 1.strip() yordamida tashqi bo‘sh joylarni olib tashlang
result1 = email.strip()
print('1 - vazifa natijasi',result1)

# 2.lower() yordamida emailni kichik harflarga o‘tkazing
result2 = email.lower()
print("2 - vazifanatijasi",result2)

# 3.startswith("john") bilan boshlanishini tekshiring
result3 = email.startswith("john")
print("3 - vazifa natijasi",result3)

# 4.endswith(".com") bilan tugashini tekshiring
result4 = email.endswith(".com")
print("4 - vazifa natijasi",result4)

# 5.find("@") yordamida @ belgisi indeksini aniqlang
result5 = email.find("@")
print("5 - vazifa natijasi",result5)

# 6.split("@") yordamida username va domen qismlarini ajrating
result6 = email.split("@")
print("6 - vazifa natijasi",result6)

# 7replace("gmail", "yahoo") orqali domenni almashtiring
result7 = email.replace("gmail","yahoo")
print("7 - vazifa natijasi",result7)

# 8.in operatori bilan "2025" mavjudligini tekshiring
result8 = "2025" in email
print("8- vazifa natijasi",result8)

# 9.isprintable() yordamida email faqat chop etiladigan belgilar ekanligini aniqlang
result9 = email.isprintable()
print("9 - vazifa natijasi",result9)

# 10.len() yordamida email uzunligini toping
result10 = len(email)
print("10- vazifa natijasi",result10)

# 11-Masala: Kitob nomi bilan ishlash

book_title = "python programming basics"

# 1.Kitob nomini title() yordamida har bir so‘zning bosh harfini katta qiling
result1 = book_title.title()
print("1 - vazifa natijasi",result1)

# 2.upper() yordamida nomni to‘liq katta harflarga aylantiring
result2 = book_title.upper()
print("2 - vazofa natijasi",result2)

# 3.count("p") yordamida p harfi nechta ekanligini aniqlang
result3 = book_title.count("p")
print("3 - vazifa natijasi",result3)

# 4.find("programming") yordamida programming so‘zining boshlanish indeksini toping
result4 = book_title.find("programming")
print("4 - vazifa natijasi",result4)

# 5.replace("basics", "advanced") yordamida basics so‘zini advanced bilan almashtiring
result5 = book_title.replace("basics","advanced")
print("5 - vazifa natijasi",result5)

# 6.split() yordamida so‘zlarni ro‘yxatga ajrating.
result6 = book_title.split()
print("6 - vazifa natijasi",result6)

# 7.startswith("python") yordamida nomning python bilan boshlanishini tekshirng
result7 = book_title.startswith("python")
print(" 7 - vazifa natijasi",result7)

# 8.isalpha() yordamida matn faqat harflardan iboratligini tekshiring
result8 = book_title.isalpha()
print("8 - vazifa natijasi",result8)

# 9.join() yordamida so‘zlarni _ belgisi bilan birlashtiring
result9 = book_title.join("_")
print("9 - vazifa natijasi",result9)

# 10.len() yordamida kitob nomining uzunligini aniqlang
result10 = len(book_title)
print("10 - vazifa natijasi",result10)

# 12-Masala: Mahsulot kodi bilan ishlash

product_code = "ABC123xyz"

# vazifalar

# 1.isalnum() yordamida kod faqat harf va raqamlardan iboratligini tekshiring
result1 = product_code.isalnum()
print("1 - vazifa natijasi ",result1)

# 2.lower() yordamida kodni kichik harflarga aylantiring
result2 = product_code.lower()
print("2 - vazifa natijasi",result2)

# 3.swapcase() yordamida katta harflarni kichikka va aksincha o‘zgartiring
result3 = product_code.swapcase()
print("3 - VAZIFA NATIJASI",result3)

# 4.count("1") yordamida 1 raqami nechta ekanligini aniqlang
result4 = product_code.count("1")
print("4 - vazifa natijasi",result4)

# 5.startswith("ABC") yordamida kodning ABC bilan boshlanishini tekshiring
result4 = product_code.startswith("ABC")
print("5 - vazifa natijasi",result4)

# 6.endswith("xyz") yordamida kodning xyz bilan tugashini tekshiring
result6 = product_code.endswith("xyz")
print("6 - vazifa natijasi",result6)

# 7.find("123") yordamida 123 qismining indeksini toping
result7 = product_code.find("123")
print("7 - vazifa natijasi",result7)

 # 8.replace("xyz", "789") yordamida xyz ni 789 bilan almashtiring
result8 = product_code.replace("xyz","789")
print("8 - vazifa natijasi",result8)

# 9.kodni teskati tartibda chiqaring ->[::-1]
result9 = product_code[::-1]
print('9 - VZIFA natijasi',result9)

# 10.len() yordamida kod uzunligini aniqlang
result10 = len(product_code)
print("10 - vazifa natijasini toping",result10)


# 13-Masala: Xabar matni bilan ishlash


message = "Assalomu alaykum, bugun dars bormi?"

# vazifalar
# 1.capitalize() yordamida birinchi harfni katta qiling
result1 = message.capitalize()
print("1 - vazifa natijasi",result1)

# 2.upper() yordamida matnni to‘liq katta harflarga aylantiring
result2 = message.upper()
print("2 - vazifa natijasi",result2)

# 3.count("u") yordamida u harfi nechta ekanligini aniqlang.
result3 = message.count("u")
print("3 - vazifa natijasi",result3)

# 4.replace("bugun", "ertaga") yordamida bugun so‘zini ertaga bilan almashtiring.
result4 = message.replace("bugun","ertaga")
print("4 - vazifa natijasi",result4)

# 5.split() yordamida so‘zlarni ro‘yxatga ajrating.
result5 = message.split()
print("5 vzifa natijasi",result5)

# 6.endswith("?") yordamida matnning savol belgisi bilan tugashini tekshiring.
result6 = message.endswith('?')
print("6 - vazifa natijasi",result6)

# 7.find("dars") yordamida dars so‘zining indeksini toping.
result7 = message.find("dars")
print("7 - vazifa natijasi",result7)

# 8.in operatori yordamida "alaykum" so‘zi mavjudligini tekshiring.
result8 = "alaykum" in message
print(" 8 - vazifa natijasi",result8)

# 9.join() yordamida so‘zlarni | belgisi bilan birlashtiring.
result9 = message.join("|")
print("9 - vazifa natijasi",result9)

# 10.len() yordamida xabar uzunligini aniqlang.
result10 = len(message)
print("10 masala natijasi",result10)

# 14-Masala: Fayl nomi bilan ishlash


file_name = "document_2025.pdf"

# vazifalar
# 1.endswith(".pdf") yordamida faylning .pdf kengaytmasi bilan tugashini tekshiring
result1 = file_name.endswith(".pdf")
print("1 - masala natijasi",result1)

# 2.replace("_2025", "") yordamida _2025 qismini olib tashlang.
result2 = file_name.replace("_2025","")
print("2 - vazifa natijasi",result2)

# 3.split(".") yordamida fayl nomi va kengaytmasini ajrating.
result3 = file_name.split(".")
print("3 - vazifa natijasi ",result3)

# 4.upper() yordamida fayl nomini katta harflarga aylantiring.
result4 = file_name.upper()
print("4 - vazifa natijasi",result4)

# 5.count("_") yordamida _ belgisi nechta ekanligini aniqlang.
result5 = file_name.count("_")
print("5 - vazifa natijasi",result5)

# 6.startswith("doc") yordamida fayl nomining doc bilan boshlanishini tekshiring.
result6 = file_name.startswith("doc")
print("6 - vazifa natijasi",result6)

# 7.startswith("doc") yordamida fayl nomining doc bilan boshlanishini tekshiring.
result7 = file_name.startswith("doc")
print("7 - vazifa natijasi",result7)

# 8.isalnum() yordamida fayl nomi faqat harf va raqamlardan iboratligini tekshiring.
result8 = file_name.isalnum()
print("8 - vazufa natijasi",result8)

# 9.Fayl nomini teskari tartibda chiqaring → [::-1].
result9 = file_name[::-1]
print("9 vazifa natijasi",result9)

# 10.len() yordamida fayl nomi uzunligini aniqlang.
result10 = len(file_name)
print("10 - vazifa natijasi",result10)



# 15-Masala: Telefon raqami bilan ishlash


phone = "+998901234567"

# Vazifalar

# 1.startswith("+998") yordamida raqamning +998 bilan boshlanishini tekshiring.
result1 = phone.startswith("+998")
print("1 - vazifa natijasi",result1)

#2.isdigit() yordamida raqam faqat raqamlardan iboratligini tekshiring
# ( + belgisidan tashqari)
result2 = phone.isdigit()
print("2 - vazifa natijasi",result2)

# 3.replace("+998", "") yordamida kod qismini olib tashlang.
result3 = phone.replace("+998","")
print("3 - vazifa natijasi",result3)

# 4.count("9") yordamida 9 raqami nechta ekanligini aniqlang.
result4 = phone.count("9")
print("4 - vazifa natijasi ",result4)

# 5.in operatori yordamida "123" qismi mavjudligini tekshiring.
result5 = "123" in phone
print("5 - masala natijasi",result5)

# 6,find("456") yordamida 456 qismining indeksini toping.
result6 = phone.find("456")
print("6- vazifa natijasi",result6)

# 7.Raqamni teskari tartibda chiqaring → [::-1].
result7 = phone[::-1]
print("7 - vazifa natijasi",result7)

# 8.isprintable() yordamida raqam chop etiladigan belgilar ekanligini tekshiring.
result8 = phone.isprintable()
print("8 - vazifa natijasi",result8)

# 9.join() yordamida raqamni har bir belgisini , bilan birlashtiring.
result9 = phone.join(",")
print("9 - VAZIFA natijasi ",result9)

# 10. len() yordamida telefon raqami uzunligini aniqlang.
result10 = len(phone)
print("10 masala natijasi",result10)


# 16-Masala: Kalit so‘zlar bilan ishlash


keywords = "python, java, javascript, c++"

# Vazifalar

# 1.split(", ") yordamida kalit so‘zlarni ro‘yxatga ajrating.
result1 = keywords.split(", ")
print("1 - vazifa natijasi",result1)

# 2.join() yordamida kalit so‘zlarni ; belgisi bilan birlashtiring.
result2 = keywords.join(";")
print("2 - vazifa natijasi",result2)

# 3.replace("java", "ruby") yordamida java ni ruby bilan almashtiring.
result3 = keywords.replace("java","ruby")
print("3  - vzifa natijasi",result3)

# 4.count("a") yordamida a harfi nechta ekanligini aniqlang.
result4 = keywords.count("a")
print("4 - vazifa natijasi",result4)


# 5.in operatori yordamida "python" so‘zi mavjudligini tekshiring.
result5 = "python" in keywords
print("5 vazifa natijasi",result5)

# 6.find("c++") yordamida c++ qismining indeksini toping.
result6 = keywords.find("c+++")
print("6 - vazifa natijasi ",result6)

# 7.upper() yordamida kalit so‘zlarni katta harflarga aylantiring.
result7 = keywords.upper()
print("7 - vazifa natijasi ",result7)

# 8.islower() yordamida matn faqat kichik harflardan iboratligini tekshiring.
result8  = keywords.islower()
print("8 - vazifa  natijasi",result8)

# 9.startswith("python") yordamida matnning python bilan boshlanishini tekshiring.
result9 = keywords.startswith("python")
print("9 - vazifa natijasi ",result9)

# 10.len() yordamida kalit so‘zlar uzunligini aniqlang.
result10 = len(keywords)
print("10 - vazifa natijasi",result10)


# 17-Masala: Maqola sarlavhasi bilan ishlash
# String:

headline = "  Yangi texnologiyalar 2025  "

# Vazifalar:

# 1.strip() yordamida bosh va oxiridagi bo‘sh joylarni olib tashlang
result1 =   headline.strip()
print("1 - vazifa natijasi",result1)

# 2.title() yordamida har bir so‘zning bosh harfini katta qiling.
result2 = headline.title()
print("2 - vazifa natijasi",result2)

# 3.replace("2025", "2030") yordamida 2025 ni 2030 bilan almashtiring.
result3 = headline.replace("2025","2030")
print("3 - vazifa natijasi ",result3)

# 4.count("a") yordamida a harfi nechta ekanligini aniqlang.
result4 = headline.count("a")
print("4 - vazifa natijasi",result4)

# 5.split() yordamida so‘zlarni ro‘yxatga ajrating.
result5 = headline.split()
print("5 - vazifa natijasi",result5)

# 6.in operatori yordamida "texnologiyalar" so‘zi mavjudligini tekshiring.
result6 = "texnologiyalar" in headline
print("6 - vazifa natijasi",result6)

# 7.find("2025") yordamida 2025 qismining indeksini toping.
result7 = headline.find("2025")
print("7 - vazifa natijasi ",result7)

# 8.lower() yordamida sarlavhani kichik harflarga aylantiring.
result8 = headline.lower()
print("8 - vazifa natijasi",result8)

# 9.isspace() yordamida matn faqat bo‘sh joylardan iborat emasligini tekshiring.
result9 = headline.isspace()
print("9 - vazifa natijasi",result9)

# 10.len() yordamida sarlavha uzunligini aniqlang.
result10 = len(headline)
print("10 - vazifa natijasi",result10)


# 18-Masala: Kurs nomi bilan ishlash
# String:

course = "Data Science and Machine Learning"

# vazifalar
# 1.title() yordamida har bir so‘zning bosh harfini katta qiling.
result1 = course.title()
print("1 - vazifa natijasi",result1)

# 2.replace("Machine Learning", "AI") yordamida Machine Learning ni AI bilan almashtiring
result2 = course.replace("Machine Learning","AI")
print("2 - vazifa natijasi",result2)

# 3.count("a") yordamida a harfi nechta ekanligini aniqlang.
result3 = course.count("a")
print("3 - vaziva natijasi",result3)

# 4.find("Science") yordamida Science so‘zining indeksini toping.
result4 = course.find("Sciense")
print("4 - vazifa natijasi",result4)

# 5.split() yordamida so‘zlarni ro‘yxatga ajrating.
result5 = course.split()
print("5 - vazifa natijasi",result5)

# 6.startswith("Data") yordamida kurs nomining Data bilan boshlanishini tekshiring.
result6 = course.startswith("Data")
print("6 - vazifa natijasi",result6)

# 7.in operatori yordamida "Learning" so‘zi mavjudligini tekshiring.
result7 = "Learing" in course
print("7 -vazifa natijasi ",result7)

# 8.upper() yordamida kurs nomini katta harflarga aylantiring.
result8 = course.upper()
print("8 - vazifa natijasi",result8)


# 9.join() yordamida so‘zlarni _ belgisi bilan birlashtiring.
result9 = course.join("_")
print("9 - vazifa natijasi",result9)

# 10.len() yordamida kurs nomi uzunligini aniqlang.
result10 = len(course)
print("10 - vazifa natijasi ",result10)
