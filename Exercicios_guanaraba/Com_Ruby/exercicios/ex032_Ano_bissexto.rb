=begin

Faça um programa que leia um ano qualquer e mostre se ele pe bissexto.

=end

puts "Insira o ano para analisar: "
ano = gets.chomp.to_i

if ano % 4 == 0 && ano % 100 != 0 || ano % 400 == 0
  puts "O ano #{ano} é Bissexto"
else
  puts "O ano #{ano} não é Bissexto"
end
