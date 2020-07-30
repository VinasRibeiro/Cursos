//Faça um programa que leia u número e mostre na tela o seu sucessor e seu antecessor.
import 'dart:io';

void main (){


  print ('Digite um número: ');
  int n = int.parse(stdin.readLineSync());
  
  print ('O sucessor é: ' + (n +1).toString());
  int n2 = n - 1;
  print ('O antecessor é: ' + n2.toString());


}