#Este arquivo env tem todos os elementos de configuração inicial dos testes

require "capybara"
require "capybara/cucumber"
require "selenium-webdriver"
require "os"

#Este módulo possui código de auxilio
require_relative "helpers"

#O comando World faz com que o modulo helpers seja usado em qualquer lugar do projeto de teste no cucumber
#Como se fosse uma variável global, porém é um modulo global.
World(Helpers)

Capybara.configure do |config|
    config.default_driver = :selenium_chrome
    config.app_host = "http://localhost:8080"

    #Este parâmetro define um tempo limite para encontrar elementos na pagina.
    #Assim não é preciso usar sleeps
    config.default_max_wait_time=10
end