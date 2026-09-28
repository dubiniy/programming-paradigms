class BiquadraticEquation:
    def __init__(self):
        self.a = self.getCoefficient("A")
        self.b = self.getCoefficient("B")
        self.c = self.getCoefficient("C")

    def getCoefficient(self, name):
        while True:
            try:
                coef = input("Введите коэффициент " + name + ": ")
                return float(coef)
            except ValueError:
                print("Ошибка! Введите число еще раз: ")

    def findRoots(self, t):
        if t > 0:
            return [t**0.5, -(t**0.5)]
        elif t == 0:
            return [0.0]
        return []

    def solve(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Бесконечное кол-во корней"
                else: 
                    return "Корней нет"
            else:
                t = -self.c / self.b
                return self.findRoots(t)

        d = self.b**2 - 4 * self.a * self.c
        if d < 0:
            return "Действительных корней нет"

        roots = []
        if d == 0:
            t = -self.b / (2 * self.a)
            roots.extend(self.findRoots(t))
        else:
            t1 = (-self.b + d**0.5) / (2 * self.a)
            t2 = (-self.b - d**0.5) / (2 * self.a)
            roots.extend(self.findRoots(t1))
            roots.extend(self.findRoots(t2))
            
        roots = list(set(roots))
        
        if not roots:
            return "Действительных корней нет"
        return roots

def main():
    equation = BiquadraticEquation()
    
    print("Уравнение: " + str(equation.a) + "x^4 + " + str(equation.b) + "x^2 + " + str(equation.c) + " = 0")
    
    result = equation.solve()

    if type(result) == str:
        print(result)
    elif len(result) == 0:
        print("Действительных корней нет")
    else:
        print("Действительные корни уравнения:", result)

if __name__ == "__main__":
    main()
