import math

count = 0


def ask_user(prompt):
    s = input(prompt)
    try:
        result = eval(s)
        return result
    except:
        return 0


def cubeanswer():
    side = input(str("Ange sidans längd på kuben i centimeter: \n"))
    cube = float(side) ** 3
    print("Kubens volym är " + str(cube) + " cm³")
    

def tetraanswer():
    tside = input(str("Ange sidan längd på tetrahedronen: \n"))
    rot = math.sqrt(2)
    tetra = (float(tside) ** 3) / (6 * float(rot))
    print("Tetrahedronens volym är: " + str(tetra) + " cm³")


def menu():
    print('\n\n========================================')
    print('|            Vad vill du göra?         |')
    print('|                                      |')
    print('|  1. Beräkna volymen på en kub        |')
    print('|  2. Beräkna volymen på en tertahedron|')
    print('|  3. Avsluta                          |')
    print('========================================')
    


while True:
    menu()
    choice = ask_user('Gör ditt val: ')
    if choice == 1:
        cubeanswer()
        count += 1
    elif choice == 2:
        tetraanswer()
        count += 1   
    elif choice == 3:
        print(f'Du har gjort {count} beräkningar. Välkommen tillbaka')
        break
    else:
        print('\n -----> Försök igen <-----')