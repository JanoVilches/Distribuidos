require 'grpc'
require './Aeropuerto_services_pb'

def regularPeso(avion)
    sleep(avion.peso-avion.pesoActual)
    avion.pesoActual = avion.peso
end

def regularCombustible(avion)
    sleep(avion.combustible-avion.combustibleActual)
    avion.combustibleActual = avion.combustible
end

def regularAmbos(avion)
    sleep([avion.combustible-avion.combustibleActual, avion.peso-avion.pesoActual].max)
    avion.combustibleActual = avion.combustible
    avion.pesoActual = avion.peso
end


puts "Bienvenido al vuelo"
puts "[Avion] Nombre de la Aerolínea y número de Avion:"
name = gets.chomp
aerolinea = name.split[0]
name = name.split[-1]
puts "[Avion - #{name}]: Peso Máximo de carga [Kg]:"
peso = gets.chomp
peso = peso.to_i
puts "[Avion - #{name}]: Capacidad del tanque de combustible [L]:"
estanque = gets.chomp
estanque = estanque.to_i
puts "[Avion - #{name}]: Torre de control inicial:"
destino = gets.chomp

avion = Avion.new(aerolinea: aerolinea, codigo_avion: name, peso: peso, combustible: estanque, torre_control_destino: destino, combustibleActual: (estanque*0.5).to_i, pesoActual: (peso*0.8).to_i)


stub = Torre::Stub.new("#{destino}:50051", :this_channel_is_insecure)
first = true
while true
    if first
        puts "[Avion - #{name}]: Esperando pista de aterrizaje..."
        first = false
    end

    response = stub.aterrizar(avion)

    if response.pista != 0
        puts "[Avion - #{name}]: Aterrizando en la pista #{response.pista}..."
        puts "[Avion - #{name}]: Presione enter para despegar"
        puts "[Avion - #{name}]: Ingrese destino"
        destino = gets.chomp
        avion.torre_control_destino = destino
        puts "[Avion - #{name}]: Pasando por el Gate..."
        response = stub.gate(avion)
        avion.combustibleActual = rand avion.combustibleActual..avion.combustible
        avion.pesoActual = rand (avion.peso*0.5).to_i..(avion.peso*1.5).to_i
        puts "[Avion - #{name}]: Todos los pasajeros a bordo y combustible cargado."
        puts "[Avion - #{name}]: Pidiendo instrucciones para despegar..."

        response = stub.despegar(avion)
        
        if response.estado < 0
            if response.estado == -1
                puts "[Avion - #{name}]: Peso excedido, regulando peso..."
                regularPeso(avion)
            elsif response.estado == -2
                puts "[Avion - #{name}]: Falta combustible, llenando el estanque..."
                regularCombustible(avion)
            elsif response.estado == -3
                puts "[Avion - #{name}]: Peso excedido y falta combustible, regulando ambos..."
                regularAmbos
            end
            puts "[Avion - #{name}]: Pidiendo instrucciones para despegar..."
            response = stub.despegar(avion)
        end

        destino = response.destino

        if response.estado == 0
            puts "[Avion - #{name}]: Todas las pistas ocupadas están ocupadas, el avión predecesor es #{response.predecesor}..."
            while response.estado == 0
                sleep(10)
                response = stub.despegar(avion)
            end
        else
            puts "[Avion - #{name}]: Pista #{response.estado} asignada y altura de #{response.altura}."
            puts "[Avion - #{name}]: Presione enter para iniciar el vuelo"
            gets.chomp
            response = stub.salir(avion)
            first = true
        end
    else
        sleep(10)
    end
end