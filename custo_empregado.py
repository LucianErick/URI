salario_base = float(raw_input())
dias = int(raw_input())
transporte= float(raw_input())

transporte_total = transporte * dias
transporte_percent = (transporte_total / salario_base) * 100

if transporte_percent <= 6:
    transporte_patrao = 0
    transporte_funcionario = 0
else:
    transporte_funcionario = salario_base * 0.06
    transporte_patrao = transporte_total - transporte_funcionario

fgts_patrao = salario_base * 0.08
inss_patrao = salario_base * 0.12

if salario_base <= 1317.07:
    inss_funcionario = salario_base * 0.08
elif 1317.07 < salario_base <= 2195.12:
    inss_funcionario = salario_base * 0.09
else:
    inss_funcionario = salario_base * 0.11


despesas_funcionario = inss_funcionario + transporte_funcionario
salario_liquido = salario_base - despesas_funcionario
despesas_patrao = transporte_patrao + fgts_patrao + inss_patrao + salario_base

print 'O salário base é R$ %.2f' % salario_base
print 'O custo mensal para o empregador é de R$ %.2f' % despesas_patrao
print 'O salário líquido que o trabalhador irá receber no mês é R$ %.2f' % salario_liquido
