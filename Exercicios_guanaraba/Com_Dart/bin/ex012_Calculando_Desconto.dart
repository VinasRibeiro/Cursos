//Faça u algoritmo que leia o preço de um produto e mostre seu novo preço, com 5%de desconto

import 'dart:io';

void main(){

  print('Insira o valor do produto: ');
  double valor = double.parse(stdin.readLineSync());
  double cdesc = valor - (valor*5/100);
  print ('O produto com 5% de desconto fica : $cdesc');



}