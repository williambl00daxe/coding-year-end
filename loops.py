# loops
for brand in ['levis','Carhart', 'wrangler']:
    for size in range(30,38,2):
        print(f'{brand} {size}')
        if size >32:
            break
        print(f'{brand}{size}')
