=begin

Faça um programa que leia um ângulo qualquer e mostre na tela o valor 
do seno, cosseno e tangente desse ângulo.

=end
angulo = gets.chomp.to_f

angulo = (angulo/180 * Math::PI)

puts "Seno :#{Math.sin(angulo).truncate(2)}"

puts "Cosseno :#{Math.cos(angulo).truncate(2)}"

puts "Tangente :#{Math.tan(angulo).truncate(2)}"

