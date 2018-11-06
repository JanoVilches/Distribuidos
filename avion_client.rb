require 'grpc'
require_relative 'Aeropuerto_services_pb'


stub = Entrar::Stub.new('[::]:50051', :this_channel_is_insecure)
aviones = []
for i in 0..5
    aviones << Avion.new(aerolinea: "a", codigo_avion: i.to_s, peso: 1, combustible: 1, torre_control_inicial: "as", torre_control_destino: "asd")
end
aviones.each do |i|
    response = stub.aterrizar(i)
    puts response.espera
end
