//Javascript encontrando elementos(primitivos)

const numeros = [1,2,3,4];

//indexof retorna o index do valor passado
//Caso ele não encontre ele retorna -1 indicando que não foi encontrado
console.log(numeros.indexOf(1));

//lastIndexOf, caso tenha valores repitidos no array ele retorna o indice do ultimo valor do array
console.log(numeros.lastIndexOf(1));


//No EC6 o includes retorna Boolean se existe o valor dentro do array
console.log(numeros.includes(2));