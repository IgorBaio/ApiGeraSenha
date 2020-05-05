import os
from random import randint
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

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

#
#3100/Brasil-1958-1963
# A-10
# A-20-1985-1995
# Alvorada-1961-1963
# Amazona-1959-1963
# Astra-1998-2011
# Beretta
# Blazer-1995-2011
# Bonanza-1989-1994
# Bolt-2019
# C-10-1974-1988
# C-14-1964-1973
# C-1416-1964-1994
# C-15-1964-1973
# C-20-1985-1995
# Camaro-2010- 
# Caravan-1975-1992
# Celta-2000-2015
# Chevette-Hatch-1980-1988
# Chevette-1973-1993
# Chevette-Junior-1992-1993
# Chevy-500-1983-1995
# Cobalt-2011-2020
# Corisco-?-1963
# Corsa-1994-2012
# Corsa-Sedan-Classic-1995-2011
# Corsa-Pick-up-1995-2002
# Corsa-Wagon-1997-2001
# Cruze-2011-
# Cruze-Sport6-2012-
# D-10-1980-1985
# D-20-1985-1995
# Ipanema-1990-1998
# Kadett-1989-1998
# Kadett-Conversível-1991-1995
# Marajó-1981-1989
# Meriva-2002-2012
# Montana-2003-
# Monza-Sedan-1983-1996
# Monza-Hatch-1982-1988
# Omega-1992-1998-1998-2012
# Onix-2012-
# Opala-Coupe-1971-1988
# Opala-1968-1992
# Prisma-2006-
# Silverado1997-2001
# S10-1995-
# Spin-2012-
# Suprema-1993-1996
# TrailBlazer-2012-
# Vectra-1993-2011
# Vectra-GT-2007-2011
# Veraneio-1964-1994
# Volt
# Zafira-2001-2012
# Equinox-2017
# SS10
# Caprice
# Malibu-2010-2012
#
#


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
    "A-10",
    "A-20-1985-1995",
    "Alvorada-1961-1963",
    "Amazona-1959-1963",
    "Astra-1998-2011",
    'Beretta',
    'Blazer-1995-2011',
    'Bonanza-1989-1994',
    'Bolt-2019',
    'C-10-1974-1988',
    'C-14-1964-1973',
    'C-1416-1964-1994',
    'C-15-1964-1973',
    'C-20-1985-1995',
    'Camaro-2010' ,
    'Caravan-1975-1992',
    'Celta-2000-2015',
    'Chevette-Hatch-1980-1988',
    'Chevette-1973-1993',
    'Chevette-Junior-1992-1993',
    'Chevy-500-1983-1995',
    'Cobalt-2011-2020',
    'Corisco-?-1963',
    'Corsa-1994-2012',
    'Corsa-Sedan-Classic-1995-2011',
    'Corsa-Pick-up-1995-2002',
    "Corsa-Wagon-1997-2001",
    "Cruze-2011",
    "Cruze-Sport6-2012-",
    "D-10-1980-1985",
    "D-20-1985-1995",
    "Ipanema-1990-1998",
    "Kadett-1989-1998",
    "Kadett-Conversível-1991-1995",
    "Marajó-1981-1989",
    "Meriva-2002-2012",
    "Montana-2003",
    "Monza-Sedan-1983-1996",
    "Monza-Hatch-1982-1988",
    "Omega-1992-1998-1998-2012",
    "Onix-2012",
    "Opala-Coupe-1971-1988",
    "Opala-1968-1992",
    "Prisma-2006",
    "Silverado1997-2001",
    "S10-1995",
    "Spin-2012",
    "Suprema-1993-1996",
    "TrailBlazer-2012",
    "Zafira-2001-2012",
    "Equinox-2017",
    "SS10",
    "Caprice",
    "Malibu-2010-2012"
    ]

def GetSenha(tipoSenha):
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
    if tipoSenha == 'SenhaBanda':
        if numOrdemSenha % 2 == 0 and not numOrdemSenha % 3 == 0:
            senha = c1+numeros[numNumeros]+bandas[numBanda]+caractere[numCaractere2]+caractere[numCaractere3]
        elif numOrdemSenha % 3 == 0 and not numOrdemSenha % 2 == 0:
            senha = caractere[numCaractere]+caractere[numCaractere2]+bandas[numBanda]+numeros[numNumeros]+caractere[numCaractere3]
        else:
            senha = caractere[numCaractere]+caractere[numCaractere2]+numeros[numNumeros]+bandas[numBanda]+caractere[numCaractere3]

    elif tipoSenha == 'SenhaCarro':
        if numOrdemSenha % 2 == 0 and not numOrdemSenha % 3 == 0:
            senha = c1+numeros[numNumeros]+carros[numCarro]+caractere[numCaractere2]+caractere[numCaractere3]
        elif numOrdemSenha % 3 == 0 and not numOrdemSenha % 2 == 0:
            senha = caractere[numCaractere]+caractere[numCaractere2]+carros[numCarro]+numeros[numNumeros]+caractere[numCaractere3]
        else:
            senha = caractere[numCaractere]+caractere[numCaractere2]+numeros[numNumeros]+carros[numCarro]+caractere[numCaractere3]

    elif tipoSenha == 'SenhaMix':
        if numOrdemSenha % 2 == 0 and not numOrdemSenha % 3 == 0:
            senha = c1+numeros[numNumeros]+carros[numCarro]+caractere[numCaractere2]+bandas[numBanda]+caractere[numCaractere3]
        elif numOrdemSenha % 3 == 0 and not numOrdemSenha % 2 == 0:
            senha = caractere[numCaractere]+bandas[numBanda]+caractere[numCaractere2]+carros[numCarro]+numeros[numNumeros]+caractere[numCaractere3]
        else:
            senha = caractere[numCaractere]+carros[numCarro]+caractere[numCaractere2]+numeros[numNumeros]+caractere[numCaractere3]+bandas[numBanda]

    return senha

@app.route("/", methods=["GET"])
def Welcome():
    return "<h1>Hello World!</h1><br /><h3>Para acessar as senhas, basta acrescentar na URL '/SenhaBanda' ou '/SenhaCarro' ou '/SenhaMix'"


@app.route("/SenhaBanda", methods=['GET'])
def SenhaBanda():
    return jsonify(GetSenha("SenhaBanda")), 200

@app.route("/SenhaCarro", methods=['GET'])
def SenhaCarro():
    return jsonify(GetSenha("SenhaCarro")), 200

@app.route("/SenhaMix", methods=['GET'])
def SenhaMix():
    return jsonify(GetSenha("SenhaMix")), 200

def main():
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)


if __name__ == '__main__':
    # app.run(debug=True)
    main()
