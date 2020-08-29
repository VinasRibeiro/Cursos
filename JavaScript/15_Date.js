const data1 = new Date();
const data2 = new Date('March 06 2019 09:30');
const data3 = new Date(20119,03, 06, 9, 30);
//No caso o mês vai aparecer abriil porém o numero do mês é 3, porque o jaca script começa a partir do zero
//Ou seja mês 00 é janeiro, 01 fevereiro, 02 Março, 03 Abril

date3.setFullYear(2030);

data2.toDateString();
//Transforma a data em string

data2.toTimeString();
//Ee transforma a data e a hora local em string

data2.toISOString();
//Ele transforma em um formato usado para armazenar em servidor.