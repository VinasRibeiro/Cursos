import 'dart:io';

void main() {
    print("Qual o seu nome? ");
    var nome = stdin.readLineSync();
    print("Bem vindo $nome");
}