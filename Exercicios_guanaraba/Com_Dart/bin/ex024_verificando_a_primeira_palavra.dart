/*

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 
'Santo'.

*/

import 'dart:io';

void main(){


  var palavra = "santo";
  print('Insira o nome completo: ');
  var user = stdin.readLineSync();
  var novonome = user.trim().split(' ')[0].toLowerCase();
  if (novonome == palavra){
    print('O primeiro nome digitado correponde com $palavra');
  }else{
    print('O primeiro nome digitado não corresponde com $palavra');
  }





}