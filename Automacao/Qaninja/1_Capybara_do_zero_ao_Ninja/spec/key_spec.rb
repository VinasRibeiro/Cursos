describe "Teclado", :key do
  before(:each) do
    visit "https://training-wheels-protocol.herokuapp.com/key_presses"
  end

  it "enviando teclas" do
    teclas = %i[tab escape enter shift control space alt]

    teclas.each do |t|
      find("#campo-id").send_keys t
      expect(page).to have_content "You entered: " + t.to_s.upcase
      sleep 1
    end
    sleep 1
  end

  it 'enviando letras' do
    letras = %w[ a s d f g h j k l]
  
    letras.each do |l|
      find('#campo-id').send_keys l
      expect(page).to have_content 'You entered: ' + l.to_s.upcase
      sleep 1
    end
  end
end



