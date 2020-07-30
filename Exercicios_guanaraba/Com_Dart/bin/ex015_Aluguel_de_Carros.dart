/*
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por km rodado.
*/

import 'dart:io';

void main(){

  print ('Quantos dias você ficou com o carro?: ');
  double dias = double.parse(stdin.readLineSync());
  
  print ('Quantos KM você utilizou?: ');
  double km = double.parse(stdin.readLineSync());

  double pago = (dias*60) + (km*0.15);

  print ('A diaria de $dias dias, custou R\$' + (dias*60).toString());

  print ('Os $km\Km utilizados, custou R\$' + (km*0.15).toString());

  print ('No total ficou: $pago');

}