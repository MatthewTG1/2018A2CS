#Matthew S3C5 Recursion
def factorial(n):
    if (n==0):
        return 1

    return n*(factorial(n-1))

def bunnyEars(x):
    if (x == 0):
        return 0

    return bunnyEars(x-1)+2

def fibonacci(x):
    if (x==0):
        return 0
    if (x==1):
        return 1

    return fibonacci(x-1)+fibonacci(x-2)

def bunnyEars2(x):
    if (x==0):
        return 0
    if x%2 == 1:
        return bunnyEars2(x-1)+2
    if x%2 == 0:
        return bunnyEars2(x-1)+3

def triangle(x):
    if(x==0):
        return 0
    return triangle(x-1)+x

def sumDigits(x):
    if (x==0):
        return 0
    return sumDigits(int(x/10)) + x%10

def count7(x):
    if (x==0):
        return 0
    if x%10 == 7:
        return 1+count7(int(x/10))
    else:
        return count7(int(x/10))

def count8(x):
    if (x==0):
        return 0
    if x%10 == 8:
        if (x//10)%10 == 8:
            return 2+count8(int(x/10))
        else:
            return 1+count8(int(x/10))
    return count8(int(x/10))

def powerN(x,n):
    if n == 0:
        return 1

    return x*powerN(x,n-1)

def countX(x):
    if len(x) == 0:
        return 0
    if x[len(x)-1] == "x":
        return 1+countX(x[:-1])
    return countX(x[:-1])

def countHi(x):
    if len(x) == 0:
        return 0
    if x[len(x)-2] == "h" and x[len(x)-1] == "i":
        return 1 + countHi(x[:-2])
    return countHi(x[:-2])


def changeXY(x):
    if len(x) == 0:
        return ""
    if x[0] == "x":
        return "y" + changeXY(x[1:])
    return x[0] + changeXY(x[1:])


def changePi(x):
    if len(x) == 0:
        return ""
    if x[0] == "p" and x[1] == "i":
        return "3.14" + changePi(x[2:])
    return x[0] + changePi(x[1:])


def noX(x):
    if len(x) == 0:
        return ""
    if x[0] == "x":
        return noX(x[1:])
    return x[0] + noX(x[1:])


def array6(x, n):
    if x[n] == 6:
        return True
    elif n + 1 == len(x):
        return False
    return array6(x, n + 1)


def array11(x, n):
    if n == len(x):
        return 0
    if x[n] == 11:
        return 1 + array11(x, n + 1)
    return array11(x, n + 1)


def array220(x, n):
    if x[n] % 10 == 0:
        return True
    elif n + 1 == len(x):
        return False
    return array220(x, n + 1)


def allStar(x):
    if len(x) == 1:
        return x

    return x[0] + "*" + allStar(x[1:])


def pairStar(x):
    if len(x) == 1:
        return x
    if x[0] == x[1]:
        return x[0] + "*"  + pairStar(x[1:])
    return x[0]+pairStar(x[1:])

def endX(x):
    if len(x) == 0:
        return ""
    if x[0] == "x":
        return endX(x[1:]) + "x"
    return x[0]+endX(x[1:])

def countPairs(x):
    if len(x) == 2:
        return 0
    if x[0] == x[2]:
        return 1 + countPairs(x[1:])
    return countPairs(x[1:])

def countAbc(x):
    if len(x) == 2:
        return 0
    if x[0] + x[1] + x[2] == "abc" or "aba":
        return 1+ countAbc(x[3:])
    return countAbc(x[3:])

def count11(x):
    if len(x) <= 1:
        return 0
    if x[0] + x[1] == "11":
        return 1 + count11(x[2:])
    return count11(x[1:])

def stringClean(x):
    if len(x) == 1:
        return x
    if x[0] == x[1]:
        return stringClean(x[1:])
    return x[0] + stringClean(x[1:])

def countHi2(x):
    if len(x) == 1:
        return 0
    if x[0] + x[1] == "hi":
        return 1+countHi2(x[1:])
    if x[0] == "x":
        return countHi2(x[2:])
    return countHi2(x[1:])

def parenBit(x):
    if len(x) == 0:
        return ""
    if x[0] == "(" and x[-1] == ")":
        return x
    if x[0] == "(":
        return parenBit(x[:-1])
    if x[-1] == ")":
        return parenBit(x[1:])
    return parenBit(x[1:-1])

def nestParen(x):
    if len(x) <= 3 and x[0] == "(" and x[-1] == ")":
        return True
    elif len(x) <= 3:
        return False
    if x[0] == "(" and x[-1] == ")":
        return nestParen(x[1:-1])
    return False

def strCount(x,s):
    if len(x) < len(s):
        return 0
    if s == x[:len(s)]:
        return 1+ strCount(x[len(s):],s)
    return strCount(x[len(s):],s)

def strCopies(string,sub,n):
	if len(sub) > len(string) and n != 0:
		return False
	elif len(sub) > len(string) and n == 0:
		return True

	if sub == string[:len(sub)]:
		return strCopies(string[1:],sub,n-1)
	return strCopies(string[1:],sub,n)

def strDist(string,sub):
	if len(sub) > len(string):
		return 0

	if sub == string[-len(sub):] and sub == string[:len(sub)]:
		return len(string)
	elif sub == string[:len(sub)]:
		return strDist(string[:-1],sub)
	elif sub == string[-len(sub):]:
		return strDist(string[1:],sub)
	return strDist(string[1:-1],sub)




print(factorial(4))
print(bunnyEars(5))
print(fibonacci(6))
print(bunnyEars2(4))
print(triangle(3))
print(sumDigits(1223))
print(count7(7677))
print(count8(8848))
print(powerN(3, 4))
print(countX("xhxhxhxh"))
print(countHi("hisdhischi"))
print(changeXY("xxagxx"))
print(changePi("piscpispi"))
print(noX("xshxshx"))
print(array6([6, 4], 0))
print(array11([11, 2, 11, 11], 0))
print(array220([2, 30, 4, 15], 0))
print(allStar("absc"))
print(pairStar("heelllo"))
print(endX("xhsxxja"))
print(countPairs("sasaha"))
print(countAbc("abcssabaabc"))
print(count11("111ab11"))
print(stringClean("aabbccc"))
print(countHi2("ahixhihi"))
print(parenBit("asd(has)sja"))
print(nestParen("(((x))"))
print(strCount("abcsdsabc","abc"))
print(strCopies("catcowcat","cat",1))
print(strDist("cccatcowcatxx","cat"))