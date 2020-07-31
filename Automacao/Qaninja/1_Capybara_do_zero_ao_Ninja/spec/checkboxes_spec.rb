describe "Caixas de seleção", :checkbox do
  before(:each) do
    visit("https://training-wheels-protocol.herokuapp.com/checkboxes")
  end

  it "marcando uma opção" do
    check("thor")
  end

  it "desmarcando uma opção" do
    uncheck("antman")
  end

  it "marcando com find set true" do
    find("input[value=cap]").set(true)
  end

  it "desmarcando com find set false" do
    find("input[value=guardians]").set(false)
  end

  after(:each) do
    sleep 3
  end
end

#Você pode usar tanto o id como o name para marcar as seleções
#o before(:each) executa um codigo antes de cada it criado
#o after(:each) executa um código após a execução de cada it
