import re
import csv

col_1 = 0
col_2 = 0


def get_table_from_file(filename):
    with open(filename, "r+") as myfile:
        table = [line.strip().split(",") for line in myfile]

    return table


def get_rendered_tajs(table):
    TAJ = []
    [TAJ.append(re.sub("-", "", element[col_1])) for element in table]
    new_tajs = [re.sub(" ", "", tajs) for tajs in TAJ]
    taj_dict = {tajnumber: index for index, tajnumber in enumerate(new_tajs)}
    return taj_dict


def compare(rendered_list1, rendered_list2): #lista = list of rendered tajnumbers
    # common_tajs = []
    # for key, value in rendered_list1.items():
    #     if key in rendered_list2.keys():
    #         common_tajs.append((value, rendered_list2[key], key))
    # return common_tajs[1:]

    # return dict(map(lambda kv: {kv[0], (kv[1], rendered_list2.get(kv[0], None))}, rendered_list1.items()))

    common_tajs = [[k, rendered_list1[k], rendered_list2[k]] for k in rendered_list1.keys() if k in rendered_list2]
    return common_tajs


def anit_compare(rendered_list1, rendered_list2):
    common_tajs = [[k, rendered_list1[k]] for k in rendered_list1.keys() if k not in rendered_list2.keys()]

    return common_tajs


def merge_files(common_tajs, anti_tajs, table1, table2):
    merged_table = []
    for tajnum, index1, index2 in common_tajs:
        item = table1[index1] + table2[index2][1:]
        merged_table.append(item)
    for tajnum, index1 in anti_tajs:
        item = table1[index1]
        merged_table.append(item)

    return merged_table


def export(merged_table):
    csvData = merged_table
    with open('merged.csv', 'w') as newFile:
        writer = csv.writer(newFile)
        writer.writerows(csvData)
    newFile.close()


def main(csv1, csv2):
    table_1 = get_table_from_file(csv1) #list of listd
    table_2 = get_table_from_file(csv2) #list of list
    newtajs_1 = get_rendered_tajs(table_1) #dictionary
    newtajs_2 = get_rendered_tajs(table_2) #dictionary
    common_tajs = compare(newtajs_1, newtajs_2) #list of list
    print("Common TAJs:")
    print(common_tajs)
    print("\n")
    anti_tajs = anit_compare(newtajs_1, newtajs_2)
    print("Anti_tajs:")
    print(anti_tajs)
    print("\n")
    merged_table = merge_files(common_tajs, anti_tajs, table_1, table_2) #list of list
    export(merged_table)

main('DrGregoryHouse.csv', 'Personal info.csv')