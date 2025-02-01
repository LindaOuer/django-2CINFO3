# classe = "Hello 2CINFO3"

# print(classe)
# # print(type(classe))

# print(classe[1:3])
# print(classe[::-1])

# name = "Mohamed"
# print(f'Hello {name}')
# print('Hello ' + name)


# print(jours[3])
# print(jours[:3])
# print(jours[::3])
# print(len(jours))

d = {
    0: 'a',
    1: 'b'
}
keys = d.keys
values = d.values
for key, value in d.items():
    print(f'key: {key}, value: {value}')

jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
toVerify = "Vendredi"
if toVerify in jours:
    print('exists')
else:
    print ('Not Found')
    
for i in range(5):
    print(i)
    
for i in range(5):
    if i == 3:
        break
    print(i)
    
for i in range(5):
    nb = int(input("Entrez un entier: "))
    if nb % 2 == 0:
        print('pair')
    else:
        print('impair')
        
def greetings(nom = "Mohamed"):
    """_summary_
        Saluer une personne
    Args:
        nom (str, optional): _description_. Defaults to "Mohamed".
    """
    print(f'Hello {nom}')
    
greetings('Malek')
greetings()
print (help(greetings))

def diviseur(nb):
    # list = []
    # for i in range(1, nb+1):
    #     if nb % i == 0:
    #         list.append(i)
    # return list
    return [i for i in range (1, nb+1) if nb % i == 0]

print(diviseur(12))