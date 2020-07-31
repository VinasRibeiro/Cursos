class AvengersHeadQuarter
  attr_accessor :list

  def initialize
    self.list = []
  end

  def put(avenger)
    self.list.push(avenger)
  end
end

# TDD (Desenvolvimento guiado por testes)

describe AvengersHeadQuarter do
  it "deve adicionar um vingador" do
    hq = AvengersHeadQuarter.new
    hq.put("Spiderman")
    #Abaixo tem duas formas de se comparar com uma string
    expect(hq.list).to eql ["Spiderman"]
    expect(hq.list).to include "Spiderman"
  end

  it "deve adicionar uma lista de vingadores" do
    hq = AvengersHeadQuarter.new
    hq.put("Thor")
    hq.put("hulk")
    hq.put("Spiderman")

    hq.list.size > 0
    res = hq.list.size > 0
    # a prorpiedade size só funciona com listas

    expect(hq.list.size).to be > 0
    expect(res).to be true
  end

  it "thor deve ser o primeiro da lista" do
    hq = AvengersHeadQuarter.new

    hq.put("Thor")
    hq.put("hulk")
    hq.put("Spiderman")

    expect(hq.list).to start_with("Thor")
  end

  it "Ironman deve ser o ultimo da lista" do
    hq = AvengersHeadQuarter.new

    hq.put("Thor")
    hq.put("hulk")
    hq.put("Spiderman")
    hq.put("Ironman")

    expect(hq.list).to end_with("Ironman")
  end

  it "deve conter o sobre nome" do
    avenger = "Peter Parker"

    expect(avenger).to match(/Parker/)
    expect(avenger).not_to match(/Papito/)
  end
end
