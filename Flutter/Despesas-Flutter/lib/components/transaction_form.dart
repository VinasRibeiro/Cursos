import 'package:flutter/material.dart';


class TransactionForm extends StatefulWidget {


  final void Function(String, double) onSubmit;


  TransactionForm(this.onSubmit);

  @override
  _TransactionFormState createState() => _TransactionFormState();
}

class _TransactionFormState extends State<TransactionForm> {
  final titleController = TextEditingController();

  final valueController = TextEditingController();

  _submitForm() {

    final title = titleController.text;
    final value = double.tryParse(valueController.text) ?? 0;

//Este if verifica se algumas das duas variáveis estão vazias
//E usa o return para não chegar na função onSubmit
//O return funciona como uma espécie de break no while 
    if(title.isEmpty || value <= 0){
      return;
    }

    widget.onSubmit(title,value);



    //as variaveis do tipo string title e value foram substituidas por controllers
    print(titleController.text);
    print(valueController.text);
  

  }

  @override
  Widget build(BuildContext context) {
    return Card(
            elevation: 5,
            child: Padding(
              padding: const EdgeInsets.all(10),
              child: Column(
                children: <Widget>[
                  TextField(

                    controller: titleController,
                    onSubmitted: (_) => _submitForm(),
                    //O evento onchanged foi substituido por TextEditingCOntroller
                    //onChanged: (newValue) => title = newValue,
                    decoration: InputDecoration(
                      labelText: 'Título',
                    ),
                  ),
                  TextField(
                    controller: valueController,
                    onSubmitted: (_) => _submitForm(),
                    keyboardType: TextInputType.numberWithOptions(decimal: true),
                    //onChanged: (newValue) => value = newValue,
                    decoration: InputDecoration(
                      labelText: 'Valor (R\$)',
                    ),
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: <Widget>[
                      FlatButton(onPressed: _submitForm, child: Text('Nova Transação'), textColor: Colors.purple,),
                    ],
                  ),
                ],
              ),
            ),
          );
  }
}