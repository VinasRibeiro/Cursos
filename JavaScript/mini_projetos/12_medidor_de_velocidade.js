verificarVelocidade(74);

function verificarVelocidade(velocidade){

    const velocidadeMaxima = 70;
    const kmPorponto = 5;
    const pontosMaximo = 12;
    
    if (velocidade === velocidadeMaxima){
        console.log("Você esta no limite de velocidade");
    }
    if (velocidade < velocidadeMaxima){
        console.log("Você esta abaixo do limite")
    }
    if(velocidade > velocidadeMaxima){
        const pontos = Math.floor(((velocidade - velocidadeMaxima) / kmPorponto))
        if(pontos >= 1){
            console.log("Você passou do limite e recebeu " + pontos + " pontos")
        }
        else{
            console.log("Você passou do limite de velocidade cuidado")
        }

        if(pontos >= pontosMaximo)
            console.log("Carteira suspendida")
        
    }
    
}