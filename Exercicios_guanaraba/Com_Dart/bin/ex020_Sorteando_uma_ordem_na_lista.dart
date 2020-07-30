/* 
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos 
dos alunos.  
Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
*/
import 'dart:io';
import 'dart:math';

void main (){

var nomes = [];

print ('Insira os nomes');
for (var i=0; i <=4; i++){

  nomes.add(stdin.readLineSync());

}

print ('Os nomes são: ' + nomes.toString());
nomes.sort();
print ('Organizando com sort: ' + nomes.toString());
nomes.shuffle();
print ('Embaralhando usando shuffle: ' + nomes.toString());

/*
Para usar as funções sort e shuffle o dart altera a variavél lista nomes
não sei se é possivél inserir junto do print, mas desta forma funciona.

Para atribuir uma lista em outra segue o exemplo abaixo.

List nomes2 = nomes;

A lista nomes2 ficou com a ultima organização, no exemplo acima foi feito pelo shuffle.
*/




}
