//Criar função somar que retorna a soam de todos os múltiplos de 3 e 5

//Multiplos de 3
//3, 6, 9
//Multiplos de 5
//5, 10

//Somando os multiplos
//armazenar os muitiplos de 3
//armazenar os multiplos de 5
//somar os dois

somar(10);
function somar(limite){
    let multiploDe3 = 0;
    let multiploDe5 = 0;
    for(i = 0; i <= limite; i++){
        if(i % 3 ===0)
        multiploDe3 += i;
            if(i % 5 === 0)
            multiploDe5 += i;
    }
    console.log(multiploDe3 + multiploDe5);
}