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
    return new_tajs


def compare(lista1, lista2):
    common_tajs = []
    for number in lista1:
        if number in lista2:
            common_tajs.append(number)
    return common_tajs

def main():
    csv_1 = "Personal info.csv"
    #csv_1 = input("Please, add base CSV file name: ")
    col_1 = int(input("Plese add the number of the containing column"))

    #csv_2 = input("Please, add base CSV file name: ")
    #col_2 = int(input("Plese add the number of the containing column"))
    csv_2 = "DrGregoryHouse.csv"
    newtajs_1 = get_rendered_tajs(csv_1)
    newtajs_2 = get_rendered_tajs(csv_2)
    print(compare(newtajs_1, newtajs_2))

main()


