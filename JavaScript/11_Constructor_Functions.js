// CamelCase umDoisTresQuatro
function criarCelular(marcaCelular, tamanhoTela, capacidadeBateria){
    return{
        marcaCelular,
        tamanhoTela,
        capacidadeBateria,
        ligar(){
            console.log("Fazendo ligação...")
        }
    }
}

//Pascal Case - UmDoisTresQuatro
function Celular(marcaCelular, tamanhoTela, capacidadeBateria){
    this.marcaCelular = marcaCelular,
    this.tamanhotela = tamanhoTela,
    this.capacidadeBateria = capacidadeBateria,
    this.ligar = function(){
        console.log("Fazendo Ligação...");
    }

}

const celular = new Celular('asus', 5.5, 5000);
console.log(celular);

//Nesses dois exemplos mostra como dois objetos podem ser criados
//O primeiro é uma função que retorna um objeto
//O segundo é um objeto sendo criado a partir do instanciamento.
//Função construtor tem a primeira letra maiúscula