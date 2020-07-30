//Escreva um programa que leia um valor em metros e o exiba convertido
//em centimetros e milimetros.

import 'dart:io';

void main(){


print ('Insira a metragem');
double metros = double.parse(stdin.readLineSync());

double centrimetros = metros * 100;
double milimetros = metros * 1000;

print (metros.toString() + ' m são' + centrimetros.toString() + ' cm e ' + milimetros.toString() + ' mm');




}