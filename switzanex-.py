import requests , csv , time
from bs4 import BeautifulSoup
from lib import nqtm


def remove_slashn(word):
    while "\n" in word :
        word = word.replace('\n','')


    return word


def find_people_named(name,writer,k):
    url = "https://zip.ch/fr/results/?q="+name+"&page="
    head = {'User-agent':'Mozilla/5.0 (Linux; Android 9; SM-G960F '\
                            'Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) '\
                            'Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36'}
    fonction = ""
    Name = ""
    Fonction = "inconu"
    T = []
    count = 0
    for i in range(0, 2010, 1):
        if i != 0 :
            if i == 1 :
                nqnt = nqtm.xyz()
                nqnt.secure(writer)
                
            h = 0
            bn = False
            while bn == False :
                try:
                    result = requests.get(url+str(i) , headers = head)
                    code = result.status_code
                    bn = True
                except Exception as e:
                    h = h + 1
                    time.sleep(h+5)
                    pass


            if code == 200:
                soup = BeautifulSoup(result.text)
                if "Oops... Ça n'a rien donné" in soup.text :
                    return k
                block = soup.find_all('div' ,class_ = """infos cell""")
                for b in block :
                    parsed_block = BeautifulSoup(str(b), 'lxml')
                    try:
                        fonction = parsed_block.find('span', {'class' : "category small ellipsis block"})
                    except Exception as e:
                        print(e)
                        Fonction = "inconu"
                        pass
                    try:
                        Name = parsed_block.find_all('h2')
                        address1 = parsed_block.find('span', {'class' : "address__street nowrap ellipsis"})
                        address2 = parsed_block.find('strong', {'class' : 'nowrap ellipsis'})
                    except Exception as e:
                        print(e)
                        pass
                    phone_paragraph = parsed_block.find('p', {'class' : "phone"})
                    parsed_phone_paragraph = BeautifulSoup(str(phone_paragraph), 'lxml')
                    try:
                        tel_link = parsed_phone_paragraph.find('a')
                        phone_Number = tel_link['href'].replace('tel:','')
                    except Exception as e:
                        print(e)
                        phone_Number = ""
                        pass
                    try:
                        Fonction = remove_slashn(fonction.text.replace('        ',''))
                    except Exception as e:
                        Fonction = "Inconu"
                        pass

                    NAME  = remove_slashn(Name[0].text.replace('        ',''))
                    try:
                        Address1 = address1.text
                    except Exception as e:
                        Address1 = ""
                        pass

                    Address2 = address2.text
                    Phone = phone_Number
                    T.append([Phone, Fonction , NAME , Address1 , Address2])
            else :
                print(str(code))
            for ccc in T :
                if ccc[0] not in k :
                    writer.writerow(ccc)
                    print("----------------------------------------------")
                    print(ccc)
                    k.append(ccc[0])

                else :
                    count = count + 1
                print(len(T))


    return k

with open('database.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Numero" , "Fonction", "Nom" , "Add1" , "Add2" ])
    k = []
    k = find_people_named("076",writer,k)

with open('database.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Numero" , "Fonction", "Nom" , "Add1" , "Add2" ])
    k = []
    k = find_people_named("078",writer,k)

with open('database.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Numero" , "Fonction", "Nom" , "Add1" , "Add2" ])
    k = []
    k = find_people_named("079",writer,k)
