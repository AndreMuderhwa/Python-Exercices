# nom=input("Saisissez votre nom")
# print("Bonjour ",nom)
# print(f"Bonjour {nom}")

###EXERCICE SUR LES CONDITIONS

# nom=input("Saisi ton nom \n")
# age=int(input("Saisi ton age \n"))

# if age>=18:
#     print(f"Bonjour {nom} vous avez {age} ans donc vous etes  majeur")
# else:
#     print(f"Bonjour {nom} vous avez {age} ans donc vous etes  mineur")

####EXERCICE SUR LES BOUCLES

# i=0
# while(i<11):
#     print(f"Bonjour {i}")
#     i=i+1
# for abc in range(10):
#     print(f"Bonjour {abc}")

##########EXERCICE SUR LE DEVINETTE


# nomAdeviner="Lydia"
# while(True):
#     nom=input("Saisi le nom a deviner \n")
#     if nom == nomAdeviner:
#         print("Bravo vous avez trouve la bonne reponse !!")
#         break
#     else:
#         print(f"Desole vous avez echoue, la reponse etait {nomAdeviner}")
#         reponse=input("Voulez vous continuez O/N \n")
#         if reponse =="O" or reponse == "o":
#             continue
#         elif reponse =="N" or reponse =="n":
#             break
#         else:
#             print("Vous avez saisi une mauvaise reponse! \n Choisissez uniquement O/N")
#             break
#








# tmp_c=float(input("Saisi la temperature en Celsius\n"))

# tmp_f=(tmp_c * 9/5)+32

# print(f"La temperature {tmp_c}oC en oF est egal a {tmp_f}")



#LES LISTES
# MyListe=list()
# Maliste=[12,34,66,'Sanel','Lydia','Satira',67.890]
# Maliste[0]="test"
# print(Maliste[0])
# print(Maliste[5:])
# print(Maliste[4:5])
# Maliste.append("Beatrice")
# Maliste.remove('Satira')
# for i in Maliste:
#     print(i)
# nom='ABC'
# print(len(nom))
# if 'BeatriceA' in Maliste:
#     print("Elle existe")
# else:
#     print("Elle n'existe pas")

#LES DICTIONNAIRES

# MonDico={
#     "nom":"Nshokano",
#     "postnom":"Satira",
#     "prenom":"Sanel",
#     "age":24,
#     "salaire":1200.89
# }
# for q in MonDico:
#     print(q)
# MyDico=dict()
# MonDico["age"]=67
# print(MonDico.values())
# print(MonDico.keys())

# print(MonDico.get("age"))
# print(MonDico["age"])

#EXERCICES
# angl_fr={}
# i=1
# while(i<4):
#     an_mot=input("Saisissez un mot en anglais \n")
#     fr_mot=input(f"Saisissez l'equivalent de {an_mot} en francais \n")
#     angl_fr[an_mot]=fr_mot
#     i=i+1

# motArechercher=input("Rechercher un mot en anglais et en francais \n")
# if motArechercher in angl_fr.keys():
#     print(f"Le mot {motArechercher} en francais c'est {angl_fr[motArechercher]}")

# elif motArechercher in angl_fr.values():
#     value=[q for q in angl_fr if angl_fr[q]==motArechercher]
#     resultat="".join(value)
#     print(f"Le mot {motArechercher} en anglais c'est {resultat}")
# else:
#     print(f"Le mot {motArechercher} est introuvable !!")




# def findMax(maListe : list ) -> int:
#     rs=maListe[0]
#     for n in maListe:
#         if n > rs:
#             rs=n

#     return rs

# print(findMax([1,2,4,5,6,7,8,90,8,0]))

# const letterFrequency =(phrase) =>{
#     // let new_phrase=phrase.toLowerCase();
#     let frequency={}
#     for(const letter of phrase){
#         if(letter in frequency){
#             frequency[letter] += 1
#         }
#         else{
#             frequency[letter] = 1
#         }
#     }
#     return frequency
# }

# def letterFrequency(phrase : str) -> dict:
#     frequency={}
#     for letter in phrase:
#         if letter in frequency:
#             frequency[letter] +=1
#         else:
#             frequency[letter]=1
#     return frequency


# def wordFrequency(phrase : str) -> dict:
#     word=phrase.split(" ")
#     return letterFrequency(word)


# print(wordFrequency("hello hello my name is memea is"))





def AddItem(myList : list, item : any) -> list :
    return myList + [item]
    


print(AddItem([],'TRACK'))