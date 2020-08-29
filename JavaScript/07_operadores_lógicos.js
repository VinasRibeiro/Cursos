console.log("Aritiméticos");
//Aritiméticos(Matemáticos)
// + - * / **
let salario = 6;
console.log(salario + salario);
console.log(salario - salario);
console.log(salario * salario);
console.log(salario / salario); 
console.log(salario ** salario); //Potência

// ++ --
let idade = 18;

//tudo isso vale para -- também
console.log(idade);
console.log(++idade);
console.log(idade);// o ++ faz o incremento e altera a variável
console.log(idade++);// o ++ depois faz o incremento depois de exibir a variável.
console.log(idade);



console.log('----------------------------------------------------------------------------------------')
console.log("Atribuição");
//Atribuição

// = += -=
let valor = 100;

// Esta expressão é igual a fazer isto:  valor = valor + valor
valor += valor;
console.log(valor);


console.log('----------------------------------------------------------------------------------------')
console.log("Comparação ou igualdade");
//Comparação
//Aqui ele compara o valor e o tipo da variável
console.log( 1 === 1);
console.log('1'=== 1);

//igualdade solta
//Aqui ele compara só o valor, internamente ele converte os tipo para serem comparados.
//Mas não é uma boa prática usar desta forma.
console.log(1 == 1);
console.log('1' == 1);


console.log('----------------------------------------------------------------------------------------')
console.log("Operador Ternário");
//Operador ternário
//Aqui ele faz uma verificação usando o > para maior que e o retorno vem depois do ? usando o : para separação de duas alternativas
//Após isso ele atribui o resultado a variável tipo
let pontos = 101;
let tipo = pontos > 100? 'premium' : 'comum';
console.log(tipo)


console.log('----------------------------------------------------------------------------------------')
console.log("Operador Lógicos");
//Operadores Lógicos


//Operador Lógico e &&
//Retorna true se os dois forem true
console.log("--- && ----");
console.log(true && true);
console.log(false && true);

//Operador lógico ou ||
console.log("--- || ----");
console.log(true || true);
console.log(false || true);

//Operador lógico de negação NOT  !

console.log("--- ! ----");
candidato = true;
console.log(candidato);
console.log(!candidato);




console.log('----------------------------------------------------------------------------------------')
console.log("Operador Lógicos não boleanos");
//Bitwise
//Falsy
//São undefined, null, 0, false, '', NaN - Not a number

//Truthy
//Retorna true quando o elemento comparado não é um valor da lista dos Falsy
//Exemplo false || 'vinicius', vai retornar a string vinicius.
console.log(false || 'vinicius');
console.log(false || 1);
console.log(false || 1 || 3); //O java script só considera o primeiro operador ||

//Outro exemplo
let corPersonalizada = 'Vermelho';
let corPadrão = 'azul';
let corPerfil = corPersonalizada || corPadrão;
console.log(corPerfil);
// Aqui ele mostra vermelho por que o || só precisa que a primeira seja verdadeira.
// No caso é uma string não vazia então retorna true e ele exibe a primeira variável

let corPersonalizada2 = '';
let corPadrão2 = 'azul';
let corPerfil2 = corPersonalizada2 || corPadrão2;
console.log(corPerfil2);
// Aqui ele mostra azul por que a string esta vazia, considerando false
