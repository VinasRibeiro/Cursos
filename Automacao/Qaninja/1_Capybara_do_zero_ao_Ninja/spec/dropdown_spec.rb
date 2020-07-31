describe "Caixa de opções", :dropdown do
  it "item especifico simples" do
    visit "https://training-wheels-protocol.herokuapp.com/dropdown"
    select("Loki", from: "dropdown")
    sleep 3
  end

  it "item esecifico com o find" do
    visit "https://training-wheels-protocol.herokuapp.com/dropdown"
    drop = find(".avenger-list")
    drop.find("option", text: "Scott Lang").select_option
    sleep 3
  end

  #Este exemplo tra todas as opções contidas em um dropbox e insere em um array
  #Depois ele sortea um elemento do dropbox e seleciona ele.
  it "qualquer item", :sample do
    visit "https://training-wheels-protocol.herokuapp.com/dropdown"
    drop = find(".avenger-list")
    drop.all("option").sample.select_option
    sleep 3
  end
end
