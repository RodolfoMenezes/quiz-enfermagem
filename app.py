# SALVE ESTE ARQUIVO COMO: quiz_enfermagem_imediato.py

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Quiz Interativo - Enfermagem", page_icon="💉", layout="centered")

# --- CSS PARA DEIXAR MAIS BONITO ---
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stButton button {
            background-color: #1e88e5;
            color: white;
            font-weight: bold;
            border-radius: 20px;
            padding: 10px 24px;
            width: 100%;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #1565c0;
            color: white;
            transform: scale(1.02);
        }
        .stRadio label { font-size: 18px; padding: 8px; }
        .stRadio [data-baseweb="radio"] { margin-top: 10px; }
        .feedback-certo { 
            background-color: #d4edda; 
            padding: 15px; 
            border-radius: 10px; 
            border-left: 6px solid #28a745;
            margin-top: 15px;
        }
        .feedback-errado {
            background-color: #f8d7da; 
            padding: 15px; 
            border-radius: 10px; 
            border-left: 6px solid #dc3545;
            margin-top: 15px;
        }
        .explicacao-box {
            background-color: #e3f2fd; 
            padding: 15px; 
            border-radius: 10px; 
            border-left: 6px solid #0d6efd;
            margin-top: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- BANCO DE PERGUNTAS (TODAS COM EXPLICAÇÕES DETALHADAS) ---
PERGUNTAS = [
    {
        "pergunta": "Durante a aspiração de vias aéreas artificiais (traqueostomia), qual é a pressão de vácuo recomendada para a fonte de aspiração fixa (de parede)?",
        "opcoes": ["40 a 60 mmHg", "80 a 120 mmHg", "150 a 200 mmHg", "10 a 15 mmHg"],
        "resposta_correta": "80 a 120 mmHg",
        "explicacao": "A pressão recomendada para fonte fixa (de parede) é de 80 a 120 mmHg. Para aspiradores portáteis, a pressão negativa deve ser de 10 a 15 mmHg. Essa padronização garante a remoção eficaz das secreções sem causar trauma à mucosa traqueal."
    },
    {
        "pergunta": "Em um paciente com traqueostomia e cânula com balonete (cuff), qual cuidado é fundamental antes de iniciar a alimentação por sonda enteral?",
        "opcoes": [
            "Aspirar a cavidade oral com a mesma sonda da traqueostomia.",
            "Manter o balonete insuflado durante a alimentação.",
            "Posicionar o paciente em decúbito dorsal plano.",
            "Desinsuflar o balonete para facilitar a passagem da dieta."
        ],
        "resposta_correta": "Manter o balonete insuflado durante a alimentação.",
        "explicacao": "O balonete (cuff) deve permanecer insuflado durante a alimentação por sonda para vedar a via aérea, prevenindo a broncoaspiração da dieta. Além disso, o paciente deve ser mantido em posição de Fowler ou semi-Fowler (cabeceira elevada entre 30° e 45°)."
    },
    {
        "pergunta": "O eletrocardiograma (ECG) é composto por ondas, complexos, segmentos e intervalos. Qual estrutura representa a despolarização dos ventrículos?",
        "opcoes": ["Onda P", "Onda T", "Complexo QRS", "Intervalo PR"],
        "resposta_correta": "Complexo QRS",
        "explicacao": "O complexo QRS representa a despolarização dos ventrículos. A onda P representa a despolarização atrial. A onda T representa a repolarização ventricular. O intervalo PR mede o tempo de condução do nó sinusal até os ventrículos."
    },
    {
        "pergunta": "Em um paciente com infarto agudo do miocárdio com supradesnivelamento do segmento ST (IAMCSST), a alteração eletrocardiográfica típica que indica lesão miocárdica subepicárdica é:",
        "opcoes": [
            "Onda T negativa e simétrica.",
            "Infradesnivelamento do segmento ST.",
            "Supradesnivelamento do segmento ST com convexidade para cima.",
            "Aparecimento de onda Q patológica."
        ],
        "resposta_correta": "Supradesnivelamento do segmento ST com convexidade para cima.",
        "explicacao": "No IAM com supradesnível (IAMCSST), a lesão subepicárdica gera elevação do segmento ST com convexidade voltada para cima. A onda T negativa e simétrica indica isquemia subepicárdica. O infradesnível ocorre na lesão subendocárdica (angina instável/IAM sem supradesnível). A onda Q patológica, por sua vez, indica necrose (morte celular) e tem caráter irreversível."
    },
    {
        "pergunta": "A oximetria de pulso é um método não invasivo para monitorar a saturação de oxigênio (SpO₂). Qual valor de SpO₂, em geral, indica a necessidade de aumentar a suplementação de oxigênio e deve ser reportado ao médico?",
        "opcoes": ["Acima de 97%", "Entre 95% e 97%", "Abaixo de 93%", "Exatamente 100%"],
        "resposta_correta": "Abaixo de 93%",
        "explicacao": "Valores de saturação (SpO₂) abaixo de 93% indicam hipoxemia clínica, exigindo aumento do oxigênio suplementar e comunicação imediata à equipe médica. A meta geral é manter a SpO₂ acima de 93% (e acima de 90% em pacientes com DPOC, que toleram níveis mais baixos)."
    },
    {
        "pergunta": "Durante o procedimento de cateterismo vesical de demora em uma mulher, a ordem correta da antissepsia do meato uretral e região perineal é:",
        "opcoes": [
            "Meato uretral → pequenos lábios → grandes lábios → períneo.",
            "Grandes lábios → pequenos lábios → meato uretral → introito vaginal → períneo.",
            "Períneo → meato uretral → pequenos lábios → grandes lábios.",
            "Introito vaginal → meato uretral → grandes lábios → pequenos lábios."
        ],
        "resposta_correta": "Grandes lábios → pequenos lábios → meato uretral → introito vaginal → períneo.",
        "explicacao": "A antissepsia deve ser realizada no sentido de cima para baixo e de fora para dentro, para evitar a contaminação do meato uretral com bactérias da região perineal. A ordem correta é: grandes lábios, pequenos lábios, meato uretral (movimento circular), introito vaginal e, por fim, períneo."
    },
    {
        "pergunta": "A sonda de Levine (ou Levin) é comumente utilizada para drenagem gástrica. Qual é a medida de referência para inserção da sonda nasogástrica em um adulto?",
        "opcoes": [
            "Do lóbulo da orelha ao apêndice xifoide.",
            "Do nariz ao lóbulo da orelha e ao apêndice xifoide.",
            "Do nariz ao umbigo.",
            "Do lóbulo da orelha à crista ilíaca."
        ],
        "resposta_correta": "Do nariz ao lóbulo da orelha e ao apêndice xifoide.",
        "explicacao": "A medida padrão para sonda gástrica (Levine) é: nariz → lóbulo da orelha → apêndice xifoide. Para a sonda nasoentérica (Dobb Hoff), a medição vai do nariz ao lóbulo da orelha, apêndice xifoide e até a crista ilíaca (avançando mais 10 a 20 cm após o apêndice xifoide) para garantir que a ponta chegue ao duodeno/jejuno."
    },
    {
        "pergunta": "Uma pessoa com colostomia terminal no cólon sigmoide, que deseja controlar o horário das eliminações intestinais e reduzir o uso de bolsas, pode ser orientada a realizar qual técnica?",
        "opcoes": [
            "Irrigação da colostomia.",
            "Uso de sistema oclusor (tampão).",
            "Realização de enteroclisma.",
            "Uso de bolsa de urostomia."
        ],
        "resposta_correta": "Irrigação da colostomia.",
        "explicacao": "A irrigação da colostomia é uma técnica que utiliza água morna (à temperatura corporal) infundida pelo estoma para limpar o cólon descendente ou sigmoide, permitindo o controle do horário das eliminações (geralmente a cada 24 ou 48 horas) e reduzindo o uso contínuo de bolsas coletoras. O método é indicado para colostomias terminais no cólon descendente ou sigmoide, sem complicações como prolapso ou hérnia."
    },
    {
        "pergunta": "Na administração de insulina regular (ação rápida) por via subcutânea, qual a seringa e agulha mais adequadas para garantir a dose correta e o menor trauma?",
        "opcoes": [
            "Seringa de 3 mL com agulha 25x7.",
            "Seringa de insulina com agulha 13x4,5 ou 13x3,8.",
            "Seringa de 5 mL com agulha 30x7.",
            "Seringa de 1 mL com agulha intramuscular."
        ],
        "resposta_correta": "Seringa de insulina com agulha 13x4,5 ou 13x3,8.",
        "explicacao": "A insulina deve ser administrada com seringa própria para insulina, que é graduada em unidades (UI), e com agulha fina (13x4,5 ou 13x3,8). Isso garante a precisão da dose e minimiza o trauma tecidual e a dor. NUNCA se deve usar seringas comuns (de 3 mL ou 5 mL) para insulina, pois a graduação é em mililitros, o que pode causar erros gravíssimos de dosagem."
    },
    {
        "pergunta": "O Índice de Massa Corporal (IMC) é um indicador antropométrico importante. De acordo com a classificação da OMS, qual faixa de IMC caracteriza sobrepeso em adultos?",
        "opcoes": ["Abaixo de 18,5 kg/m²", "Entre 18,5 e 24,9 kg/m²", "Entre 25,0 e 29,9 kg/m²", "Acima de 30,0 kg/m²"],
        "resposta_correta": "Entre 25,0 e 29,9 kg/m²",
        "explicacao": "Segundo a OMS: abaixo de 18,5 = baixo peso; 18,5 a 24,9 = normal (eutrófico); 25,0 a 29,9 = sobrepeso; ≥ 30,0 = obesidade. O IMC é calculado dividindo o peso (kg) pela altura (m) ao quadrado."
    },
    {
        "pergunta": "A cianose central (observada nas mucosas dos olhos e da boca) é uma manifestação benigna e pode ser ignorada, pois indica apenas vasoconstrição periférica local.",
        "opcoes": ["Verdadeiro", "Falso"],
        "resposta_correta": "Falso",
        "explicacao": "A cianose central (lábios, mucosa oral e conjuntiva) é um sinal de alerta GRAVE que indica hipoxemia significativa (baixa saturação de oxigênio no sangue arterial). Ela nunca deve ser ignorada. Ao contrário, a cianose periférica (pontas dos dedos e unhas) pode ser benigna e decorrer de vasoconstrição local por frio."
    },
    {
        "pergunta": "Durante a aspiração de vias aéreas superiores, a sonda utilizada na cavidade nasal pode ser reutilizada para aspirar a cavidade oral, desde que seja lavada com soro fisiológico entre as aspirações.",
        "opcoes": ["Verdadeiro", "Falso"],
        "resposta_correta": "Falso",
        "explicacao": "Nunca se deve utilizar a mesma sonda de aspiração para as cavidades nasal/oral e, depois, na traqueostomia ou tubo endotraqueal. A sonda usada na boca e no nariz é considerada contaminada (microrganismos da orofaringe) e não pode ser reintroduzida na via aérea inferior. Além disso, a ordem correta é aspirar as vias superiores (menos contaminadas) com uma sonda, descartá-la, e só então aspirar a via aérea artificial com outra sonda estéril."
    }
]

# --- FUNÇÃO PRINCIPAL ---
def main():

    # Inicializa as variáveis de estado (sessão)
    if "indice" not in st.session_state:
        st.session_state.indice = 0
        st.session_state.pontuacao = 0
        st.session_state.finalizado = False
        st.session_state.scored = {}  # Dicionário para marcar se cada pergunta já foi pontuada

    # Título e cabeçalho
    st.title("💉 Quiz Imediato - Semiologia e Semiotécnica")
    st.markdown("*Clique em uma alternativa para ver a explicação na hora!*")
    st.markdown("---")

    # --- SE O QUIZ TERMINOU ---
    if st.session_state.finalizado:
        st.balloons()
        st.header("🏆 Resultado Final")
        
        total = len(PERGUNTAS)
        acertos = st.session_state.pontuacao
        percentual = int((acertos / total) * 100)

        # Define classificação
        if acertos >= 10:
            icon = "👑"
            msg = "Enfermeira Master! Você domina o assunto com excelência!"
        elif acertos >= 7:
            icon = "💪"
            msg = "Quase lá! Reforce os tópicos com mais leitura e você chega lá."
        elif acertos >= 4:
            icon = "📚"
            msg = "Bom início! Revise os conceitos básicos com calma."
        else:
            icon = "🤝"
            msg = "Calma! Este é o momento de aprender. Estude com calma e tente novamente."

        st.markdown(f"## {icon} Você acertou **{acertos}** de **{total}** perguntas (**{percentual}%**)")
        st.markdown(f"### {msg}")
        
        if st.button("🔄 Recomeçar Quiz", use_container_width=True):
            st.session_state.indice = 0
            st.session_state.pontuacao = 0
            st.session_state.finalizado = False
            st.session_state.scored = {}
            st.rerun()
        return

    # --- LÓGICA DA PERGUNTA ATUAL ---
    idx = st.session_state.indice
    pergunta_atual = PERGUNTAS[idx]

    # Barra de progresso
    st.progress((idx + 1) / len(PERGUNTAS))
    st.caption(f"Pergunta {idx + 1} de {len(PERGUNTAS)}")

    # Exibe a pergunta
    st.subheader(pergunta_atual["pergunta"])

    # Verifica se esta pergunta já foi respondida (para bloquear o radio)
    ja_respondida = st.session_state.scored.get(idx, False)

    # Cria a chave única para o radio
    radio_key = f"radio_{idx}"

    # Exibe as opções (desabilita se já respondida)
    resposta = st.radio(
        "Selecione uma alternativa:",
        pergunta_atual["opcoes"],
        key=radio_key,
        index=None,
        disabled=ja_respondida
    )

    # --- LÓGICA DE CORREÇÃO IMEDIATA ---
    # Se uma opção foi selecionada E esta pergunta ainda não foi pontuada
    if resposta is not None and not ja_respondida:
        # Verifica se acertou
        if resposta == pergunta_atual["resposta_correta"]:
            st.session_state.pontuacao += 1
            st.session_state.scored[idx] = True  # Marca como respondida
        else:
            st.session_state.scored[idx] = True  # Marca como respondida mesmo errando
        
        # Força o recarregamento da página para mostrar o feedback
        st.rerun()

    # --- EXIBE O FEEDBACK (se já foi respondida) ---
    if ja_respondida:
        # Verifica qual foi a resposta selecionada (pegando do session_state)
        resposta_selecionada = st.session_state.get(radio_key, None)
        correta = pergunta_atual["resposta_correta"]

        # Caixa de acerto ou erro
        if resposta_selecionada == correta:
            st.markdown('<div class="feedback-certo">✅ <b>Resposta correta!</b> 🎉</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="feedback-errado">❌ <b>Ops, não foi dessa vez!</b> A resposta correta é: <b>{correta}</b></div>', unsafe_allow_html=True)

        # Caixa de explicação (sempre aparece, para ela aprender sempre!)
        st.markdown(f'<div class="explicacao-box">📘 <b>Explicação detalhada:</b><br>{pergunta_atual["explicacao"]}</div>', unsafe_allow_html=True)

        # Botão para avançar (aparece somente após responder)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("➡️ Próxima pergunta", use_container_width=True):
                # Verifica se é a última pergunta
                if idx + 1 < len(PERGUNTAS):
                    st.session_state.indice += 1
                    st.rerun()
                else:
                    st.session_state.finalizado = True
                    st.rerun()

    # Rodapé com a pontuação parcial
    st.markdown("---")
    st.caption(f"✅ Pontuação atual: {st.session_state.pontuacao} acerto(s)")

if __name__ == "__main__":
    main()
