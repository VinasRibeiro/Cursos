/*

Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

*/

import 'dart:io';

import 'dart:math';


void main(){


  var nomes = [];
  var v = [];
  
  
  print ('Insira os nomes para o sorteio');

  for(int i =0; i <= 4; i++ ){
    
    nomes.add(stdin.readLineSync());
    
    
  }
  
 
print ('Os nomes são: $nomes');
print ('O nome sorteado foi ' + (nomes[new Random().nextInt(4)]));


}
