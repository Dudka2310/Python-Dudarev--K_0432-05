print ('Введите произвольное число:')
chislo = float(input())
print ('Введите пограничное число:')
granica = float(input())
if chislo < granica:
    print ('первое число {} меньше пограничного {}'.format (chislo, granica))
elif chislo > granica:
    print ('первое число {} больше пограничного {}'.format (chislo, granica))
    if (granica * 3) == chislo:
        print ('первое число {} больше пограничного {} ровно в три раза'.format (chislo, granica))
    elif (granica * 3) < chislo:
        print('первое число {} больше пограничного {} более чем в три раза'.format (chislo, granica))
else:
    print ('первое число как-то относится к пограничному, однако данное отношение не описано в условиях задачи')
