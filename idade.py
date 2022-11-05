age = int(input('Digite a sua idade em dias: '))
years = age // 365
months = (age % 365)//30
days = (age % 365) % 30
print('Você tem: ' + str(years) + ' anos, ' + str(months) + ' meses e ' + str(days) +' dias')