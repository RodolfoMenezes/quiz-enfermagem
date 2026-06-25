# SALVE ESTE ARQUIVO COMO: app.py

import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="Quiz Enfermagem - 100 Perguntas", page_icon="💉", layout="centered")

# --- CSS PARA DEIXAR MAIS BONITO ---
st.markdown("""
    <style>
        .main { background-color: #f0f2f6; }
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
        .high-score-box {
            background-color: #fff3cd;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #ffc107;
            text-align: center;
            margin-bottom: 20px;
        }
        .historico-box {
            background-color: #e8e8e8;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# BANCO DE 100 PERGUNTAS (BASEADO NOS SEUS DOCUMENTOS)
# ============================================================
PERGUNTAS_ORIGINAIS = [

    # --- TEMA 1: OXIGENAÇÃO (20 perguntas) ---
    {
        "pergunta": "Qual é a frequência respiratória normal para um adulto em repouso?",
        "opcoes": ["8 a 12 rpm", "12 a 20 rpm", "20 a 28 rpm", "28 a 36 rpm"],
        "resposta_correta": "12 a 20 rpm",
        "explicacao": "A frequência respiratória normal do adulto varia de 12 a 20 respirações por minuto (rpm). Recém-nascidos respiram mais rápido (30-60 rpm), e a frequência diminui com a idade."
    },
    {
        "pergunta": "O que significa apneia?",
        "opcoes": ["Respiração rápida e profunda", "Cessação da respiração por 20 segundos ou mais", "Dificuldade para respirar", "Respiração ruidosa"],
        "resposta_correta": "Cessação da respiração por 20 segundos ou mais",
        "explicacao": "Apneia é a cessação da respiração por 20 segundos ou mais. É normal em recém-nascidos por poucos segundos, mas frequente ou prolongada é anormal."
    },
    {
        "pergunta": "Onde ocorre a troca gasosa (difusão) entre o ar e o sangue?",
        "opcoes": ["Bronquíolos", "Traqueia", "Alvéolos", "Faringe"],
        "resposta_correta": "Alvéolos",
        "explicacao": "A troca gasosa ocorre nos alvéolos, que são pequenos sacos de ar envoltos por capilares. O oxigênio difunde-se do alvéolo para o sangue, e o dióxido de carbono faz o caminho inverso."
    },
    {
        "pergunta": "A cianose central (lábios e mucosas) é um sinal de:",
        "opcoes": ["Vasoconstrição periférica benigna", "Hipoxemia grave", "Excesso de hemoglobina", "Febre alta"],
        "resposta_correta": "Hipoxemia grave",
        "explicacao": "A cianose central indica baixa saturação de oxigênio no sangue arterial e é um sinal de alerta grave. Ao contrário, a cianose periférica (pontas dos dedos) pode ser benigna por frio."
    },
    {
        "pergunta": "Qual a pressão de vácuo recomendada para aspiração traqueal em fonte de parede?",
        "opcoes": ["10 a 15 mmHg", "40 a 60 mmHg", "80 a 120 mmHg", "150 a 200 mmHg"],
        "resposta_correta": "80 a 120 mmHg",
        "explicacao": "A pressão para aspirador de parede é de 80 a 120 mmHg. Para aspiradores portáteis, a pressão negativa é de 10 a 15 mmHg."
    },
    {
        "pergunta": "O tamanho da sonda de aspiração não deve exceder qual porcentagem do diâmetro do tubo endotraqueal?",
        "opcoes": ["30%", "40%", "50%", "60%"],
        "resposta_correta": "50%",
        "explicacao": "A sonda deve ter no máximo 50% do diâmetro do TOT para evitar hipóxia e trauma. Exemplo: TOT 8,0 mm → sonda no máximo 14 Fr."
    },
    {
        "pergunta": "Qual o tempo máximo recomendado para cada passagem da sonda durante a aspiração traqueal?",
        "opcoes": ["5 segundos", "10 a 15 segundos", "20 segundos", "30 segundos"],
        "resposta_correta": "10 a 15 segundos",
        "explicacao": "Cada passagem da sonda deve durar no máximo 10 a 15 segundos para evitar hipóxia grave e resposta vagal (bradicardia)."
    },
    {
        "pergunta": "Como se chama o mecanismo de defesa pulmonar que varre o muco para cima?",
        "opcoes": ["Macrófago alveolar", "Elevador mucociliar", "Reflexo da tosse", "Reflexo do espirro"],
        "resposta_correta": "Elevador mucociliar",
        "explicacao": "O elevador mucociliar é composto por células ciliadas que transportam o muco com partículas aprisionadas para cima e para fora dos pulmões, protegendo contra infecções."
    },
    {
        "pergunta": "O que é atelectasia?",
        "opcoes": ["Inflamação dos alvéolos", "Colapso alveolar", "Acúmulo de líquido no pulmão", "Espasmo brônquico"],
        "resposta_correta": "Colapso alveolar",
        "explicacao": "Atelectasia é o colapso dos alvéolos, reduzindo a área para troca gasosa. Ocorre por restrição do movimento pulmonar (dor, obesidade) ou obstrução da via aérea."
    },
    {
        "pergunta": "Qual o fluxo máximo de oxigênio recomendado para a cânula nasal (óculos) para não ressecar a mucosa?",
        "opcoes": ["2 L/min", "4 L/min", "6 L/min", "10 L/min"],
        "resposta_correta": "6 L/min",
        "explicacao": "A cânula nasal é usada com fluxo de 1 a 6 L/min (FIO2 24-44%). Acima de 6 L/min, o ar seco pode ressecar e lesar a mucosa nasal, necessitando umidificador."
    },
    {
        "pergunta": "O que é o ponto J no eletrocardiograma?",
        "opcoes": ["Final da onda P", "Transição entre o QRS e o segmento ST", "Pico da onda R", "Final da onda T"],
        "resposta_correta": "Transição entre o QRS e o segmento ST",
        "explicacao": "O ponto J é o ponto de junção entre o final do complexo QRS e o início do segmento ST. O desnível do ponto J (> 1 mm nas periféricas ou > 2 mm nas precordiais) indica lesão miocárdica."
    },
    {
        "pergunta": "Qual derivação do ECG é mais utilizada para monitorização cardíaca contínua?",
        "opcoes": ["DI", "DII", "aVR", "V1"],
        "resposta_correta": "DII",
        "explicacao": "A derivação DII é a preferida para monitorização porque seu eixo elétrico é o mais paralelo ao fluxo normal do coração, gerando as ondas mais visíveis."
    },
    {
        "pergunta": "No ECG, as derivações V1 e V2 visualizam qual parede cardíaca?",
        "opcoes": ["Anterior", "Inferior", "Lateral", "Septal"],
        "resposta_correta": "Septal",
        "explicacao": "V1 (4º EIC à direita do esterno) e V2 (4º EIC à esquerda do esterno) visualizam a parede septal. V3/V4 = anterior; V5/V6 = lateral; DII/DIII/aVF = inferior."
    },
    {
        "pergunta": "Qual substância é conhecida por deprimir o centro respiratório e diminuir a ventilação?",
        "opcoes": ["Cafeína", "Narcóticos (ex: morfina)", "Salbutamol", "Metilxantina"],
        "resposta_correta": "Narcóticos (ex: morfina)",
        "explicacao": "Barbitúricos, narcóticos e sedativos deprimem o sistema nervoso central, reduzindo a frequência e profundidade respiratória, podendo causar apneia."
    },
    {
        "pergunta": "Qual valor de saturação de oxigênio (SpO₂) indica hipoxemia e necessidade de aumentar o oxigênio?",
        "opcoes": ["< 90%", "< 93%", "< 95%", "< 97%"],
        "resposta_correta": "< 93%",
        "explicacao": "SpO₂ abaixo de 93% indica hipoxemia clínica, necessitando aumento do oxigênio suplementar e comunicação à equipe médica."
    },
    {
        "pergunta": "Se um dreno torácico for acidentalmente expulso do paciente, qual a conduta imediata?",
        "opcoes": ["Reintroduzir o dreno imediatamente", "Cobrir com gaze estéril e chamar o médico", "Aspirar o local", "Colocar selo d'água no curativo"],
        "resposta_correta": "Cobrir com gaze estéril e chamar o médico",
        "explicacao": "Nunca reinsira o dreno. Cubra o orifício com gaze estéril (compressa oclusiva) e chame o médico imediatamente para evitar pneumotórax aberto."
    },
    {
        "pergunta": "Qual a função do surfactante pulmonar?",
        "opcoes": ["Aumentar a tensão superficial", "Diminuir a tensão superficial e evitar colapso alveolar", "Aumentar o fluxo sanguíneo", "Produzir muco"],
        "resposta_correta": "Diminuir a tensão superficial e evitar colapso alveolar",
        "explicacao": "O surfactante reduz a tensão superficial nos alvéolos, evitando que eles colabem na expiração. Prematuros não têm surfactante suficiente, causando Síndrome do Desconforto Respiratório."
    },
    {
        "pergunta": "O baqueteamento dos dedos (dedos em hipocráticos) está associado a:",
        "opcoes": ["Anemia", "Doença pulmonar crônica e hipóxia prolongada", "Hipertensão", "Taquicardia"],
        "resposta_correta": "Doença pulmonar crônica e hipóxia prolongada",
        "explicacao": "O baqueteamento digital (arredondamento e alargamento das extremidades) ocorre por hipóxia tissular prolongada, comum em DPOC, fibrose cística e câncer de pulmão."
    },
    {
        "pergunta": "Qual o método de confirmação da posição da sonda nasoentérica (Dobb Hoff)?",
        "opcoes": ["Ausculta com insuflação de ar", "Medição do pH gástrico", "Raio-X de tórax/abdome", "Teste com seringa"],
        "resposta_correta": "Raio-X de tórax/abdome",
        "explicacao": "Para sonda nasoentérica (pós-pilórica), o Raio-X é obrigatório para confirmar a posição no duodeno/jejuno antes de usar. Sondas gástricas podem ser confirmadas por pH e ausculta."
    },
    {
        "pergunta": "Como se chama o som anormal de alta tonalidade ouvido na ausculta pulmonar na asma?",
        "opcoes": ["Estertores", "Roncos", "Sibilos", "Atrito pleural"],
        "resposta_correta": "Sibilos",
        "explicacao": "Sibilos são sons contínuos de alta tonalidade, característicos de broncoespasmo ou obstrução de vias aéreas, como na asma e DPOC."
    },

    # --- TEMA 2: NUTRIÇÃO (20 perguntas) ---
    {
        "pergunta": "O que significa IMC (Índice de Massa Corporal)?",
        "opcoes": ["Peso (kg) / Altura (m)", "Peso (kg) / Altura² (m²)", "Altura (m) / Peso (kg)", "Peso (kg) x Altura (m)"],
        "resposta_correta": "Peso (kg) / Altura² (m²)",
        "explicacao": "O IMC é calculado dividindo o peso em quilogramas pela altura em metros ao quadrado. É usado para classificar o estado nutricional."
    },
    {
        "pergunta": "Qual IMC classifica um adulto como obeso?",
        "opcoes": ["> 25 kg/m²", "> 27 kg/m²", "≥ 30 kg/m²", "≥ 35 kg/m²"],
        "resposta_correta": "≥ 30 kg/m²",
        "explicacao": "Obesidade é IMC ≥ 30 kg/m². Sobrepeso é 25,0 a 29,9. Abaixo de 18,5 é baixo peso."
    },
    {
        "pergunta": "Qual vitamina é sintetizada pelo organismo através da exposição à luz solar?",
        "opcoes": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"],
        "resposta_correta": "Vitamina D",
        "explicacao": "A vitamina D é produzida na pele pela ação dos raios UVB. É essencial para a absorção de cálcio e saúde óssea."
    },
    {
        "pergunta": "A bile, produzida pelo fígado, tem qual função principal na digestão?",
        "opcoes": ["Digestão de proteínas", "Digestão de carboidratos", "Emulsificação de gorduras (lipídios)", "Digestão de ácidos nucleicos"],
        "resposta_correta": "Emulsificação de gorduras (lipídios)",
        "explicacao": "A bile emulsifica (quebra em gotículas menores) os lipídios, aumentando a superfície de ação da lipase pancreática."
    },
    {
        "pergunta": "O que é disfagia?",
        "opcoes": ["Perda de apetite", "Dificuldade de deglutição", "Vômito frequente", "Dor abdominal"],
        "resposta_correta": "Dificuldade de deglutição",
        "explicacao": "Disfagia é a dificuldade de deglutir, podendo ser orofaríngea (neurológica, como AVC) ou esofágica (obstrutiva, como tumores)."
    },
    {
        "pergunta": "No sistema digestivo, o jejuno é uma parte de qual órgão?",
        "opcoes": ["Estômago", "Intestino delgado", "Intestino grosso", "Pâncreas"],
        "resposta_correta": "Intestino delgado",
        "explicacao": "O intestino delgado é dividido em duodeno, jejuno e íleo. O jejuno é a porção média, onde ocorre grande parte da absorção de nutrientes."
    },
    {
        "pergunta": "Qual macronutriente é a principal fonte de energia do organismo?",
        "opcoes": ["Lipídios", "Proteínas", "Carboidratos", "Vitaminas"],
        "resposta_correta": "Carboidratos",
        "explicacao": "Os carboidratos fornecem 4 kcal por grama e são a principal e mais rápida fonte de energia, principalmente para o cérebro."
    },
    {
        "pergunta": "O processo de formação de glicose a partir de proteínas e lipídios no fígado é chamado de:",
        "opcoes": ["Glicogênese", "Glicogenólise", "Gliconeogênese", "Cetogênese"],
        "resposta_correta": "Gliconeogênese",
        "explicacao": "A gliconeogênese ocorre no fígado quando a glicose está em baixa, convertindo aminoácidos (proteínas) e glicerol (lipídios) em glicose."
    },
    {
        "pergunta": "Qual enzima e órgão são responsáveis pela produção da pepsina?",
        "opcoes": ["Amilase - Pâncreas", "Pepsina - Estômago", "Lipase - Fígado", "Tripsina - Intestino"],
        "resposta_correta": "Pepsina - Estômago",
        "explicacao": "A pepsina é uma enzima proteolítica secretada pelo estômago (na forma de pepsinogênio, ativada pelo ácido clorídrico), responsável por iniciar a digestão das proteínas."
    },
    {
        "pergunta": "A albumina sérica é um marcador laboratorial de:",
        "opcoes": ["Estado nutricional proteico", "Função renal", "Função cardíaca", "Níveis de glicose"],
        "resposta_correta": "Estado nutricional proteico",
        "explicacao": "A albumina (meia-vida de 18 dias) reflete a ingestão/produção de proteína. Valores < 3,5 g/dl indicam desnutrição ou doenças hepáticas/renais."
    },
    {
        "pergunta": "Qual é uma contraindicação absoluta para a passagem de sonda nasogástrica?",
        "opcoes": ["Paciente idoso", "Trauma facial com fratura de base de crânio", "Paciente em coma", "Refluxo gastroesofágico"],
        "resposta_correta": "Trauma facial com fratura de base de crânio",
        "explicacao": "Em fratura de base de crânio, a sonda pode penetrar na cavidade craniana. Contraindicações também incluem obstrução esofágica total e varizes esofágicas recentes."
    },
    {
        "pergunta": "Qual a medida de referência para inserção da sonda de Levine (gástrica) em adultos?",
        "opcoes": ["Nariz → lóbulo da orelha → apêndice xifoide", "Nariz → lóbulo da orelha → crista ilíaca", "Boca → umbigo", "Nariz → ombro → apêndice xifoide"],
        "resposta_correta": "Nariz → lóbulo da orelha → apêndice xifoide",
        "explicacao": "A medida padrão é (nariz) até (lóbulo da orelha) até (apêndice xifoide). Para sonda enteral (Dobb Hoff), vai até a crista ilíaca."
    },
    {
        "pergunta": "A dieta enteral administrada por sonda, após aberta, deve ser infundida em até:",
        "opcoes": ["2 horas", "4 horas", "8 horas", "24 horas"],
        "resposta_correta": "4 horas",
        "explicacao": "A dieta enteral não deve permanecer infundindo por mais de 4 horas para evitar proliferação bacteriana. Troque o frasco e o equipo a cada 24 horas."
    },
    {
        "pergunta": "O que significa Nutrição Parenteral Total (NPT)?",
        "opcoes": ["Nutrição via sonda gástrica", "Nutrição via oral com suplementos", "Nutrição por via intravenosa com soluções hipertônicas", "Nutrição via retal"],
        "resposta_correta": "Nutrição por via intravenosa com soluções hipertônicas",
        "explicacao": "NPT é a administração de nutrientes diretamente na corrente sanguínea, por via venosa central (subclávia/jugular), contendo glicose > 10%, aminoácidos, lipídios e eletrólitos."
    },
    {
        "pergunta": "Por que a NPT deve ser administrada por via venosa central?",
        "opcoes": ["Para ser mais rápida", "Devido à alta osmolaridade da solução, que irritaria veias periféricas", "Para evitar infecções", "Para permitir maior volume"],
        "resposta_correta": "Devido à alta osmolaridade da solução, que irritaria veias periféricas",
        "explicacao": "A NPT é hipertônica (osmolaridade elevada). Veias centrais (subclávia, jugular) têm alto fluxo sanguíneo, diluindo a solução e evitando tromboflebite."
    },
    {
        "pergunta": "O colostro, produzido nos primeiros dias de lactação, é rico em:",
        "opcoes": ["Gordura e carboidratos", "Anticorpos (imunoglobulinas)", "Ferro", "Vitamina K"],
        "resposta_correta": "Anticorpos (imunoglobulinas)",
        "explicacao": "O colostro é o primeiro leite, amarelado e rico em IgA e outros anticorpos, protegendo o recém-nascido contra infecções."
    },
    {
        "pergunta": "A constipação em idosos está frequentemente relacionada a:",
        "opcoes": ["Excesso de fibras", "Baixa ingestão de líquidos e fibras", "Alta ingestão de proteínas", "Excesso de exercícios"],
        "resposta_correta": "Baixa ingestão de líquidos e fibras",
        "explicacao": "Idosos frequentemente ingerem poucos líquidos e fibras, diminuindo a motilidade intestinal e causando constipação. A hidratação e fibras são essenciais."
    },
    {
        "pergunta": "Qual enzima é responsável pela digestão da lactose (açúcar do leite)?",
        "opcoes": ["Amilase", "Lipase", "Lactase", "Maltase"],
        "resposta_correta": "Lactase",
        "explicacao": "A lactase, produzida no intestino delgado, quebra a lactose em glicose e galactose. Sua deficiência causa intolerância à lactose (diarreia e distensão)."
    },
    {
        "pergunta": "O que é esteatorreia?",
        "opcoes": ["Fezes com sangue", "Fezes com presença de gordura", "Fezes líquidas e frequentes", "Fezes muito duras"],
        "resposta_correta": "Fezes com presença de gordura",
        "explicacao": "Esteatorreia são fezes gordurosas, volumosas, fétidas e de difícil descarga, indicando má absorção de lipídios (ex: doença celíaca, insuficiência pancreática)."
    },
    {
        "pergunta": "Um valor de albumina sérica abaixo de 3,5 g/dL sugere:",
        "opcoes": ["Desnutrição proteica", "Diabetes", "Hipertensão", "Anemia ferropriva"],
        "resposta_correta": "Desnutrição proteica",
        "explicacao": "Albumina abaixo de 3,5 g/dL indica depleção proteica e desnutrição, além de outras condições como doença hepática ou síndrome nefrótica."
    },

    # --- TEMA 3: ESTOMIAS (15 perguntas) ---
    {
        "pergunta": "A colostomia é um estoma criado em qual segmento intestinal?",
        "opcoes": ["Íleo", "Cólon (intestino grosso)", "Estômago", "Jejuno"],
        "resposta_correta": "Cólon (intestino grosso)",
        "explicacao": "Colostomia vem de 'cólon'. Ela exterioriza uma parte do intestino grosso para eliminação de fezes."
    },
    {
        "pergunta": "A ileostomia é um estoma criado em qual segmento intestinal?",
        "opcoes": ["Cólon", "Íleo (intestino delgado distal)", "Estômago", "Duodeno"],
        "resposta_correta": "Íleo (intestino delgado distal)",
        "explicacao": "A ileostomia é realizada no íleo (porção final do intestino delgado). O efluente é líquido/pastoso e muito irritante para a pele."
    },
    {
        "pergunta": "Qual a coloração normal de um estoma saudável?",
        "opcoes": ["Rosa pálido", "Vermelho-vivo ou rosa-escuro", "Azulada", "Branca"],
        "resposta_correta": "Vermelho-vivo ou rosa-escuro",
        "explicacao": "A mucosa do estoma deve ser vermelho-viva ou rosa-escura, úmida e brilhante, semelhante à mucosa oral. Coloração escura/preta indica necrose."
    },
    {
        "pergunta": "O prolapso de estoma é caracterizado por:",
        "opcoes": ["Estoma abaixo do nível da pele", "Exteriorização excessiva da alça intestinal", "Estenose do estoma", "Hérnia ao redor do estoma"],
        "resposta_correta": "Exteriorização excessiva da alça intestinal",
        "explicacao": "Prolapso é a protrusão excessiva (saída) da alça intestinal pelo orifício do estoma, podendo ser parcial ou total, e geralmente é reducível manualmente."
    },
    {
        "pergunta": "A necrose do estoma (cor escura/preta) é uma complicação que requer:",
        "opcoes": ["Troca da bolsa", "Avaliação médica imediata", "Aplicação de pomada", "Massagem local"],
        "resposta_correta": "Avaliação médica imediata",
        "explicacao": "A necrose (isquemia do estoma) é uma emergência cirúrgica. A coloração escura/preta indica falta de fluxo sanguíneo, podendo levar à perfuração e peritonite."
    },
    {
        "pergunta": "Para um estoma retraído (abaixo do nível da pele), qual equipamento é mais indicado?",
        "opcoes": ["Bolsa plana", "Bolsa convexa", "Bolsa com filtro", "Protetor de pele em pó"],
        "resposta_correta": "Bolsa convexa",
        "explicacao": "A bolsa convexa exerce pressão ao redor do estoma, ajudando a 'puxar' o estoma para fora e direcionar o efluente para a bolsa, evitando vazamentos."
    },
    {
        "pergunta": "A irrigação da colostomia é uma técnica que consiste em:",
        "opcoes": ["Passar água morna pelo estoma para limpar o cólon", "Aplicar pomada", "Trocar a bolsa", "Medicar via estoma"],
        "resposta_correta": "Passar água morna pelo estoma para limpar o cólon",
        "explicacao": "A irrigação usa água morna (à temperatura corporal) para evacuar o cólon sigmoide/descendente, permitindo controle do horário da eliminação."
    },
    {
        "pergunta": "O objetivo principal da demarcação pré-operatória do estoma é:",
        "opcoes": ["Reduzir custos", "Posicionar o estoma em local que facilite o autocuidado", "Facilitar a cirurgia", "Agradar o paciente"],
        "resposta_correta": "Posicionar o estoma em local que facilite o autocuidado",
        "explicacao": "A demarcação é feita com o paciente em várias posições (sentado, deitado) para escolher um local plano, longe de pregas e ossos, onde ele consiga ver e manusear o equipamento."
    },
    {
        "pergunta": "O que é a hérnia paraestomal?",
        "opcoes": ["Infecção no estoma", "Protrusão de vísceras ao redor do estoma", "Estoma estreitado", "Sangramento no estoma"],
        "resposta_correta": "Protrusão de vísceras ao redor do estoma",
        "explicacao": "A hérnia paraestomal é a saída de alças intestinais pela parede abdominal ao redor do estoma, causando abaulamento. Uso de cinta e evitar esforços são preventivos."
    },
    {
        "pergunta": "A limpeza da pele periestomal deve ser feita preferencialmente com:",
        "opcoes": ["Álcool 70%", "Água e sabão neutro", "Clorexidina", "Éter"],
        "resposta_correta": "Água e sabão neutro",
        "explicacao": "Álcool e substâncias agressivas danificam a pele. Use água morna e sabão neutro (pH próximo ao da pele), secando bem antes de aplicar a nova bolsa."
    },
    {
        "pergunta": "O recomendado é esvaziar a bolsa coletora quando ela estiver com aproximadamente:",
        "opcoes": ["Totalmente cheia", "1/3 da capacidade", "1/2 da capacidade", "3/4 da capacidade"],
        "resposta_correta": "1/3 da capacidade",
        "explicacao": "Esvazie a bolsa quando estiver com 1/3 da capacidade para evitar o peso excessivo que pode tracionar a placa adesiva e causar vazamentos."
    },
    {
        "pergunta": "A urostomia é um estoma para eliminação de:",
        "opcoes": ["Fezes", "Urina", "Muco", "Gases"],
        "resposta_correta": "Urina",
        "explicacao": "Urostomia é uma derivação urinária, onde a urina é eliminada através da parede abdominal, geralmente em casos de câncer de bexiga ou má-formação."
    },
    {
        "pergunta": "No conduto ileal (derivação de Bricker), o que é anastomosado?",
        "opcoes": ["Estômago ao íleo", "Ureteres ao íleo", "Cólon ao reto", "Íleo à bexiga"],
        "resposta_correta": "Ureteres ao íleo",
        "explicacao": "No conduto ileal, um segmento do íleo é isolado. Os ureteres são implantados nesse segmento, e a outra extremidade é exteriorizada como urostomia."
    },
    {
        "pergunta": "Os pelos ao redor do estoma devem ser removidos com:",
        "opcoes": ["Lâmina de barbear", "Tesoura", "Creme depilatório", "Pinça"],
        "resposta_correta": "Tesoura",
        "explicacao": "Use tesoura de ponta curva para aparar os pelos rentes à pele. Lâmina e cremes podem irritar a pele e causar lesões."
    },
    {
        "pergunta": "Quem é o profissional capacitado para prescrever adjuvantes (pós, pastas) para o cuidado do estoma?",
        "opcoes": ["Médico", "Enfermeiro Estomaterapeuta", "Farmacêutico", "Nutricionista"],
        "resposta_correta": "Enfermeiro Estomaterapeuta",
        "explicacao": "O Enfermeiro Estomaterapeuta (ou dermatoterapeuta) é o profissional especializado na avaliação, prescrição e orientação sobre equipamentos e adjuvantes para estomias."
    },

    # --- TEMA 4: ECG (15 perguntas) ---
    {
        "pergunta": "Qual a duração normal do complexo QRS no ECG?",
        "opcoes": ["0,04 a 0,08 s", "0,06 a 0,12 s", "0,12 a 0,20 s", "0,20 a 0,30 s"],
        "resposta_correta": "0,06 a 0,12 s",
        "explicacao": "O QRS normal é estreito, com duração entre 0,06 e 0,12 segundos. QRS alargado (> 0,12s) indica bloqueio de ramo ou ritmo ventricular (TV)."
    },
    {
        "pergunta": "O intervalo PR normal em adultos tem duração entre:",
        "opcoes": ["0,04 a 0,08 s", "0,06 a 0,12 s", "0,12 a 0,20 s", "0,20 a 0,30 s"],
        "resposta_correta": "0,12 a 0,20 s",
        "explicacao": "O intervalo PR (início da P ao início do QRS) mede a condução átrio-ventricular. Normal: 0,12 a 0,20 s. PR prolongado indica bloqueio AV de 1º grau."
    },
    {
        "pergunta": "A onda T no ECG representa:",
        "opcoes": ["Despolarização atrial", "Despolarização ventricular", "Repolarização ventricular", "Repolarização atrial"],
        "resposta_correta": "Repolarização ventricular",
        "explicacao": "A onda T representa a repolarização (recuperação elétrica) dos ventrículos. Geralmente é positiva, exceto em aVR."
    },
    {
        "pergunta": "A bradicardia é definida por uma frequência cardíaca:",
        "opcoes": ["< 50 bpm", "< 60 bpm", "> 100 bpm", "> 120 bpm"],
        "resposta_correta": "< 60 bpm",
        "explicacao": "Bradicardia é FC abaixo de 60 bpm no adulto. Taquicardia é FC acima de 100 bpm. Ritmo normal é 60-100 bpm."
    },
    {
        "pergunta": "A taquicardia é definida por uma frequência cardíaca:",
        "opcoes": ["< 50 bpm", "< 60 bpm", "> 90 bpm", "> 100 bpm"],
        "resposta_correta": "> 100 bpm",
        "explicacao": "Taquicardia é FC acima de 100 bpm no adulto. Pode ser fisiológica (exercício) ou patológica (febre, arritmias)."
    },
    {
        "pergunta": "O supradesnivelamento do segmento ST indica, na maioria das vezes:",
        "opcoes": ["Isquemia subendocárdica", "Lesão miocárdica subepicárdica (IAM)", "Necrose", "Hipertrofia ventricular"],
        "resposta_correta": "Lesão miocárdica subepicárdica (IAM)",
        "explicacao": "Supradesnivelamento (elevação) do ST reflete lesão (injúria) transmural ou subepicárdica, típica do Infarto Agudo do Miocárdio com supra de ST (IAMCSST)."
    },
    {
        "pergunta": "A onda Q patológica (profunda e larga) no ECG indica:",
        "opcoes": ["Isquemia reversível", "Lesão celular", "Necrose miocárdica", "Hipertrofia"],
        "resposta_correta": "Necrose miocárdica",
        "explicacao": "A onda Q patológica (duração ≥ 0,04s e amplitude ≥ 1/3 da R) indica necrose (morte celular), sendo um achado irreversível no ECG."
    },
    {
        "pergunta": "As derivações DII, DIII e aVF visualizam qual parede do coração?",
        "opcoes": ["Septal", "Anterior", "Inferior", "Lateral"],
        "resposta_correta": "Inferior",
        "explicacao": "DII, DIII e aVF (periféricas inferiores) visualizam a parede inferior do coração, geralmente suprida pela artéria coronária direita ou circunflexa."
    },
    {
        "pergunta": "As derivações V5 e V6 visualizam qual parede do coração?",
        "opcoes": ["Septal", "Anterior", "Inferior", "Lateral"],
        "resposta_correta": "Lateral",
        "explicacao": "V5 (linha axilar anterior) e V6 (linha axilar média) visualizam a parede lateral do ventrículo esquerdo."
    },
    {
        "pergunta": "A derivação V4R é utilizada para visualizar qual estrutura?",
        "opcoes": ["Parede posterior", "Ventrículo direito", "Átrio esquerdo", "Septo"],
        "resposta_correta": "Ventrículo direito",
        "explicacao": "V4R (posicionada à direita no 5º EIC linha hemiclavicular) é usada para detectar infarto do ventrículo direito, comum em IAM inferior."
    },
    {
        "pergunta": "Um intervalo QT prolongado (> 0,45s em homens, > 0,46s em mulheres) está associado a:",
        "opcoes": ["Menor risco de arritmias", "Maior risco de arritmias (Torsades de Pointes)", "Melhor prognóstico", "Bradicardia"],
        "resposta_correta": "Maior risco de arritmias (Torsades de Pointes)",
        "explicacao": "QT prolongado reflete repolarização ventricular prolongada e predispõe a arritmias graves como Torsades de Pointes, podendo ser congênito ou adquirido por drogas."
    },
    {
        "pergunta": "Qual a velocidade padrão do papel do eletrocardiograma?",
        "opcoes": ["10 mm/s", "25 mm/s", "50 mm/s", "100 mm/s"],
        "resposta_correta": "25 mm/s",
        "explicacao": "A velocidade padrão é 25 mm/s. Cada quadrado pequeno horizontal corresponde a 0,04 segundos. (1mm / 25mm/s = 0,04s)."
    },
    {
        "pergunta": "No ECG, cada quadrado pequeno horizontal (1 mm) corresponde a quanto tempo?",
        "opcoes": ["0,02 s", "0,04 s", "0,10 s", "0,20 s"],
        "resposta_correta": "0,04 s",
        "explicacao": "A 25 mm/s, 1 mm = 1/25 = 0,04 segundos. O quadrado grande (5 mm) = 0,20 segundos."
    },
    {
        "pergunta": "Para calcular a frequência cardíaca em um ritmo irregular, utiliza-se:",
        "opcoes": ["Método dos 1500", "Método sequencial 300-150-100", "Contar QRS em 30 quadrados grandes (6s) e multiplicar por 10", "Método dos 300"],
        "resposta_correta": "Contar QRS em 30 quadrados grandes (6s) e multiplicar por 10",
        "explicacao": "Em ritmos irregulares (ex: fibrilação atrial), conte o número de QRS em 30 quadrados grandes (equivalente a 6 segundos) e multiplique por 10 para obter batimentos por minuto."
    },
    {
        "pergunta": "O ponto J é o local exato onde:",
        "opcoes": ["Termina a onda P", "Termina o QRS e começa o segmento ST", "Começa a onda T", "Termina o intervalo PR"],
        "resposta_correta": "Termina o QRS e começa o segmento ST",
        "explicacao": "O ponto J é a junção entre o final do complexo QRS e o início do segmento ST. Sua análise é crucial para diagnosticar isquemia/lesão."
    },

    # --- TEMA 5: PROCEDIMENTOS/TÉCNICAS (15 perguntas) ---
    {
        "pergunta": "No cateterismo vesical de demora em mulher, a ordem correta da antissepsia é:",
        "opcoes": ["Meato → pequenos lábios → grandes lábios", "Grandes lábios → pequenos lábios → meato → introito → períneo", "Períneo → meato", "Introito → grandes lábios"],
        "resposta_correta": "Grandes lábios → pequenos lábios → meato → introito → períneo",
        "explicacao": "A antissepsia deve ser de cima para baixo e de fora para dentro: grandes lábios, pequenos lábios, meato uretral (circular), introito vaginal e períneo."
    },
    {
        "pergunta": "No cateterismo vesical de demora em homem, a ordem correta da antissepsia é:",
        "opcoes": ["Meato uretral → prepúcio → glande → corpo → escroto", "Corpo → glande → meato", "Escroto → prepúcio", "Glande → corpo → meato"],
        "resposta_correta": "Meato uretral → prepúcio → glande → corpo → escroto",
        "explicacao": "Começa-se pelo meato uretral em movimento circular, depois prepúcio, glande, corpo do pênis e por último o escroto."
    },
    {
        "pergunta": "Para administrar insulina regular (ação rápida), a seringa correta é:",
        "opcoes": ["Seringa de 3 ml", "Seringa de insulina (graduada em unidades)", "Seringa de 5 ml", "Seringa de 20 ml"],
        "resposta_correta": "Seringa de insulina (graduada em unidades)",
        "explicacao": "Utilize exclusivamente seringa própria para insulina, graduada em unidades (UI), com agulha 13x4,5 ou 13x3,8, para garantir dose exata."
    },
    {
        "pergunta": "De acordo com a Resolução COFEN nº 703/2022, a punção arterial para gasometria e monitorização invasiva é privativa de qual profissional?",
        "opcoes": ["Médico", "Enfermeiro", "Técnico de Enfermagem", "Fisioterapeuta"],
        "resposta_correta": "Enfermeiro",
        "explicacao": "A Resolução COFEN 703/2022 estabelece que a punção arterial é procedimento privativo do Enfermeiro, assim como a instalação de cateter arterial para monitorização da PAI."
    },
    {
        "pergunta": "Na sondagem gástrica (SNG), a competência do técnico de enfermagem inclui:",
        "opcoes": ["Inserir a sonda", "Confirmar a posição por Raio-X", "Auxiliar o enfermeiro e realizar os cuidados de manutenção", "Prescrever a dieta"],
        "resposta_correta": "Auxiliar o enfermeiro e realizar os cuidados de manutenção",
        "explicacao": "Conforme COFEN 619/2019, a inserção da SNG é privativa do Enfermeiro. Ao técnico cabe auxiliar, monitorar e manter o sistema de drenagem/alimentação."
    },
    {
        "pergunta": "Quem é responsável pela inserção da sonda nasogástrica (SNG), conforme a Resolução COFEN 619/2019?",
        "opcoes": ["Médico", "Enfermeiro", "Técnico de Enfermagem", "Nutricionista"],
        "resposta_correta": "Enfermeiro",
        "explicacao": "A Resolução COFEN 619/2019 determina que a sondagem oro/nasogástrica e nasoentérica é procedimento privativo do Enfermeiro."
    },
    {
        "pergunta": "Qual a pressão recomendada para aspiração em aspiradores portáteis (unidades móveis)?",
        "opcoes": ["10 a 15 mmHg", "40 a 60 mmHg", "80 a 120 mmHg", "150 a 200 mmHg"],
        "resposta_correta": "10 a 15 mmHg",
        "explicacao": "Aspiradores portáteis usam pressão negativa de 10 a 15 mmHg, enquanto a fonte de parede usa 80 a 120 mmHg."
    },
    {
        "pergunta": "Durante a aspiração traqueal, a passagem da sonda não deve ultrapassar:",
        "opcoes": ["5 segundos", "10 segundos", "15 segundos", "20 segundos"],
        "resposta_correta": "10 a 15 segundos",
        "explicacao": "O tempo máximo de aspiração é de 10 a 15 segundos para evitar hipoxemia e reflexo vagal. O intervalo entre as passagens deve ser de 1 minuto."
    },
    {
        "pergunta": "Se o paciente apresentar queda de saturação ou cianose durante a aspiração, a conduta é:",
        "opcoes": ["Aumentar a pressão", "Interromper o procedimento e oxigenar imediatamente", "Continuar aspirando mais rápido", "Injetar soro fisiológico"],
        "resposta_correta": "Interromper o procedimento e oxigenar imediatamente",
        "explicacao": "Se houver queda da saturação ou cianose, pare a aspiração imediatamente e oferte oxigênio para reverter a hipóxia antes de tentar novamente."
    },
    {
        "pergunta": "A sonda utilizada para drenagem gástrica (esvaziamento) é conhecida como:",
        "opcoes": ["Dobb Hoff", "Levine", "Foley", "Guedel"],
        "resposta_correta": "Levine",
        "explicacao": "A sonda de Levine (ou Levin) é mais calibrosa (14-22 Fr) e usada para drenagem/lavagem gástrica. Dobb Hoff (8-12 Fr) é usada para nutrição enteral."
    },
    {
        "pergunta": "Como confirmar a posição da sonda gástrica antes de iniciar a alimentação?",
        "opcoes": ["Apenas raio-x", "Ausculta com insuflação de ar e aspiração de conteúdo gástrico (pH < 4)", "Teste de sucção", "Verificar visualmente"],
        "resposta_correta": "Ausculta com insuflação de ar e aspiração de conteúdo gástrico (pH < 4)",
        "explicacao": "A confirmação é feita por ausculta de som característico ao insuflar ar, aspiração de conteúdo gástrico (pH ácido < 4) e, em casos duvidosos, raio-x."
    },
    {
        "pergunta": "O balonete da sonda de Foley (cateter vesical de demora) é insuflado com:",
        "opcoes": ["Soro fisiológico", "Água destilada", "Ar", "Lidocaína"],
        "resposta_correta": "Água destilada",
        "explicacao": "O balonete da Foley deve ser insuflado com água destilada (5 a 10 ml) para fixar o cateter na bexiga. Água destilada é isotônica e não cristaliza."
    },
    {
        "pergunta": "A posição ginecológica (litotômica) é utilizada para:",
        "opcoes": ["Sondagem gástrica", "Cateterismo vesical em mulheres", "Aspiração traqueal", "Administração de enema"],
        "resposta_correta": "Cateterismo vesical em mulheres",
        "explicacao": "A posição litotômica (decúbito dorsal, pernas fletidas e afastadas) é a posição padrão para cateterismo vesical feminino e exames ginecológicos."
    },
    {
        "pergunta": "A fixação da sonda Foley na mulher deve ser feita preferencialmente na:",
        "opcoes": ["Região abdominal", "Face interna da coxa", "Testa", "Perna"],
        "resposta_correta": "Face interna da coxa",
        "explicacao": "A sonda deve ser fixada na face interna da coxa com adesivo hipoalergênico, evitando tração e lesões uretrais. No homem, fixa-se na região superior da coxa ou abdome."
    },
    {
        "pergunta": "A administração de dieta enteral por seringa (intermitente) deve ser feita lentamente, em aproximadamente:",
        "opcoes": ["2 a 5 minutos", "10 a 15 minutos", "30 minutos", "1 hora"],
        "resposta_correta": "10 a 15 minutos",
        "explicacao": "A infusão intermitente por seringa deve levar 10 a 15 minutos para evitar náuseas, cólicas e vômitos por distensão gástrica súbita."
    },

    # --- TEMA 6: FISIOLOGIA/PATOLOGIA E DIVERSOS (15 perguntas) ---
    {
        "pergunta": "O que é hipóxia?",
        "opcoes": ["Baixo oxigênio no sangue arterial", "Deficiência de oxigênio nos tecidos", "Excesso de oxigênio", "Baixo dióxido de carbono"],
        "resposta_correta": "Deficiência de oxigênio nos tecidos",
        "explicacao": "Hipóxia é a redução de oxigênio a nível tissular. Hipoxemia é a redução no sangue arterial. A hipóxia pode causar danos celulares irreversíveis."
    },
    {
        "pergunta": "O que é hipoxemia?",
        "opcoes": ["Deficiência de oxigênio nos tecidos", "Baixa concentração de oxigênio no sangue arterial", "Alta concentração de CO2 no sangue", "Redução da frequência cardíaca"],
        "resposta_correta": "Baixa concentração de oxigênio no sangue arterial",
        "explicacao": "Hipoxemia é a baixa pressão parcial de oxigênio (PaO2) no sangue arterial, geralmente refletida pela baixa SpO2 (< 93%)."
    },
    {
        "pergunta": "A broncoaspiração ocorre quando:",
        "opcoes": ["O ar entra no estômago", "Líquido ou sólido entra nas vias aéreas inferiores", "Há excesso de muco", "Os alvéolos colapsam"],
        "resposta_correta": "Líquido ou sólido entra nas vias aéreas inferiores",
        "explicacao": "Broncoaspiração é a entrada de conteúdo gástrico, saliva ou alimentos na traqueia e pulmões, podendo causar pneumonia química ou infecciosa."
    },
    {
        "pergunta": "A principal causa evitável de Doença Pulmonar Obstrutiva Crônica (DPOC) é:",
        "opcoes": ["Poluição", "Tabagismo", "Genética", "Infecções"],
        "resposta_correta": "Tabagismo",
        "explicacao": "O tabagismo é o fator de risco mais importante para DPOC. O fumo inibe o elevador mucociliar e causa inflamação crônica e destruição alveolar (enfisema)."
    },
    {
        "pergunta": "A dispneia é definida como:",
        "opcoes": ["Respiração rápida", "Dificuldade respiratória subjetiva (falta de ar)", "Respiração ruidosa", "Parada respiratória"],
        "resposta_correta": "Dificuldade respiratória subjetiva (falta de ar)",
        "explicacao": "Dispneia é a sensação subjetiva de falta de ar ou dificuldade para respirar. É um sintoma comum em doenças cardíacas e pulmonares."
    },
    {
        "pergunta": "A taquipneia é caracterizada por:",
        "opcoes": ["Frequência respiratória elevada (> 20 rpm no adulto)", "Frequência cardíaca elevada", "Respiração superficial", "Dificuldade respiratória"],
        "resposta_correta": "Frequência respiratória elevada (> 20 rpm no adulto)",
        "explicacao": "Taquipneia é a respiração acelerada (FR > 20 rpm no adulto), comum em febre, dor, hipóxia e ansiedade."
    },
    {
        "pergunta": "A hiperventilação consiste em:",
        "opcoes": ["Respiração lenta e profunda", "Aumento da ventilação pulmonar, reduzindo CO2", "Respiração com esforço", "Respiração ruidosa"],
        "resposta_correta": "Aumento da ventilação pulmonar, reduzindo CO2",
        "explicacao": "Hiperventilação é o aumento da frequência e/ou profundidade da respiração, levando à eliminação excessiva de CO2 e alcalose respiratória."
    },
    {
        "pergunta": "A principal célula de defesa pulmonar que fagocita partículas estranhas nos alvéolos é:",
        "opcoes": ["Neutrófilo", "Macrófago alveolar", "Linfócito", "Eosinófilo"],
        "resposta_correta": "Macrófago alveolar",
        "explicacao": "Os macrófagos alveolares são células fagocitárias que ingerem bactérias e partículas que chegam aos alvéolos, realizando a limpeza pulmonar."
    },
    {
        "pergunta": "A epiglote tem como função principal:",
        "opcoes": ["Produzir muco", "Fechar a via aérea durante a deglutição", "Aquecer o ar", "Filtrar o ar"],
        "resposta_correta": "Fechar a via aérea durante a deglutição",
        "explicacao": "A epiglote é uma estrutura cartilaginosa que atua como 'tampa', fechando a entrada da laringe durante a deglutição para evitar broncoaspiração."
    },
    {
        "pergunta": "O Diabetes Mellitus é caracterizado por:",
        "opcoes": ["Hipotensão", "Hiperglicemia (níveis elevados de glicose no sangue)", "Hipoglicemia", "Hipertensão"],
        "resposta_correta": "Hiperglicemia (níveis elevados de glicose no sangue)",
        "explicacao": "Diabetes é um distúrbio metabólico crônico caracterizado por hiperglicemia, devido à deficiência de insulina ou resistência à sua ação."
    },
    {
        "pergunta": "A glicemia capilar é um teste que utiliza uma gota de sangue obtida preferencialmente:",
        "opcoes": ["Polpa digital central", "Lateral da polpa digital", "Lóbulo da orelha", "Calcanhar"],
        "resposta_correta": "Lateral da polpa digital",
        "explicacao": "A punção deve ser feita na lateral da polpa digital (não no centro), pois é menos dolorosa e menos vascularizada, evitando lesões e hematomas."
    },
    {
        "pergunta": "Resultados falsos de glicemia capilar podem ocorrer se o dedo estiver contaminado com:",
        "opcoes": ["Álcool gel", "Resíduo de alimento (açúcar)", "Água", "Sabonete antisséptico"],
        "resposta_correta": "Resíduo de alimento (açúcar)",
        "explicacao": "Resíduos de açúcar ou carboidratos nas mãos podem elevar falsamente a glicemia capilar. Lave e seque bem as mãos antes da punção."
    },
    {
        "pergunta": "A hemoglobina glicada (HbA1c) reflete o controle glicêmico médio dos últimos:",
        "opcoes": ["15 dias", "1 mês", "3 meses", "6 meses"],
        "resposta_correta": "3 meses",
        "explicacao": "A HbA1c é um marcador que reflete a média da glicemia nos últimos 3 meses, pois as hemácias vivem em média 120 dias. É o padrão-ouro para avaliação do controle do diabetes."
    },
    {
        "pergunta": "Qual valor de glicemia de jejum é considerado diagnóstico de Diabetes Mellitus?",
        "opcoes": ["> 100 mg/dl", "> 110 mg/dl", "≥ 126 mg/dl", "≥ 200 mg/dl"],
        "resposta_correta": "≥ 126 mg/dl",
        "explicacao": "Para diagnóstico de diabetes, glicemia de jejum ≥ 126 mg/dL confirmada em duas ocasiões, ou glicemia casual ≥ 200 mg/dL com sintomas de hiperglicemia."
    },
    {
        "pergunta": "Na glicemia capilar, qual fator pode causar um falso resultado de glicemia alta?",
        "opcoes": ["Dedos frios", "Hematócrito baixo", "Hipertrigliceridemia", "Altitude elevada"],
        "resposta_correta": "Hipertrigliceridemia",
        "explicacao": "Triglicerídeos elevados podem interferir na reação enzimática das tiras, causando leitura falsamente elevada (ou baixa, dependendo do método)."
    }
]

# ============================================================
# LÓGICA DO QUIZ COM EMBARALHAMENTO E HISTÓRICO
# ============================================================

def main():

    # --- INICIALIZAÇÃO DO ESTADO DA SESSÃO ---
    if "indice" not in st.session_state:
        st.session_state.indice = 0
        st.session_state.pontuacao = 0
        st.session_state.finalizado = False
        st.session_state.scored = {}
        st.session_state.perguntas_embaralhadas = []  # Lista que vai armazenar as perguntas na ordem sorteada
        
    # --- INICIALIZAÇÃO DO HISTÓRICO E HIGH SCORE ---
    if "high_score" not in st.session_state:
        st.session_state.high_score = 0
    if "historico" not in st.session_state:
        st.session_state.historico = []  # Lista para armazenar as últimas pontuações

    # --- EMBARALHAR AS PERGUNTAS NA PRIMEIRA VEZ QUE O APP RODA ---
    if not st.session_state.perguntas_embaralhadas:
        # Cria uma cópia e embaralha
        perguntas_temp = PERGUNTAS_ORIGINAIS.copy()
        random.shuffle(perguntas_temp)
        st.session_state.perguntas_embaralhadas = perguntas_temp

    # Atalho para a lista embaralhada
    PERGUNTAS = st.session_state.perguntas_embaralhadas

    # --- TÍTULO E INFORMAÇÕES ---
    st.title("💉 Quiz Master - 100 Perguntas")
    st.markdown("### 🧠 Estude de forma interativa com perguntas aleatórias!")

    # Exibe High Score no topo
    if st.session_state.high_score > 0:
        st.markdown(f'<div class="high-score-box">🏆 <b>RECORDE DO FLIPERAMA:</b> {st.session_state.high_score} acertos!</div>', unsafe_allow_html=True)

    st.markdown("---")

    # --- SE O QUIZ TERMINOU ---
    if st.session_state.finalizado:
        st.balloons()
        st.header("🏁 Resultado Final")
        
        total = len(PERGUNTAS)
        acertos = st.session_state.pontuacao
        percentual = int((acertos / total) * 100)

        # Verifica e atualiza o recorde (High Score)
        if acertos > st.session_state.high_score:
            st.session_state.high_score = acertos
            st.success(f"🎉 **NOVO RECORDE!** {acertos} acertos! Incrível!")

        # Salva a pontuação atual no histórico (mantém últimas 5 partidas)
        st.session_state.historico.append(acertos)
        if len(st.session_state.historico) > 5:
            st.session_state.historico.pop(0)

        # Classificação
        if acertos >= 90:
            icon = "👑"
            msg = "Enfermeira Master! Você é uma verdadeira especialista!"
        elif acertos >= 70:
            icon = "🌟"
            msg = "Excelente! Você está muito bem preparada!"
        elif acertos >= 50:
            icon = "💪"
            msg = "Bom trabalho! Continue revisando para fixar ainda mais."
        elif acertos >= 30:
            icon = "📚"
            msg = "Está no caminho certo! Revise os temas com mais calma."
        else:
            icon = "🤝"
            msg = "Todo mundo começa de algum lugar! Estude e tente novamente."

        st.markdown(f"## {icon} Você acertou **{acertos}** de **{total}** perguntas (**{percentual}%**)")
        st.markdown(f"### {msg}")

        # Exibe o histórico de pontuações (últimas 5 jogadas)
        st.markdown("---")
        st.markdown("### 📊 Histórico das últimas partidas")
        historico_invertido = reversed(st.session_state.historico)
        historico_str = " → ".join([f"{h}%" for h in historico_invertido])
        st.markdown(f'<div class="historico-box">📈 {historico_str}</div>', unsafe_allow_html=True)
        
        if st.button("🔄 Jogar Novamente (Perguntas Embaralhadas)", use_container_width=True):
            # Reseta tudo e embaralha de novo
            st.session_state.indice = 0
            st.session_state.pontuacao = 0
            st.session_state.finalizado = False
            st.session_state.scored = {}
            # Embaralha novamente
            perguntas_temp = PERGUNTAS_ORIGINAIS.copy()
            random.shuffle(perguntas_temp)
            st.session_state.perguntas_embaralhadas = perguntas_temp
            st.rerun()
        return

    # --- LÓGICA DA PERGUNTA ATUAL ---
    idx = st.session_state.indice
    pergunta_atual = PERGUNTAS[idx]

    # Barra de progresso (calcula com base no índice)
    progresso = (idx + 1) / len(PERGUNTAS)
    st.progress(progresso)
    st.caption(f"Pergunta {idx + 1} de {len(PERGUNTAS)}")

    # Exibe a pergunta
    st.subheader(pergunta_atual["pergunta"])

    # Verifica se esta pergunta já foi respondida
    ja_respondida = st.session_state.scored.get(idx, False)
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
    if resposta is not None and not ja_respondida:
        if resposta == pergunta_atual["resposta_correta"]:
            st.session_state.pontuacao += 1
        st.session_state.scored[idx] = True
        st.rerun()

    # --- EXIBE O FEEDBACK ---
    if ja_respondida:
        resposta_selecionada = st.session_state.get(radio_key, None)
        correta = pergunta_atual["resposta_correta"]

        if resposta_selecionada == correta:
            st.markdown('<div class="feedback-certo">✅ <b>Resposta correta!</b> 🎉</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="feedback-errado">❌ <b>Ops, não foi dessa vez!</b> A resposta correta é: <b>{correta}</b></div>', unsafe_allow_html=True)

        st.markdown(f'<div class="explicacao-box">📘 <b>Explicação detalhada:</b><br>{pergunta_atual["explicacao"]}</div>', unsafe_allow_html=True)

        # Botão para avançar
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("➡️ Próxima pergunta", use_container_width=True):
                if idx + 1 < len(PERGUNTAS):
                    st.session_state.indice += 1
                    st.rerun()
                else:
                    st.session_state.finalizado = True
                    st.rerun()

    # Rodapé com pontuação parcial
    st.markdown("---")
    st.caption(f"✅ Pontuação atual: {st.session_state.pontuacao} acertos | 🏅 Recorde: {st.session_state.high_score}")

if __name__ == "__main__":
    main()
