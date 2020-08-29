//Javascript Aula 36 - Natureza dinâmica de Objetos
//Os objetos em javascript pode receber mais atributos ao longo do programa

const mouse = {
    cor : 'red',
    marcar : 'dazz'
}
console.log(mouse)

console.log("Acrecentando atributo e função ao objeto");
mouse.velocidade = 5000;
mouse.trocaDPI = function (){
    console.log(' mudando DPI ');
}
console.log(mouse);


console.log("Removendo atributo e função do objeto");
delete mouse.velocidade;
delete mouse.trocaDPI;

console.log(mouse);