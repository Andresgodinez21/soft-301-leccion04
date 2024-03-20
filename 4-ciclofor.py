lista_etapas_lavado = ["Llenado", "Lavado", "Enjuage", "Drenado", "Listo"]

for elemento in lista_etapas_lavado:
    print(elemento)
    if elemento == "Llenado" or elemento == "Listo":
        print("Puedes abrir la tapa :")
    else:
        print("No puede abrir la tapa, espere.....")

    print("##################")
