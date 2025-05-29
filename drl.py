def simulate_drl_decision(energia, banda, prioridade, estabilidade):
    score = (energia * 0.3 + banda * 0.3 + prioridade * 0.2 + estabilidade * 0.2)
    if score > 75:
        return "Alta Performance"
    elif score > 50:
        return "Modo Balanceado"
    else:
        return "Economia de Energia"