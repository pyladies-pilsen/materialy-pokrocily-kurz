#!python
# -*- coding: utf-8 -*-

__author__ = "Jakub Červinka"

import xml.etree.ElementTree as ET

# načtu si soubor do objektu
tree = ET.parse('spravne_22_650.xml')
root = tree.getroot()

# najdu si pomocí vyhledávacího xml dotazu (z dokumentace)
# všechny "datafieldy", které mají "tag='700'"
all_700s = root.findall("record/datafield[@tag='700']")

# pro každý datafield (sedmistovka)
for datafield in all_700s:
    # print(datafield)

    # získám si všechny jeho subfieldy
    # - a zároveň jejich kódy (code="...")
    all_subfields_codes = [
        sf.attrib['code']
        for sf in datafield.findall('subfield')
    ]
    print("Původní stav")
    print(f'{all_subfields_codes = }')

    # pokud v nalezených kódech není 'e'
    if 'e' not in all_subfields_codes:
        # vytvořím si nový element typu 'subfield'
        sub_elem = ET.SubElement(
            datafield,
            'subfield',
            attrib={
                'code': 'e',
                },
            )
        # nastavím mu text 'Editor'
        sub_elem.text = 'Editor'

    print("Po přidání")
    # kontorluji, že se správně přidal
    all_subfields_codes = [
        sf.attrib['code']
        for sf in datafield.findall('subfield')
        ]
    print(f'{all_subfields_codes = }')

# zapíšu hotový výsledek do souboru
tree.write('opraveno_700.xml', encoding='utf-8')
