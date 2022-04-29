def csv_text_to_list(s: str):
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