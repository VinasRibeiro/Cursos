/*

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno 
e tangente desse ângulo. 

*/
import 'dart:io';
import 'dart:math';
void main(){

  double angulo = double.parse(stdin.readLineSync());

  angulo = (angulo/180 * pi);

  print ('Seno :' + sin(angulo).toString());

  print ('Cosseno :' + cos(angulo).toString());

  print ('Tangente :' + tan(angulo).toString());
  

}