import 'package:flutter/foundation.dart';


class Transaction {
  final String id;
  final String title;
  final double value;
  final DateTime date;


  Transaction({
    //O decorador @required faz com que os valores que o construtor recebe sejam obrigatórios
    // as chaves entre os parenteses do construtor Transaction significa que os parametros 
    //do metodo construtor Transaction são nomeados, ou seja na hora de passar os parametros 
    //ele devem ser escrito assim, id: blablabla, title: blablabla, value: blablabla e etc...
    @required this.id,
    @required this.title,
    @required this.value,
    @required this.date,
  });


}