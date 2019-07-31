import re

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


def compare(lista1, lista2): #lista = list of rendered tajnumbers
    common_tajs = []
    for key, value in lista1.items():
        if key in lista2.keys():
            common_tajs.append((value, lista2[key], key))
    return common_tajs
    # return dict(map(lambda kv: {kv[0], (kv[1], lista2.get(kv[0], None))}, lista1.items()))


def main(csv1, csv2):
    table_1 = get_table_from_file(csv1)
    table_2 = get_table_from_file(csv2)
    newtajs_1 = get_rendered_tajs(table_1)
    newtajs_2 = get_rendered_tajs(table_2)
    common_tajs = compare(newtajs_1, newtajs_2)
    print(common_tajs)
