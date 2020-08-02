#O get_token é um comando que vem do helpers

Quando('faço login com {string} e {string}') do |email, password|
   @login_page.go
   @login_page.with(email,password)    
end

Então('devo ser autenticado') do    
    expect(get_token.length).to be 147
end

Então('devo ver {string} na área logada') do |expect_name|
    expect(@sidebar.logged_user).to eql expect_name
end

Então('não devo ser autenticado') do
    js_script = 'return window.localStorage.getItem("default_auth_token");'
    token = page.execute_script(js_script)
    expect(get_token).to be nil
end

Então('devo visualizar a mensagem de alerta {string}') do |expect_message|
    expect(@login_page.alert).to eql expect_message
end