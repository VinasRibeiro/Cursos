#Excreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

puts 'Inisira a metragem: '
metros = gets.chomp.to_f
centimetros = metros * 100
milimetros = metros * 1000


puts "#{metros}m são: #{centimetros}cm e #{milimetros}mm"