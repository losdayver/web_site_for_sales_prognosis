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

def get_line(l):
    rows_count = len(l)-1

    c_index = get_header_index(l, 'количество проданного')

    s_index = get_header_index(l, 'цена продажи')

    if rows_count == 1:
        return []

    c1 = 0
    s1 = 0
    for r in l[1:rows_count//2]:
        c1 += int(r[c_index])
        s1 += int(r[s_index])


    c2 = 0
    s2 = 0
    for r in l[rows_count // 2:]:
        c2 += int(r[c_index])
        s2 += int(r[s_index])


    return [s1/(rows_count//2), c1/(rows_count//2), s2/(rows_count - rows_count//2), c2/(rows_count - rows_count//2)]

def get_interpolation(line):
    if len(line) <= 1: return 'недостаточно данных для составления прогноза'

    slope = (line[1] - line[3]) / (line[0] - line[2])

    return '(Спрос) = '+str(slope)+'*(Цена продажи)'



