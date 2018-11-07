require 'grpc'
require './Aeropuerto_services_pb'

def regularPeso(avion)

end

class PlaneServer < Plane::Service
    
end

puts "Bienvenido al vuelo"
puts "[Avion] Nombre de la Aerolínea y número de Avion:"
name = gets.chomp
aerolinea = name.split[-1]
name = name.split[0]
puts "[Avion - #{name}]: Peso Máximo de carga [Kg]:"
peso = gets.chomp
peso = peso.to_i
puts "[Avion - #{name}]: Capacidad del tanque de combustible [L]:"
estanque = gets.chomp
estanque = estanque.to_i
puts "[Avion - #{name}]: Torre de control inicial:"
destino = gets.chomp

stub = Torre::Stub.new('destino:50051', :this_channel_is_insecure)

avion = Avion.new(aerolinea: aerolinea, codigo_avion: name, peso: peso, combustible: estanque, torre_control_destino: destino, combustibleActual: (estanque*0.5).to_i, pesoActual: (peso*0.8).to_i)

response = stub.aterrizar(avion)

puts "[Avion - #{name}]: Esperando pista de aterrizaje..."

if response.pista != 0
    puts "[Avion - #{name}]: Aterrizando en la pista #{response.pista}..."
    puts "[Avion - #{name}]: Presione enter para despegar"
    puts "[Avion - #{name}]: Ingrese destino"
    destino = gets.chomp
    avion.torre_control_destino = destino
    response = stub.gate(avion)
    puts "[Avion - #{name}]: Pasando por el Gate..."
    avion.combustibleActual = rand avion.combustibleActual..avion.combustible
    avion.pesoActual = rand (avion.peso*0.5).to_i..(avion.peso*1.5).to_i
    puts "[Avion - #{name}]: Todos los pasajeros a bordo y combustible cargado."
    puts "[Avion - #{name}]: Pasando por el Gate..."
    response = stub.despegar(avion)
    if response.estado == 0
        #server
    elsif response.estado == -1

    end    
else

end
