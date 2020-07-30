=begin

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

=end

a = gets.chomp.to_i
b = gets.chomp.to_i
c = gets.chomp.to_i

#Verificando o menor, partindo do pré suposto que A é o menor
menor = a
if b < a && b < c
  menor = b
end

if c < a && c < b
  menor = c
end

#Verificando o maior com partindo do pré suposto que a seja maior
maior = a

if b > a && b > c
  maior = b
end
if c > a && c > b
  maior = c
end

puts "O maior é #{maior} o menor é #{menor}"
