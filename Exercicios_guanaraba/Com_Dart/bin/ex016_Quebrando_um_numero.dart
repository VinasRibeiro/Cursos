/*
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
inteira.

Ex: Digite um número: 6.127
O número 6.127 tem a inteira 6.

*/

import 'dart:io';
void main(){

  print ('Digite u número qualquer: ');
  double n = double.parse(stdin.readLineSync());
  

  print ('O numero inteiro é ' + (n).truncate().toString());


}