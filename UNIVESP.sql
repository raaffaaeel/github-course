
UNIVESP 

Portal Univesp
Usuario: 2008700@aluno.univesp.br
Senha: @Cruze2014

COORDENADORA > GABRIELA 

MONITORA > DANIELE

AULAS PRESENCIAL TODA QUINTA FEIRA AS 18:00.

CTRL SHIFT N = GUIA ANONIMA.


================================================================================


(Segue meu Desafio semana 2)

Programa Declaração_de_Imposto_de_Renda

Var
basecalculoinss: real;
aliquota: real;
dependentes: inteiro;
salario: real;
deducao: real;
calculodependente: real;
Inicio
ESCREVA ("NÚMEROS DE DEPENDENTES:");
LER dependentes;
ESCREVA ("VALOR DO SEU SÁLARIO: ");
LER salario;
calculodependente = dependentes * 189,59;
deducao = salario - calculodependente;

--Contribuição cálculo do INSS
SE deducao <= 1045,00 ENTÃO
basecalculoinss = deducao * 0,075;
ESCREVA (" VALOR DE CONTRIBUIÇÃO ",basecalculoinss);

SE 1045,01 => deducao <=  2089,60 ENTÃO
basecalculoinss = deducao * 0,090;
ESCREVA (" VALOR DE CONTRIBUIÇÃO",basecalculoinss);

SE 2089,61 => deducao <=  3134,40 ENTÃO
basecalculoinss = deducao * 0,12;
ESCREVA (" VALOR DE CONTRIBUIÇÃO",basecalculoinss);

SENÃO
basecalculoinss = deducao * 0,014;
ESCREVA (" VALOR DE CONTRIBUIÇÃO",basecalculoinss);

--Cálculo de Alíquotas
SE deducao <= 1903,99 ENTÃO
ESCREVA (" ISENTO ");

SE 1903,99 > deducao <=  2826.65 ENTÃO
aliquota = deducao * 0.075;
ESCREVA (" VALOR DE ALIQUOTA A SER PAGA:",aliquota);

SE 2089,66 > deducao <=  3751.05 ENTÃO
aliquota = deducao * 0.15;
ESCREVA (" VALOR DE ALIQUOTA A SER PAGA:",aliquota);

SE 3751.06 > deducao <=  4664.68 ENTÃO
aliquota = deducao * 0.225;
ESCREVA (" VALOR DE ALIQUOTA A SER PAGA:",aliquota);

SENÃO
aliquota = deducao * 0.275;
ESCREVA (" VALOR DE ALIQUOTA A SER PAGA:",aliquota);

FIM SE

FIM

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

Algoritmo Imposto de Renda
Variáveis
 irpf, inss, salarioBruto, salarioBase: real
 numDependentes: inteiro
Início
 // primeira parte, cálculo do salário base
 Escreva (“Informe seu salário bruto: “);
 Leia (salarioBruto);
 Escreva (“Informe o número de dependentes: “);
 Leia (numDependentes);
 Se salarioBruto <= 1.045,00 entao
    inss = salarioBruto * 0,075;
 Senao se salarioBruto <= 2.089,60 entao
    inss = salarioBruto * 0,09;
 Senao se salarioBruto <= 3.134,40 entao
    inss = salarioBruto * 0,12;
 Senao 
    inss = salarioBruto * 0,14;
 Fim_se
 salarioBase = salarioBruto – inss – (numDependentes * 189,59);

 // segunda parte, cálculo do IRPF
 Se salarioBase < 1.903,99 entao
    Escreva(“Você está isento”);
    irpf = 0;
 Senao se salarioBase <= 2.826,65 entao
    irpf = salarioBase * 0,075 - 142,80;
 Senao se salarioBase <= 3.751,05 entao
    irpf = salarioBase * 0,15 - 354,80;
 Senao se salarioBase <= 4.664,68 entao
    irpf = salarioBase * 0,225 - 636,13;
 Senao
    irpf = salarioBase * 0,275 - 869,36;
 Fim_se
 Escreva (“Valor Mensal do IRPF: “, irpf);
Fim_algoritmo 

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


