Bue_rate = 3.9285
Selling_rate = 3.8507
print('Podaj czy chcesz kupić czy sprzedać dolary')
Type_of_transaction = input(' Jeśli kupić napisz [k], a jeśli chcesz sprzedac napisz [s] :')
Order = int(input('podaj ile dolarów chcesz nabyc lub sprzedać'))

if Type_of_transaction not in ('k', 's'):
    print('Nie wybrałeś właściwej opcji. Spróbuj ponownie ')
    Type_of_transaction = input(' Napisz [k] lub [s] :')

    Order = int(input('podaj ile dolarów chcesz nabyc lub sprzedać : '))
if Type_of_transaction == 'k':
    Value_of_purchase = (Order * Bue_rate)
    print(f'do zapłaty za nabycie {Order} dolarów : {Value_of_purchase:.2f} PLN')
elif Type_of_transaction == 's':
    Value_of_sales = (Order * Selling_rate)
    print(f'otrzymasz ze sprzedaży {Order} dolarów: {Value_of_sales:.2f} PLN')
else:
    print('coś pomyliłeś')
