const celular = {
    marcaCelular : 'ASUS',
    tamanhoTela: {
        vertical: 155,
        horizontal: 75
    },

    ligar: function (){
        console.log("Fazendo Ligação...");
    }
}

//------------------------------------------------------------
//Primeira forma de clonar objeto
const novoObjeto = Object.assign({
    bateria: 5000
},celular);

//-------------------------------------------------------------
//Segunda forma de clonar objeto
const objeto2 = {...celular};

//Exibindo os objetos ------------------------------------------
console.log(celular);
console.log(novoObjeto);
console.log(objeto2);

