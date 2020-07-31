describe "Upload", :upload do
  before(:each) do
    visit "https://training-wheels-protocol.herokuapp.com/upload"
    @arquivo = Dir.pwd + "/spec/fixtures/teste.txt"
    @imagem = Dir.pwd + "/spec/fixtures/noct.jpg"
  end

  it "upload com arquivo texto" do
    attach_file("file-upload", @arquivo)
    click_button "Upload"

    div_arquivo = find("#uploaded-file")
    expect(div_arquivo.text).to eql "teste.txt"
  end

  it "upload com arquivo texto" do
    attach_file("file-upload", @imagem)
    click_button "Upload"

    img = find("#new-image")
    expect(img[:src]).to include "noct.jpg"
  end

  after(:each) do
    sleep 2
  end
end
