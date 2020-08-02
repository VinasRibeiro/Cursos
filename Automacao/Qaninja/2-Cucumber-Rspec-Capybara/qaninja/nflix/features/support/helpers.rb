module Helpers
    def get_token
        #Este timeout é o mesmo que foi setado no arquivo env
        #Este código faz um loop de acordo com o valor setado na variável Capybara.default_max_wait_time
        timeout = Capybara.default_max_wait_time
        timeout.times do
            js_script = 'return window.localStorage.getItem("default_auth_token");'
            @token = page.execute_script(js_script)
            sleep 1
        end
        @token
    end
end