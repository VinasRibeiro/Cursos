import 'package:validators/validators.dart';

void main () {

  String palavra = "TESTE";

  print ('A palavra esta vazia?: ' + palavra.isEmpty.toString());
  print('A palavra esta em Maiuscula? :' + isUppercase(palavra).toString());
  print('A palavra esta em Minuscula? :' + isLowercase(palavra).toString());



}