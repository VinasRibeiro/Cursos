//Faça um programa que converta uma temperatura digitada em °c e converta para °f
import 'dart:io';

void main(){
  
  print ('Insira o °C: ');
  double c = double.parse(stdin.readLineSync());
  print ('Insira o °F: ')  ;
  double f = double.parse(stdin.readLineSync());

  f = (c*1.8)+32;
  print ('O valor de °F é $f');
  





}
