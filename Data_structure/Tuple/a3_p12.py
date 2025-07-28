# nested tuple iteration

nested_tpl = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
for tpl in nested_tpl:
    for elem in tpl:
        print(elem)
                  