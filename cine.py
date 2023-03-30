def valor_de_boleta (numero_boletas, tipo_de_sala, horario, medio_de_pago, reserva):
    tarifa = 0
    if tipo_de_sala == 'Dinamix':
        tarifa = 18800
    elif tipo_de_sala == '3D':
        tarifa = 15500
    elif tipo_de_sala == '2D':
        tarifa = 11300
    if horario < 16 or horario > 21:
        descuento_horas_no_pico = 0.1
        descuento_boletas_variado = 0
        if numero_boletas >= 3:
            descuento_boletas_variado = 500
        descuento_promocion = (descuento_horas_no_pico * tarifa) + (descuento_boletas_variado * (numero_boletas - 1))
        tarifa = tarifa - descuento_promocion

    if medio_de_pago == 'tarjeta_cinema':
        descuento_de_tarjeta = 0.05 * tarifa
        tarifa = tarifa - descuento_de_tarjeta

    if reserva:
        recargo_reserva = 2000
        tarifa = tarifa + recargo_reserva

    if 16 <= horario <= 21:
        if tipo_de_sala == '2D' or tipo_de_sala == '3D':
            tarifa = tarifa * 1.25
        elif tipo_de_sala == 'Dinamix':
            tarifa = tarifa * 1.50

    precio_total = tarifa * numero_boletas
    return precio_total

resultado = valor_de_boleta(1, '2D', 10, 'tarjeta_cinema', False)
print("total pagar: ", resultado)
resultado = valor_de_boleta(2, '3D', 17, 'tarjeta_cinema', False)
print("total pagar: ", resultado)
resultado = valor_de_boleta(1, 'Dinamix', 20, 'tarjeta_cinema', True)
print("total pagar: ", resultado)