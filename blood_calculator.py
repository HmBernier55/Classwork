def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Chol_driver()

def input_HDL():
    HDL_input = input("Enter the HDL value: ")
    return int(HDL_input)

def check_HDL(HDL_result):
    if HDL_result >= 60:
        return "Normal"
    elif 40 <= HDL_result < 60:
        return "Borderline Low"
    else:
        return "Low"    
    
def HDL_driver():
    HDL_value = input_HDL()
    answer = check_HDL(HDL_value)
    output_HDL_result(HDL_value, answer)

def output_HDL_result(HDL_value, charac):
    print("The results for an HDL value of {} is {}".format(HDL_value, charac))



def input_LDL():
    LDL_input = input("Enter the LDL value: ")
    return int(LDL_input)

def check_LDL(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result <= 159:
        return "Borderline High"
    elif 160 <= LDL_result <= 189:
        return "High"
    else:
        return "Very High"      
    
def LDL_driver():
    LDL_value = input_LDL()
    answer = check_LDL(LDL_value)
    output_LDL_result(LDL_value, answer)

def output_LDL_result(LDL_value, charac):
    print("The results for an LDL value of {} is {}".format(LDL_value, charac))



def input_chol():
    Chol_input = input("Enter the total cholesterol value: ")
    return int(Chol_input)

def check_Chol(Chol_result):
    if Chol_result < 200:
        return "Normal"
    elif 200 <= Chol_result <= 239:
        return "Borderline High"
    else:
        return "High"

interface()