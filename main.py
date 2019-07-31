import re
import csv

def get_table_from_file(filename):
    with open(filename, "r+") as myfile:
        table = [line.strip().split(",") for line in myfile]

    return table

def get_rendered_tajs(filename):
    table = filename
    TAJ = []
    [TAJ.append(re.sub("-", "", element[col_1])) for element in table]
    new_tajs = [re.sub(" ", "", tajs) for tajs in TAJ]
    taj_dict = {tajnumber: index for index, tajnumber in enumerate(new_tajs)}
    return taj_dict

def compare(lista1, lista2): #lista = list of rendered tajnumbers
    # common_tajs = []
    # for key, value in lista1.items():
    #     if key in lista2.keys():
    #         common_tajs.append((value, lista2[key], key))
    # return common_tajs[1:]

    # return dict(map(lambda kv: {kv[0], (kv[1], lista2.get(kv[0], None))}, lista1.items()))

    common_tajs = [[k, lista1[k], lista2[k]] for k in lista1.keys() if k in lista2]
    return common_tajs

def merge_files(common_tajs, table1, table2):
    final = []
    for tajnum, index1, index2 in common_tajs:
        item = table1[index1] + table2[index2]
        final.append(item)
    return final


def export(final):
    csvData = final
    with open('merged.csv', 'w') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(csvData)
    newFile.close()

def original_data_append(table_1, final):
    with open("merged.csv", 'a') as myfile:
        for row in table_1:
            if any(row[0] in element for element in final):
                row = str((",").join(row) + ("\n"))
                myfile.write(row)

col_1 = int(input("Plese add the number of the containing column"))
col_2 = int(input("Plese add the number of the containing column"))

def main():
    csv_1 = "Personal info.csv"
    #csv_1 = input("Please, add base CSV file name: ")
    # col_1 = int(input("Plese add the number of the containing column"))
    # #csv_2 = input("Please, add base CSV file name: ")
    # col_2 = int(input("Plese add the number of the containing column"))
    csv_2 = "DrGregoryHouse.csv"
    table_1 = get_table_from_file(csv_1)
    print(table_1)
    table_2 = get_table_from_file(csv_2)
    newtajs_1 = get_rendered_tajs(table_1)
    newtajs_2 = get_rendered_tajs(table_2)
    common_tajs = compare(newtajs_1, newtajs_2)
    final = merge_files(common_tajs, table_1, table_2)
    print(final)
    export(final)
    # print(newtajs_1)
    # print(newtajs_2)
    # print(common_tajs)
    original_data_append(table_1, final)


if __name__ == "__main__":
    main()


