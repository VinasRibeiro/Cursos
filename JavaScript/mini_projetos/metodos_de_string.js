//Metodos de String
//Tipo primitivo
const mensagem = ' minha primeira mensagem ';
//tipo objeto
const outraMensagem = new String('bom dia');

//Internamente o tipo string é um objeto para o java script
//Assim você tem a opção de usar alguns metodos para manipular esta string

//O length retorna a quantidade de caracteres da string
console.log(outraMensagem.length);

//Retorna o caracter na posição 2 do array de caracteres ou seja na terceira posição real.
console.log(outraMensagem[2]);

//Verifica se a string em questão esta dentro da variável e retorna true ou false
console.log(mensagem.includes('vermelho'));

//Verifica se começa com a string minha e retorna true ou false
console.log(mensagem.startsWith('minha'));

//Verifica se termina com a string minha e retorna true ou false
console.log(mensagem.endsWith('mensagem'));

//Qual indice começa a palavra primeira.
console.log(mensagem.indexOf('primeira'));

//Substitui uma palavra por outra.
console.log(mensagem.replace('minha', 'sua'));

//Remove espaços no inicio e no fim
console.log(mensagem.trim());

//Separa as palavras
console.log(mensagem.split(' '));