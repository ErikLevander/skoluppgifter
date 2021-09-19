import math




choice = input("Skriv k för att räkna ut volymen på en kub eller t för volymen på en tetrahedron: \n")
if choice == ("k"):
    side = input(str("Ange sidans längd på kuben i centimeter: \n"))
    cube = float(side) ** 3
    print("Kubens volym är " + str(cube) + " cm³")

if choice == ("t"):
    tside = input(str("Ange sidan längd på tetrahedronen: \n"))
    rot = math.sqrt(2)
    tetra = (float(tside) ** 3) / (6 * float(rot))
    print("Tetrahedronens volym är: " + str(tetra) + " cm³")