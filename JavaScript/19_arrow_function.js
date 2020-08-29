//Arrow function

const marcas = [
    {id:1, nome:'a'},
    {id:2, nome:'b'}
];

console.log(marcas.find(function(marca){

    return marca.nome === 'a';
    
}));

//A partir do ES6 foi incluido o arrow function
console.log(marcas.find((marca) => {

    return marca.nome === 'a';
    
}));

//Caso essa função tenha apenas 1 parametro pode ser usado sem parenteses e sem chaves.
console.log(marcas.find(marca => marca.nome === 'a'));

//Tabém pode ser usado sem parâmetro, vulgo função anonima
console.log(marcas.find(() => marca.nome === 'a'));