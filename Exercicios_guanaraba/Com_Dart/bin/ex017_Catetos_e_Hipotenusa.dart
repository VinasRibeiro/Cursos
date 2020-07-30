/*

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
triângulo retangulo, calcule e mostre o comprimento da hipotenusa.

*/
import 'dart:io';
import 'dart:math';

void main(){

  print ('Digite o cateto oposto: ');
  double co = double.parse(stdin.readLineSync());

  print ('Digite o cateto adjacente: ');
  double ca = double.parse(stdin.readLineSync());

  double hipo = pow((pow(co, 2) + pow(ca, 2)), 0.5);

  print ('A hipotenusa é: $hipo');


}