//As funções n java script são diferentes de outras linguagems.
//A função pode alterar uma variável externa da função
//Em outras linguagems isso não acontece


//Esta função não retorna nada
let corSite = "azul";
function resetaCor(cor, tonalidade){
    corSite = cor + " " + tonalidade;
};

console.log(corSite);
resetaCor("Vermelho","Claro");
console.log(corSite);



//Esta função retorna algo
function MultiplicarPorDois(valor){
    return valor* 2;  
};

let resultado = MultiplicarPorDois(5);
console.log(resultado);