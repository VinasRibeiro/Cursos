=begin

Escreva um programa que pergunte o salário de um funcionário e 
calcule o valor do seu auento.
Para salário superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

=end

puts "Insira o salário: "
salario = gets.chomp.to_f

if salario <= 1250
  salario = salario + (salario * 15 / 100)
else
  salario = salario + (salario * 10 / 100)
end

puts "Seu novo salário é #{salario}"
