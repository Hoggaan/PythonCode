#!/usr/bin/python
import re

line = 'Cats are smatter than dogs'

#searchObj = re.search(r'(.*) are (.*?) .*', line, re.M|re.I)

# if searchObj:
#     # print("searchObject.group() : ", searchObj.group())
#     # print("searchObject.group(1) : ", searchObj.group(1))
#     # print("searchObject.group(2) : ", searchObj.group(2))
# else:
#     print("No search!!")

# matchObj = re.match(r'dogs', line, re.M|re.I)
# if matchObj:
#     print("Match---->matchObj.group() : ", matchObj.group())
# else:
#     print("No Match")

# searchobj = re.search(r'dogs', line, re.M|re.I)
# if searchobj:
#     print("search-----> searchobj.group() : ", searchobj.group())
# else:
#     print("Not Found")

#phone = "2004-959-559 # This is Phone Number."

# num = re.sub(r'#.*$',"", phone)
# print("Phone Num: ", num)

# num1 = re.sub(r'\D', "", phone)
# print("Mobile Num: ", num1)

#cmnt = re.search('?#', phone)
#print(cmnt)

# REGEX correy Tutorial
text_to_search = '''
abcdefghijklmnopqrstuv
ABCDEFGHIJKLMNOPQRSTUV
mmsdlkm 

wax kale iska qor

822-783-2748
329.392.2392
700.392.2392
500-392-2392

AmericaAmerica 

. ^ $ * + ? [] { } () / \ | 

Cishqi iyo Jacyl

Aflagaadadu waa wax reeban 
Fadlan isag joogsada oo yaanay afkiina idika barin

Waxaan idiin sheegayaa inaad Alle ka cabsataan

Abdulaziz Aw Hassan Farax

fagaaraha.com
fagaaraha.net
fagaaraha.so

Mohamed MohamudMohamud Hassan $200
kol
tol 
yol
col

Mr. Habiibullah waa lajan
Mr Hayaan
Mr. hurdaaye
Mr. Hudhude
Mr. T
Mr. HAGE
Ms. Halima
Mrs. Hayat



'''

text = 'Maxaa kaa galay dhamaad'

pattern = re.compile(r'Dhamaad')
matches = pattern.match(text, re.I, re.M)
#for match in matches:
print(matches)

# pattern = re.compile(r'[a-zA-Z]]')

# with open("tutorials/data.txt", 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:
#         print(match)


'--------------------------------*******----------------------------------'
# ## Emails
# emails = '''
# CoreyMSchafer@gmail.com
# corey.schafer@university.edu
# corey-321-schafer@my-work.net
# '''

# pattern = re.compile(r'[a-zA-Z1-9-.]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern.finditer(emails)

# for match in matches:
#     print(match)

'------------------------************________________________________'
#### URLS 
urls = '''
https://www.google.com
http://microsoft.com
https://www.amazon.com
http://youtube.com
http://aniga.cirka
'''
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')


# # matches = pattern.finditer(urls)
# # for match in matches:
# #     print(match.group(3))

# suburls = pattern.sub(r'\2\3', urls)
# print(suburls)