def division(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("a n'est pas un reel")
    if not isinstance(b, (int, float)):
        raise TypeError("b n'est pas un reel")
    return a / b

if __name__ == "__main__":
    v1 = 10
    v2 = 2
    try:
        res = division(v1, v2)
    except ZeroDivisionError:
        print("division par 0 impossible")
    except TypeError as e:
        print("mauvais type :", e)
    except Exception as e:
        print("autre probleme :", e)
    else:
        print("resultat =", res)
    finally:
        print("fin du script")

    try:
        division(5, 0)
    except ZeroDivisionError:
        print("erreur zero bien capturee")

    try:
        division("cinq", 2)
    except TypeError as e:
        print("erreur type bien capturee :", e)