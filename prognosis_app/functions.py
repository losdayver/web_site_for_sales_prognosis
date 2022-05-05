def csv_text_to_list(s):
    output = []
    while s != '':
        sub_s = ''
        index = s.find('\n')
        if index != -1:
            sub_s = s[:s.find('\n')]
            s = s[s.find('\n') + 1:]
        else:
            sub_s = s
            s = ''

        suboutput = []
        while sub_s != '':
            index = sub_s.find(';')
            if index != -1:
                colomn = sub_s[:sub_s.find(';')]
                suboutput.append(colomn)
                sub_s = sub_s[sub_s.find(';') + 1:]
            else:
                suboutput.append(sub_s)
                break

        output.append(suboutput)

    return output

def get_header_index(l, s):
    a = [x.lower() for x in l[0]]
    a[-1] = a[-1][:-1]

    try:
        header_field_index = a.index(s)
        return header_field_index
    except: return -1

def get_by_id_sort_by_date(l, id):
    a = [x.lower() for x in l[0]]
    a[-1] = a[-1][:-1]

    try:
        id_field_index = a.index('id')
        date_field_index = a.index('дата сделки')
    except: return []

    def get_date_column(l):
        return l[date_field_index]

    id_item_list = []

    for i in l[1:]:
        if i[id_field_index] == id:
            id_item_list.append(i)

    id_item_list.sort(key = get_date_column)

    id_item_list.insert(0, l[0])

    return id_item_list


