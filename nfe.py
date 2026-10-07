# CALCULO DE IMPOSTO PARA NFE
while 1>0:
    try:
        valor = float(input("Valor total: "))
        icms = valor * 0.0307
        pis = valor * 0.003
        confins = valor * 0.01253
        im = icms+pis+confins

        #print("ICMS ", round(icms, 2) ," PIS ",round(pis,2), " COFINS ", round(confins,2))
        texto = f"ICMS  {icms:.2f}  PIS {pis:.2f}  COFINS  {confins:.2f}"
        saida = texto.replace(".", ",")
        textoim = f"Total de imposto pago pro governo: {im:.2f}"
        print(saida)
        #print(textoim.replace(".", ","))
    except:
        print("Input inválido")
