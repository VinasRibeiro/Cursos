// Arrarys

let familia = [26,64,53,63,53];
let familiaVarios = [true,45,'vini', 17];
let familiaVasio = [];

console.log(familia);
console.log(familia[2]);
console.log(familiaVarios);
console.log(familiaVasio);





console.log("Inserindo em um array -----------------------------------------------------");
// Javascript Adicionando elemento em array 
let numeros = [1,2,3];

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



console.log("Removendo do array --------------------------------------------------");
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

//OBS: Você pode atribuir um arrai a outra variavel porém esta variável fica vinculada a origem, se a origem for apagada ela também vai.


console.log("Esvaziando um array -------------------------------------------------");
//Esvaziando um array


numeros = [1,2,3,4,5];


//Metodo 1
console.log(numeros = []);

//Metodo 2
//Este é o masi recomendado
console.log(numeros.length = 0);

//Metodo 3
console.log(numeros.splice(0, numeros.length));




console.log("Concatenar arrays----------------------------------------------");

const primeiro = [1,2,3,4];
const segundo = [5,6,7,8];

const combinado = primeiro.concat(segundo);
console.log(combinado);

//OBS Para concatenar arrays do tipo const é necessário atribuir a outra variável ou constante

//PAra dividir um array se usa o slice
//Neste caso ele pega o indice 1 e o indice 3 menos um, é estranho mas é assim mesmo.
const cortado = combinado.slice(1,3);
console.log(cortado);


const primeiroo = [{id: 1}];
const segundoo = [4,5,6];
console.log(primeiroo.concat(segundoo));
primeiroo[0].id = 10;

const combinado2 = primeiroo.concat(segundoo);
console.log(combinado2);

//Como já dito antes, quando vc muda alguma coisa na primeira variável ela reflete nas demais variáveis 
//Qua copiaram ela, pq esse método copia só a referência da variável.


console.log("Usando operador spread ------------------------------------------------------");
// O spread é usado para distribuir os valores em um array, 
const primeirooo = [1,2,3,4];
const segundooo = [5,6,7,8];

const combinadooo = [...primeirooo,'a',...segundooo,'#'];
console.log(combinadooo);


const clonado = [...combinadooo];
console.log(clonado);


console.log("Usando foreach --------------------------------------------------------------");

//Funciona como um for para iterar entre os elementos de um array
//Porém de forma abreveada

const numeroseach = [1,2,3,4,5];

//Para iterar por todos os elementos do array
for (numero of numeroseach)
    console.log(numero);

// foreach
numeroseach.forEach(function(numero){
    console.log(numero);

})

//Pode ser usado com o metodo arrow function
numeroseach.forEach((numero) => console.log(numero))

//Pode ser usado com indice também
numeroseach.forEach((numero, indice) => console.log(numero, indice))


console.log("Combinando arrays -----------------------------------------------------------");

//O join junta todo o array e coloca um ponto entre cada um
// slug é a frase com - separadondo eles
const numerojoin = [1,2,3,4,5];
const combinadojoin = numeros.join('-');
console.log(combinadojoin);

console.log("Separando pelo espaço --------------------------------------------------");
//Aqui ele divide pelo espaço a string
const frase = "olha bem vindo ao curso";
const resultado = frase.split(' ');
console.log(resultado);



