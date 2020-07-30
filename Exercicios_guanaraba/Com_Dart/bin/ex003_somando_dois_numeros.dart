import 'dart:io';

void main() {
    print("Insira dois numeros:");
    int n1 = int.parse(stdin.readLineSync());
    int n2 = int.parse(stdin.readLineSync());
    int result = n1 + n2;
    print("A soma entre $n1 e $n2 é: $result");
    
}