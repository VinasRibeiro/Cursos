// Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

import 'dart:io';

void main(){


print ('Nota 1: ');
int nota1 = int.parse(stdin.readLineSync());
print ('Nora 2: ');
int nota2 = int.parse(stdin.readLineSync());

print ('A média é: ' + ((nota1 + nota2) / 2).toString());



}