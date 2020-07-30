/*

Crie um programa que leia o nome completo de uma pessoa e mostre:
>O nome com todas as letras maiúsculas e minúsculas.
>Quantas letras ao todo (sem considerar espaços).
>Quantoas letras tem o primeiro nome.

nome = 'vinicius rodrigues ribeiro'

nomesplit = nome.split

print "#{nomesplit} \n"
print nomesplit.join(" ")

No caso do dart o split precisa de parametros, ele remove

*/
import 'dart:io';

void main(){


print ('Digite seu nome completo: ');
var nome = stdin.readLineSync();

print ('Seu nome em maiusculo: ' + nome.toUpperCase());
print ('Seu nome em minusculo: ' + nome.toLowerCase());
print ('Seu nome tem ao todo: ' + nome.split(' ').join().length.toString());
print ('Seu primeiro nome é ' + nome.split(' ')[0] + ' e ele tem ' + nome.split(' ')[0].length.toString() + ' Letras ');

}