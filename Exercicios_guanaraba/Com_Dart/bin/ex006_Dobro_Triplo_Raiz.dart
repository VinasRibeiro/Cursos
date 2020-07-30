//Crie u algoritmo que leia um número e mostre o seu dobro, triplo e raizquadrada.
import 'dart:io';

import 'dart:math';

void main (){

print ('Insira um numero: ');
int numero = int.parse(stdin.readLineSync());

print ('O brodro é: ' + (numero*2).toString());
print ('O brodro é: ' + (numero*3).toString());
print ('A raiz quadrada é: ' + sqrt(numero).toString());



}