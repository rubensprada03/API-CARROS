from fastapi import FastAPI

app = FastAPI()

toyota = [
    {
        "id": 1,
        "Marca": "Toyota",
        "Modelo": "Corolla - Altis",
        "Motor": "2.0 Dual VVT-iE 16V DOHC Flex (Dynamic Force",
        "Ano": 2021,
        "Fipe": "152.400",
    },

    {
        "id": 2,
        "Marca": "Toyota",
        "Modelo": "Hillux - SRX",
        "Motor": "2.8 16V turbodiesel ",
        "Ano": 2022,
        "Fipe": "304.159",
    },

    {
        "id": 3,
        "Marca": "Toyota",
        "Modelo": "SW4 - SRX",
        "Motor": "motor 2.8 de 204 cv a diesel",
        "Ano": 2022,
        "Fipe": "389.790",
    },

    {
        "id": 4,
        "Marca": "Toyota",
        "Modelo": "Supra - MK5",
        "Motor": "mB58 3.0 litros. Potência Máxima: 340 cv e 387 cv. Torque Máximo: 50,3 kgfm e 50,9 kgfm",
        "Ano": 2022,
        "Resselers": "1.000.000",
    },

]

lamborghini = [
    {
        "id": 5,
        "Marca": "Lamborghini",
        "Modelo": "Huracan - EVO",
        "Motor":  "V10 5.2 aspirado gerando 640 cv a 8.500 rpm e 57,6 kgfm a 6.500 rpm",
        "Ano": 2014,
        "Fipe": "5.400.000",
    },

    {
        "id": 6,
        "Marca": "Lamborghini",
        "Modelo": "Aventador - SVJ",
        "Motor": "central traseira, longitudinal, gasolina, V12, 6.498 cm3, 48V, 95 x 76,4 mm, 11,8:1, 770 cv a 8.550 rpm, 73,4 mkgf a 6.750 rpm",
        "Ano": 2020,
        "Fipe": "8.200.000",
    },

    {
        "id": 7,
        "Marca": "Lamborghini",
        "Modelo": "Urus",
        "Motor": "V8 de 666 cv",
        "Ano": 2022,
        "Fipe": "3.500.000"
    },

    {
        "id": 8,
        "Marca": "Lamborghini",
        "Modelo": "Countach",
        "Motor": "12 6.5 de 769 cv auxiliado por motor elétrico",
        "Ano": 2022,
         "Fipe": "16.340.000"
    },

]

mercedes = [
    {
        "id": 9,
        "Marca": "Mercedes",
        "Modelo": "G63",
        "Motor": "r 4.0 V8 twin-turbo desenvolve 593 cv de potência e 86,6 kgfm de torque",
        "Ano": 2021,
        "Fipe": "1.990.000",
    },

    {
        "id": 10,
        "Marca": "Mercedes",
        "Modelo": "G63-GT",
        "Motor": "4.0 V8 twin-turbo desenvolve 593 cv de potência e 86,6 kgfm de torque",
        "Ano": 2020,
        "Fipe": "1.972.815",
    },

    {
        "id": 11,
        "Marca": "Mercedes",
        "Modelo": "Gle 63",
        "Motor": "V8 biturbo de 4.0 litros",
        "Ano": 2022,
        "Fipe": "1.184.000"
    },

    {
        "id": 12,
        "Marca": "Mercedes",
        "Modelo": "AMG - GT",
        "Motor": "4.0 V8 de 730 cv, alcançando os 100 kmqh em 3,2 segundos",
        "Ano": 2020,
        "Fipe": "1.553.109"
    },

    {
        "id": 13,
        "Marca": "Mercedes",
        "Modelo": "C 180",
        "Motor": "Motor 1.6 Turbo Flex de 156 cv e 25,5 kgfm",
        "Ano": 2021,
        "Fipe": "279,835"
    }
]
#CONSULTAS TOYOTA
@app.get("/toyota")
def carros_toyota():
    return(toyota)

@app.get("/toyota/{modelo}")
def carros_toyota(modelo: str):
    # Filtra a lista de carros da Toyota pelo modelo especificado
    carros_filtrados = [carro for carro in toyota if carro["Modelo"].lower() == modelo.lower()]
    return carros_filtrados
#=======================================================================================================================

#CONSULTAS LAMBO
@app.get("/lamborghini")
def carros_lamborghini():
    return(lamborghini)

@app.get("/lamborghini/{modelo}")
def carros_lamborghini(modelo: str):
    # Filtra a lista de carros da Toyota pelo modelo especificado
    carros_filtrados = [carro for carro in lamborghini if carro["Modelo"].lower() == modelo.lower()]
    return carros_filtrados
#=======================================================================================================================

#TODOS OS CARROS FILTRO
@app.get("/carros")
def todos_carros():
    return(toyota,lamborghini, mercedes)
#=======================================================================================================================

#CONSULTAS MERCEDES
@app.get("/mercedes")
def carros_mercedes():
    return(mercedes)

@app.get("/mercedes/{modelo}")
def carros_mercedes(modelo: str):
    # Filtra a lista de carros da Toyota pelo modelo especificado
    carros_filtrados = [carro for carro in mercedes if carro["Modelo"].lower() == modelo.lower()]
    return carros_filtrados

#=======================================================================================================================