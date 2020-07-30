#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

puts 'Insira o valor do produto: '
valor = gets.chomp.to_f
cdesc = valor - (valor * 5/100)
puts "O produto com 5% de desconto fica: #{cdesc}"