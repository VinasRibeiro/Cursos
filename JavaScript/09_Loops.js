console.log("Usando for---------------------------------------------");
//Aqui o i é uma variável mas é comum porque representa um indice ou index.
for(let i = 0; i< 5;i++){
    console.log('Estou aprendendo!', i);
}
console.log('ao contrário');
//Também funciona ao contrário
for(let i = 5; i >= 1; i--){
    console.log('Estou aprendendo!', i);
}


console.log("Usando while---------------------------------------------");

let i = 5;
while (i >= 1){
    console.log(i)
    i--;
}

console.log("Usando Do..while---------------------------------------------");
//O while crai um loop infinito e precisa de uam condição para terminar o loop
//Ou de um break no meio dele para encerrar o loop
i = 0;
do{
    console.log("Digitando");
    i++;
}while (i < 10)

console.log("Usando Fo..in---------------------------------------------");

//O for in serve para interar sobre objetos.

const pessoa = {
    nome: 'Vinicius',
    idade: 25
};

//key-value
for(let chave in pessoa){
    console.log(chave, pessoa[chave]);

}

const cores = ['Vermelho', 'Azul', 'Verde'];

for (let indice in cores){
    console.log(indice, cores[indice])
}



//for-of
//For-of é mais usado para arrays
console.log("Usando For..of---------------------------------------------");
for(let cor of cores){
    console.log(cor);
}