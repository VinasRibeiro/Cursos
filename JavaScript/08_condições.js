
console.log("Usando if ---------------------------------------------------------------------------")
let hora = 10;

if (hora > 6 && hora < 12){
    console.log("Bom dia");

}
else if (hora > 12&& hora < 18) {
    console.log("Boa tarde");
}
else {
    console.log("Boa noite");
}

console.log("Usando switchcase ---------------------------------------------------------------------")

let permissao;

switch(permissao){
    case 'Comum':
        console.log('Usuario Comum');
    break;

    case 'Gerente':
        console.log('Usuario Gerente');
    break;

    case 'Diretor':
        console.log('Usuario Diretor');
    break;

    default:
        console.log('Usuário não reconhecido');

}