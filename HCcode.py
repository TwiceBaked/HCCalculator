import time

INSTRUCTIONS = """
*************************************
      --Health Risk Calculator--    

    Answer the following questions
   and this program will calculate
           your health risk.
*************************************
"""
print(INSTRUCTIONS)

StringNumberList = [str(x) for x in range(1000 + 1)]

def CheckAnswerInt(IntAnswer):
    while IntAnswer not in StringNumberList:
        IntAnswer = input("*!Error!* Please enter an integer: ")
    
    return int(IntAnswer)

def CheckYesNo(Answer):
    ExeceptedAnswer = ["YES", "yes", "Y", "y", "Yes", "yES", "NO", "no", "N", "n", "No", "nO"]
    YesList = ["YES", "yes", "Y", "y", "Yes", "yES"]
    NoList = ["NO", "no", "N", "n", "No", "nO"]
    YesAnswer = "YES"
    NoAnswer = "NO"

    while Answer not in ExeceptedAnswer:
        Answer = str(input("*!ERROR!* Answer must be either YES or NO: "))
        continue

    if Answer in YesList:
        return YesAnswer

    elif Answer in NoList:
        return NoAnswer

while True:
    Age = CheckAnswerInt(str(input("Enter your age in years: ")))
    Height = input("Enter your height in feet and inches (separated by a space): ")

    Hsplit = Height.split(' ')
    Fstr = Hsplit[0]
    Istr = Hsplit[1]

    if Fstr and Istr in StringNumberList:
        pass
    else:
        while Fstr and Istr not in StringNumberList:
            Height = input("*!ERROR!* Please enter your height with a space separating the two numbers: ")
            Hsplit = Height.split(' ')
            Fstr = Hsplit[0]
            Istr = Hsplit[1]
            if Fstr and Istr in StringNumberList:
                break

    Weight = CheckAnswerInt(str(input("Enter you weight in lbs: ")))
    BloodPressure = input("Enter your blood pressure (Upper then Lower separated by a space): ")

    Bloodsplit = BloodPressure.split(' ')
    UpperStr = Bloodsplit[0]
    LowerStr = Bloodsplit[1]

    if UpperStr and LowerStr in StringNumberList:
        pass
    else:
        while UpperStr or LowerStr not in StringNumberList:
            BloodPressure = input("*!ERROR!* Please enter your upper and lower blood pressures separated by a space: ")
            Bloodsplit = BloodPressure.split(' ')
            UpperStr = Bloodsplit[0]
            LowerStr = Bloodsplit[1]
            if UpperStr and LowerStr in StringNumberList:
                break

    Diabetes = CheckYesNo(str(input("Does your family have a history of Diabetes: YES/NO: ")))
    Cancer = CheckYesNo(str(input("Does your family have a history of Cancer: YES/NO: ")))
    Alzheimers = CheckYesNo(str(input("Does your family have a history of Alzhimer's: YES/NO: ")))

    WeightKG = Weight / 2.2
    WeightKGLimit = round(WeightKG, 2)

    Hsplit = Height.split(' ')

    F = int(Hsplit[0])
    I = int(Hsplit[1])

    F2 = I / 12
    Ftotal = F + F2
    HeightMeters = Ftotal * 0.3048

    BMI = WeightKG / (HeightMeters ** 2)
    BMILimit = round(BMI, 2)

    if 24.9 > BMI >= 18.5:
        BMIPoints = 0
    elif 29.9 > BMI >= 24.9:
        BMIPoints = 30
    elif 34.9 >= BMI >= 30.0:
        BMIPoints = 75
    else:
        BMIPoints = 100

    Bloodsplit = BloodPressure.split(' ')

    Upper = int(Bloodsplit[0])
    Lower = int(Bloodsplit[1])

    if Upper < 120 and Lower <= 80:
        BloodP = 0
    elif 129 > Upper >= 120 and Lower <= 80:
        BloodP = 15
    elif 139 > Upper >= 129 or 89 >= Lower > 80:
        BloodP = 30
    elif 180 > Upper >= 139 or 120 > Lower >= 90:
        BloodP = 75
    elif Upper >= 180 or Lower >= 120:
        BloodP = 100

    if Age < 30:
        AgeP = 0
    elif 45 > Age >= 30:
        AgeP = 10
    elif 60 > Age >= 45:
        AgeP = 20
    else:
        AgeP = 30

    if Diabetes == "YES":
        DP = 10
    elif Diabetes == "NO":
        DP = 0

    if Cancer == "YES":
        CP = 10
    elif Cancer == "NO":
        CP = 0

    if Alzheimers == "YES":
        AP = 10
    elif Alzheimers == "NO":
        AP = 0

    TotalP = AgeP + BMIPoints + BloodP + DP + CP + AP

    print("\nCALCULATING...")
    time.sleep(1)

    print("\nAge: " + str(Age))
    print("Height: " + str(Hsplit[0]) + "'" + str(Hsplit[1]) + '"')
    print("Weight: " + str(Weight))
    print("BMI: " + str(BMILimit))
    print("Blood Pressure: " + str(Upper) + " Over " + str(Lower))

    if TotalP <= 20:
        print("\nYou are low risk\n")
    elif 20 < TotalP <= 50:
        print("\nYou are moderate risk\n")
    elif 50 < TotalP <= 75:
        print("\nYou are high risk\n")
    else:
        print("\nYour risk is unisurable\n")

    Again = CheckYesNo(str(input("Would you like to calculate another person's risk? YES/NO: ")))

    if Again == "YES":
        continue
    elif Again == "NO":
        break