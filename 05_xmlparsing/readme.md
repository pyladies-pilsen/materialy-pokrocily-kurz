# Zadání

by Adam Jaško

Kompletní data jsou ke stažení [zde](https://drive.google.com/drive/folders/1DUX3I93fABYRMwKeRjYOw4yqC7GcG5K8?usp=sharing)

- každý katalogizační záznam začíná řádkem `<record>`
- každé pole je uvozeno řetězcem `<datafield tag ...>`
- upravovaná pole

## Úkol pro pole 700:
- je-li obsaženo pole 700 v tomto znění a současně chybí 
```xml
<datafield tag="700" ind1="1" ind2="#">
 <subfield code="a">Klácel, František Matouš,</subfield>
 <subfield code="d">1808-1882</subfield>
 <subfield code="7">jk01060239</subfield>
 <subfield code="4">fmo</subfield>
</datafield>
```

a současně chybí řetězec:
 `<subfield code="5">CZ-PrNMA</subfield>`

nahraď celý blok s polem 700 tímto blokem:
```xml
<datafield tag="700" ind1="1" ind2="#">
 <subfield code="a">Klácel, František Matouš,</subfield>
 <subfield code="d">1808-1882</subfield>
 <subfield code="7">jk01060239</subfield>
 <subfield code="4">fmo</subfield>
 <subfield code="5">CZ-PrNMA</subfield> # PŘIDÁNÍ TOHOTO ŘÁDKU NA TUTO POZICI
</datafield>
```



## Úkol pro pole 650:
- je-li obsaženo pole 650 v tomto znění:

```xml
<datafield tag="650" ind1="0" ind2="4">
<subfield code="a">dějiny středověké</subfield> # ZDE MŮŽE BÝT LIBOVOLNĚ DLOUHÝ ŘETĚZEC
</datafield>  
```
a současně v něm chybí tento řetězec:

```xml
<subfield code="2">czenas</subfield>
```
vrať celý blok s polem 650 v tomto znění:

```xml
<datafield tag="650" ind1="0" ind2="4">
<subfield code="a">středověk</subfield>
<subfield code="2">czenas</subfield> # PŘIDÁNÍ TOHOTO ŘÁDKU NA TUTO POZICI
</datafield>
```

## Úkol pro pole 020:
- výsledkem bude odmazání části řádku a přidání nového
- bude zpravidla ve formátu 13 členného řetězce, mezera, řetězec v závorce:
	- buď (váz.) nebo (brož.) - může nastat více případů
	- výsledkem má být nahrazení tohoto bloku:

```xml
<datafield tag="020" ind1="#" ind2="#">
 <subfield code="a">80-7185-773-4 (váz.)</subfield> # KDYŽ JE OBSAŽENO (VÁZ.)
</datafield>
```

- blokem tímto:
```xml
<datafield tag="020" ind1="#" ind2="#">
 <subfield code="a">80-7185-773-4</subfield> # ZDE SE ODMAŽOU VŠECHNY ZNAKY ČTENO ODPRAVA AŽ PO PRVNÍ ČÍSLO (poslední smazaný znak je mezera)
 <subfield code="q">(vázáno)</subfield> # NOVĚ PŘIDANÝ ŘÁDEK
</datafield>
```
 
- je-li v závorce v původním řetězci (brož.), do nově vytvořené řádky přidat (brožováno)
