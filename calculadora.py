PESOS_COBRE = {
    "1/4": 0.130,
    "3/8": 0.203,
    "1/2": 0.283,
    "5/8": 0.350,
    "3/4": 0.423,
    "7/8": 0.509,
}


def metros_para_kg(bitola, metros):
    peso_por_metro = PESOS_COBRE[bitola]

    peso_exato = metros * peso_por_metro
    peso_com_acrescimo = peso_exato + 0.300

    return {
        "bitola": bitola,
        "metros": metros,
        "peso_exato": peso_exato,
        "peso_com_acrescimo": peso_com_acrescimo,
    }


def kg_para_metros(bitola, kg):
    peso_por_metro = PESOS_COBRE[bitola]

    metros = kg / peso_por_metro

    return {
        "bitola": bitola,
        "kg": kg,
        "metros": metros,
    }


def calcular_btus(area, pessoas=1, sol=False):
    """
    Calcula uma estimativa de BTUs com base na área.

    area: área do ambiente em m²
    pessoas: quantidade de pessoas no ambiente
    sol: True se houver incidência direta de sol
    """

    btus_por_metro = 600

    btus = area * btus_por_metro

    if pessoas > 1:
        btus += (pessoas - 1) * 600

    if sol:
        btus += 800

    # Arredonda para uma capacidade comercial de ar-condicionado
    capacidades = [
        7500,
        9000,
        12000,
        18000,
        24000,
        30000,
        36000,
        48000,
        60000,
    ]

    btus_recomendado = capacidades[-1]

    for capacidade in capacidades:
        if btus <= capacidade:
            btus_recomendado = capacidade
            break

    return {
        "area": area,
        "pessoas": pessoas,
        "sol": sol,
        "btus_calculado": btus,
        "btus_recomendado": btus_recomendado,
    }