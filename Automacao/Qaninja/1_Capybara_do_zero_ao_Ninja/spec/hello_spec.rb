describe "Meu primeiro script" do
  it "Visitar a pagina " do
    visit "https://training-wheels-protocol.herokuapp.com/"
    puts page.title
    expect(page.title).to eql "Training Wheels Protocol"
  end
end

#O comando visit e page.title são do capybara e o comando expect são do rspec
#
