import re

def get_table_from_file(filename):
    with open(filename, "r+") as myfile:
        table = [line.strip().split(",") for line in myfile]

    return table

csv_1 = "Personal info.csv"
#csv_1 = input("Please, add base CSV file name: ")
col_1 = int(input("Plese add the number of the containing column"))

#csv_2 = input("Please, add base CSV file name: ")
#col_2 = int(input("Plese add the number of the containing column"))
csv_2 = "DrGregoryHouse.csv"

def get_rendered_tajs(filename):
    table = get_table_from_file(filename)
    TAJ = []
    [TAJ.append(re.sub("-", "", element[col_1])) for element in table]
    new_tajs = [re.sub(" ", "", tajs) for tajs in TAJ]
    taj_dict = {index: tajnumber for index, tajnumber in enumerate(new_tajs)}
    return taj_dict

def compare(lista1, lista2): #lista = list of rendered tajnumbers
    common_tajs = []
    for number in lista1.values():
        if number in lista2.values():
            common_tajs.append(number)
    return common_tajs

def main():
    csv_1 = "Personal info.csv"
    #csv_1 = input("Please, add base CSV file name: ")
    col_1 = int(input("Plese add the number of the containing column"))

    #csv_2 = input("Please, add base CSV file name: ")
    #col_2 = int(input("Plese add the number of the containing column"))
    csv_2 = "DrGregoryHouse.csv"
    table_1 = get_table_from_file(csv_1)
    table_2 = get_table_from_file(csv_2)
    newtajs_1 = get_rendered_tajs(csv_1)
    newtajs_2 = get_rendered_tajs(csv_2)
    common_tajs = compare(newtajs_1, newtajs_2)
    print(newtajs_1)
    print(newtajs_2)
    print(common_tajs)

main()


