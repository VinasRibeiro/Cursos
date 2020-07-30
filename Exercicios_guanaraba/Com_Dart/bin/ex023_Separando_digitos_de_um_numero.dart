/*

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número: 1834
unidade: 4 dezena:3 centena:8 milhar:1

*/

import 'dart:io';

void main (){

print ('Insira um numero até 999:');

int numero = int.parse(stdin.readLineSync());

//este calculo retorna um valor com .0 e precisa ser armazenado em um double
int u = (numero / 1 % 10).truncate();
int d = (numero / 10 % 10).truncate();
int c = (numero / 100 % 10).truncate();

print ("A unidade é $u a dezena é $d a centena $c.");




}