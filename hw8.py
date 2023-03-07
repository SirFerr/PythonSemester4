import re


def main(input_str):
    result = []
    matches = re.findall(r'\s*(\w+)\s*:=\s?#\s*\((.*?)\)',
                         input_str.replace("\n", " "))
    for match in matches:
        name = match[0]
        values = [val.strip() for val in match[1].split(',')]
        result.append((name, values))

    return result


data3 = "<block> make atcear:=#( ondi_647 ,soaed_831,enrige_585). " \
        "make\nrerere_785 :=#( geisma_933 ,atques ). make eslara :=#(" \
        "leonla_722,\nmaarile , tira_89, arre ). </block>"

test4 = '<block> make atcear:=#( ondi_647 ,soaed_831,enrige_585). ' \
        'make\nrerere_785 :=#( geisma_933 ,atques ). make eslara :=#(' \
        'leonla_722,\nmaarile , tira_89, arre ). </block>'

test5 = '<block> make anteza :=#(lexeis_454 , ened , arin_164 ). make ' \
        'lezate:=\n#( edla_483, tiarqu, anri_623 ). make lequer := #( onsoan ' \
        '' \
        '' \
        '' \
        '' \
        '' \
        '' \
        ', geerti_90\n, enatce ). make orleat := #( isso_806 , cerebe ). ' \
        '</block>'
result1 = main(test5)

print(result1)
