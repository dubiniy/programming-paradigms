def getCoefficient(name):
    while True:
        try:
            coef = input("Введите коэффициент " + name + ": ")
            return float(coef)
        except ValueError:
            print("Ошибка! Введите число еще раз: ")

def findRootsFunctional(t):
    match t:
        case _ if t > 0:
            return [t**0.5, -(t**0.5)]
        case 0.0:
            return [0.0]
        case _:
            return []

def biquadraticSolutionFunctional(a, b, c):
    match a:
        case 0:
            match b:
                case 0:
                    return "Бесконечное кол-во корней" if c == 0 else "Корней нет"
                case _:
                    t = -c / b
                    return findRootsFunctional(t)
        case _:
            d = b**2 - 4*a*c
            
            match d:
                case _ if d < 0:
                    return "Действительных корней нет"
                case 0:
                    t = -b / (2 * a)
                    roots = findRootsFunctional(t)
                case _:
                    t1 = (-b + d**0.5) / (2 * a)
                    t2 = (-b - d**0.5) / (2 * a)
                    # Складываем списки корней
                    roots = findRootsFunctional(t1) + findRootsFunctional(t2)
            
            roots = list(set(roots))
            
            if not roots:
                match roots:
                    case []: return "Действительных корней нет"
            return roots

def main():
    a = getCoefficient('A')
    b = getCoefficient('B')
    c = getCoefficient('C')

    print("Уравнение: "+str(a)+"x^4 + "+str(b)+"x^2 +"+str(c)+" = 0")
    result = biquadraticSolutionFunctional(a, b, c)

    if type(result) == str:
        print(result)
    elif len(result) == 0:
        print("Действительных корней нет")
    else:
        print("Действительные корни уравнения:", result)

if __name__ == "__main__":
    main()
