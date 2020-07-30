#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raizquadrada.

puts 'Insira um numero: '
numero = gets.chomp.to_i

puts "O dobro dele é: #{numero*2}"
puts "O triplo dele é: #{numero*3}"

if numero >= 0
    puts "A raiz quadrada de #{numero} é #{numero**0.5}"
    puts "Usando metodo sqrt a raiz de #{numero} é #{Math.sqrt(numero)}"
else
    puts'Não pode ser um numero menor ou igual a 0'
end