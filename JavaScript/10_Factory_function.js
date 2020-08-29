const celular = {
    marcaCelular : 'ASUS',
    tamanhoTela : {
        vertical : 155,
        horizontal : 75
    },
    capacidadeBateria: 5000,
    ligar : function(){
        console.log("Fazendo ligação...")
    }
}

//Javascript Aula 34 - Factory Functions (Função de Fábrica)

function criarCelular(marcaCelular, tamanhoTela){
    return {
        //Geralmente um objeto precisa de chave valor, mas no java script como a chave e o valor tem o mesmo nome 
        //podemos deicxar só 1 nome.
        //antes seria assim marcaCelular : marcaCelular
        //Assim como function igual o exemplo acima esta diferente do de baixo
        //E isso funciona normalmente.
        marcaCelular,
        tamanhoTela,
        capacidadeBateria,
        ligar(){
            console.log("Fazendo ligação...")
        }
    }
}

const celular1 = criarCelular('Zenfone', 5.5, 5000);
console.log(celular1);