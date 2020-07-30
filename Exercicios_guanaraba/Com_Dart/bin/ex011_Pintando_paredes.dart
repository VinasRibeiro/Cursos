/*

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área
de 2m quadrados.

*/

import 'dart:io';


void main(){

  print ('Insira a largura e altura da parede');
  print ('Largura: ');
  double larg = double.parse(stdin.readLineSync());
  print ('Altura: ');
  double alt = double.parse(stdin.readLineSync());

  double res = (larg*alt)/2;
  print ('Você vai precisar de $res\lt de tinta');


}