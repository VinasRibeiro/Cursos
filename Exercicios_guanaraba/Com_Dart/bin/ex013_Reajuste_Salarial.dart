//Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15%
//de aumento.
import 'dart:io';

void main(){

  print ('Insira o seu salário: ');
  double salario = double.parse(stdin.readLineSync());
  double novosal= salario + (salario * 15 /100);
  print ('Seu salário com 15% de aumento foi para: $novosal');


}