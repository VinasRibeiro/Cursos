=begin
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, 
sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
=end


puts 'Quantos dias você ficou com o carro?:'
dias = gets.chomp.to_i

puts 'Quantos KM você utilizou?: '
KM = gets.chomp.to_f

pago = (dias*60)+ (KM*0.15)
puts "A diaria de #{dias} dias, custou R$#{dias*60}"
puts "Os #{KM}Km utilizados, custou R$#{KM*0.15}"
puts "No total ficou #{pago}"