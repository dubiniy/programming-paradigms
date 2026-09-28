def getCoefficient(name):
    while True:
        try:
            coef = input("Введите коэффициент "+name+": ")
            return float(coef)
        except ValueError:
            print("Ошибка! Введите число еще раз: ")

def findRoots(t):
    if t>0:
        return [t**0.5, -(t**0.5)]
    elif t==0:
        return [0.0]
    return []

def biquadraticSolution(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                return "Бесконечное кол-во корней"
            else: 
                return "Корней нет"
        else:
            t = -c/b
            return findRoots(t)
    d = b**2 - 4*a*c
    if d < 0:
        return "Действительных корней нет"

    roots = []
    if d == 0:
        t = -b / (2*a)
        roots.extend(findRoots(t))
    else:
        t1 = (-b + d**0.5) / (2*a)
        t2 = (-b - d**0.5) / (2*a)
        roots.extend(findRoots(t1))
        roots.extend(findRoots(t2))
        
    roots = list(set(roots))
    
    if not roots:
        return "Действительных корней нет"
    return roots
def main():
    a = getCoefficient('A')
    b = getCoefficient('B')
    c = getCoefficient('C')

    print("Уравнение: "+str(a)+"x^4 + "+str(b)+"x^2 + "+str(c)+" = 0")
    result = biquadraticSolution(a,b,c)

    if type(result) == str:
        print(result)
    elif len(result) == 0:
        print("Действительных корней нет")
    else:
        print("Действительные корни уравнения: ", result)

if __name__ == "__main__":
    main()