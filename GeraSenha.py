from random import randint
from flask import Flask, jsonify

app = Flask(__name__)


bandas = [
    "Metallica",
    "Guns'nRoses",
    "LedZeppelin",
    "Ledzeppelin",
    "ledZeppelin",
    "SkidRow",
    "RHCP",
    "Offspring",
    "NickelBack",
    "Nirvana",
    "PinkFloyd",
    "LegiaoUrbana",
    "CharlieBrownJr",
    "EngenheirosdoHawaii",
    "Pitty",
    "Skank",
    "BaraoVermelho",
    "RoupaNova",
    "CapitalInicial",
    "Rappa",
    "Titas",
    "Raimundos",
    "OsParalamasdoSucesso",
    "MamonasAssassinas",
    "Angra",
    "LosHermanos", 
    
]



numeros = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0"
]

caractere = ["@","#","!","$","%","^","&","*","?","/","'",'"',"[","{","}","}","`","~","<",">","-","_","+","="]

carros = [
    "Ka",
    "ka",
    "Mustang",
    "mustang",

]

def GetSenha():
    numCaractere = randint(0,caractere.__len__()-1)
    numCaractere2 = randint(0,caractere.__len__()-1)
    exit = True
    while exit:
        if numCaractere2 == numCaractere:
            numCaractere2 = randint(0,caractere.__len__()-1)
        else:
            exit = False
    exit = True
    numCaractere3 = randint(0,caractere.__len__()-1)
    while exit:
        if numCaractere2 == numCaractere or numCaractere2 == numCaractere3:
            numCaractere3 = randint(0,caractere.__len__()-1)
        else:
            exit = False
    numCarro = randint(0,carros.__len__()-1)

    numBanda = randint(0,bandas.__len__()-1)
    
    numNumeros = randint(0,numeros.__len__()-1)
    
    numOrdemSenha = randint(0,9)

    c1=caractere[numCaractere]
    if numOrdemSenha % 2 == 0 and not numOrdemSenha % 3 == 0:
        senha = c1+numeros[numNumeros]+bandas[numBanda]+caractere[numCaractere2]+caractere[numCaractere3]
    elif numOrdemSenha % 3 == 0 and not numOrdemSenha % 2 == 0:
        senha = caractere[numCaractere]+caractere[numCaractere2]+bandas[numBanda]+numeros[numNumeros]+caractere[numCaractere3]
    else:
        senha = caractere[numCaractere]+caractere[numCaractere2]+numeros[numNumeros]+bandas[numBanda]+caractere[numCaractere3]

    return senha


@app.route("/Senha", methods=['GET'])
def home():
    return jsonify(GetSenha()), 200

if __name__ == '__main__':
    app.run(debug=True)
