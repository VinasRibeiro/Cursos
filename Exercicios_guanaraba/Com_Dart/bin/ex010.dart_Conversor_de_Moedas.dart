//Faça um programa que converta sreais em dolares.
import 'dart:io';

void main(){

print ('Quanto você em na carteira?: ');

int n = int.parse(stdin.readLineSync());

double res = n / 4.5;

print ('você tem $res Dolares');

}