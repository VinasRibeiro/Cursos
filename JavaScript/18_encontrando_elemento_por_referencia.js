//Encontrando elementos do tipo referencia

const marcas = [
    {id:1, nome: 'a'},
    {id:2, nome: 'b'},
]

//Para encontrar um objeto por referência é usado o find()

const marca = marcas.find(function(marca){
    return marca.nome === 'a';
});

console.log(marca);