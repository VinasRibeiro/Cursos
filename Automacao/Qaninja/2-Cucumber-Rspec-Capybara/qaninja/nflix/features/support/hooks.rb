require "report_builder"
require "date"

Before do
    @login_page = LoginPage.new
    @movie_page = MoviePage.new
    @sidebar = SideBarView.new

    # page.driver.browser.manage.window.maximize
    page.current_window.resize_to(1440,900)
end

Before("@login") do
    user = CONFIG["users"]["cat_manager"]
    @login_page.go
    @login_page.with(user["email"], user["pass"])
end

After do |scenario|
    #if scenario.failed?
    temp_shot = page.save_screenshot("log/temp_shot.png")
    screenshot = Base64.encode64(File.open(temp_shot,'rb').read)
    attach(screenshot, "image/png")    
    #end
end
#A função embed esta depreciada, Agora esta usando o attach(file ,media_type)

d = DateTime.now
@current_date = d.to_s.tr(":", "-")


#A função at_exit só vai executar no final de todos os testes
#O ReportBuilder é uma gem que gera uma visualização mais completa do resultado dos testes
 at_exit do
    ReportBuilder.configure do |config|
        config.input_path = 'log/report.json'
        config.report_path = 'log/' + @current_date
        config.report_types = [:retry, :html]
        config.report_title = 'Ninjaflix WebApp'
        config.compress_image = true
        config.additional_info = {"App" => "web", "Data de execução" => @current_date}
        config.color = "indigo"
    end
    ReportBuilder.build_report
end