=begin

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A apresentação mensal, não pode exceder 30% do salário ou então o empréstimo será
negado.

=end

puts "Quanto você ganha por mês? "
salario = gets.chomp.to_f

puts "Qual o valor das casa? "
casa = gets.chomp.to_f

puts "Quantos anos de financiamento "
prazo = gets.chomp.to_i

prestação = casa / (prazo * 12)

if prestação > salario / 100 * 30
  puts "Seu crédito não foi aprovado"
else
  puts "Seu crédito foi aprovado"
end

puts "O valor de prestação é #{prestação}"
