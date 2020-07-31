describe "Alertas de JS", :alerts do
  before(:each) do
    visit "https://training-wheels-protocol.herokuapp.com/javascript_alerts"
    sleep 1
  end

  it "alerta" do
    click_button "Alerta"
    msg = page.driver.browser.switch_to.alert.text
    puts msg
    expect(msg).to eql "Isto é uma mensagem de alerta"
  end

  it "sim confirma" do
    click_button "Confirma"

    msg = page.driver.browser.switch_to.alert.text
    expect(msg).to eql "E ai confirma?"

    page.driver.browser.switch_to.alert.accept
    expect(page).to have_content "Mensagem confirmada"
  end

  it "sim confirma" do
    click_button "Confirma"
    

    msg = page.driver.browser.switch_to.alert.text
    expect(msg).to eql "E ai confirma?"

    page.driver.browser.switch_to.alert.accept
    expect(page).to have_content "Mensagem confirmada"
  end

  it 'accept prompt', :accept_prompt do
    accept_prompt(with: 'Fernando') do
        click_button 'Prompt'
        sleep 2        
    end
    expect(page).to have_content 'Olá, Fernando'
    end

    it 'accept prompt', :dismiss_prompt do
        dismiss_prompt(with: '') do
            click_button 'Prompt'
            sleep 2        
        end
        expect(page).to have_content 'Olá, null'
        end

    
end
