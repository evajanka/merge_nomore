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
    taj_dict = {tajnumber: index for index, tajnumber in enumerate(new_tajs)}
    return taj_dict

def compare(lista1, lista2): #lista = list of rendered tajnumbers
    common_tajs = []
    for key, value in lista1.items():
        if key in lista2.keys():
            common_tajs.append((value, lista2[key], key))
    return common_tajs
    # return dict(map(lambda kv: {kv[0], (kv[1], lista2.get(kv[0], None))}, lista1.items()))

def main():
    csv_1 = "Personal info.csv"
    #csv_1 = input("Please, add base CSV file name: ")
    col_1 = int(input("Plese add the number of the containing column"))

    #csv_2 = input("Please, add base CSV file name: ")0
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


