sal = float(input('Digite o salário: R$'))
if(sal >= 1250):
    aum = (10/100)    
else:
    aum = (15/100)
sal_f = sal + (sal*aum)
print('O salário de R${:.2f} passa a ser R${:.2f}'.format(sal, sal_f))