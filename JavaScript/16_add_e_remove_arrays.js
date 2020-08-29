// Javascript Adicionando elemento em array

const numeros = [1,2,3];

//inserindo no iniico
//unshift empurra os numeros para direita e insere no inicio
numeros.unshift(0);
console.log(numeros);


//Inserindo no meio
//O primeiro parâmetro indica em qual indice vai ser inserido, o segundo parâmetro é um doolean 0 ou 1 se vai deletar ou não a informação no indice definido antes
//E o ultimo parâmetro é qual valor vai ser inserido.
numeros.splice(1,0,'a');
console.log(numeros);

//No final
//Insere o numero no final do array
numeros.push(5);
console.log(numeros);

//Remove no final do array
numeros.pop();
console.log(numeros);

//Remove no inicio do array
numeros.shift();
console.log(numeros);

//Remove entre o array
//Assim como no anterior, neste caso ele acha o indice 2 e remove ele.
numeros.splice(2,1);
console.log(numeros);

