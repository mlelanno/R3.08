class Point:
    def __init__(self, x=0.0, y=0.0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("coordonnee invalide")
        self.__x = float(x)
        self.__y = float(y)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise TypeError("x doit etre un reel")
        self.__x = float(x)

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise TypeError("y doit etre un reel")
        self.__y = float(y)

    def distanceCoord(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("coordonnees invalides")
        return ((self.__x - a) ** 2 + (self.__y - b) ** 2) ** 0.5

    def distance_coordonnees(self, a, b):
        return self.distanceCoord(a, b)

    def distancePoint(self, p):
        if not isinstance(p, Point):
            raise TypeError("un Point est obligatoire")
        return self.distanceCoord(p.get_x(), p.get_y())


class Cercle:
    def __init__(self, r=1.0, centre=None):
        if centre is None:
            centre = Point(0.0, 0.0)
        if not isinstance(centre, Point):
            raise TypeError("le centre doit etre un Point")
        if not isinstance(r, (int, float)):
            raise TypeError("rayon non reel")
        if r <= 0:
            raise ValueError("rayon superieur a 0")
        self.__centre = centre
        self.__rayon = float(r)

    def get_rayon(self):
        return self.__rayon

    def set_rayon(self, r):
        if not isinstance(r, (int, float)):
            raise TypeError("rayon non reel")
        if r <= 0:
            raise ValueError("rayon superieur a 0")
        self.__rayon = float(r)

    def get_centre(self):
        return self.__centre

    def set_centre(self, c):
        if not isinstance(c, Point):
            raise TypeError("le centre doit etre un Point")
        self.__centre = c

    def diametre(self):
        return 2 * self.__rayon

    def perimetre(self):
        return 2 * 3.14159 * self.__rayon

    def surface(self):
        return 3.14159 * (self.__rayon ** 2)

    def intersection(self, c):
        if not isinstance(c, Cercle):
            raise TypeError("un Cercle est attendu")
        dist = self.__centre.distancePoint(c.get_centre())
        return dist <= (self.__rayon + c.get_rayon())

    def appartient(self, p):
        if not isinstance(p, Point):
            raise TypeError("un Point est attendu")
        return self.__centre.distancePoint(p) <= self.__rayon


class Rectangle:
    def __init__(self, p=None, a=1.0, b=1.0):
        if p is None:
            self.__bg = Point(0.0, 0.0)
            self.__longueur = 1.0
            self.__hauteur = 1.0
        elif isinstance(a, Point):
            if not isinstance(p, Point):
                raise TypeError("point de depart invalide")
            self.__bg = p
            self.__longueur = float(a.get_x() - p.get_x())
            self.__hauteur = float(a.get_y() - p.get_y())
        else:
            if not isinstance(p, Point):
                raise TypeError("point de depart invalide")
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("cotes non reels")
            self.__bg = p
            self.__longueur = float(a)
            self.__hauteur = float(b)

        if self.__longueur <= 0 or self.__hauteur <= 0:
            raise ValueError("dimensions doivent etre positives")

    def get_bg(self):
        return self.__bg

    def set_bg(self, p):
        if not isinstance(p, Point):
            raise TypeError("un Point est attendu")
        self.__bg = p

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, l):
        if not isinstance(l, (int, float)):
            raise TypeError("longueur non reelle")
        if l <= 0:
            raise ValueError("doit etre positif")
        self.__longueur = float(l)

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, h):
        if not isinstance(h, (int, float)):
            raise TypeError("hauteur non reelle")
        if h <= 0:
            raise ValueError("doit etre positif")
        self.__hauteur = float(h)

    def surface(self):
        return self.__longueur * self.__hauteur

    def perimetre(self):
        return 2 * (self.__longueur + self.__hauteur)

    def point_bas_gauche(self):
        return self.__bg

    def point_bas_droit(self):
        return Point(self.__bg.get_x() + self.__longueur, self.__bg.get_y())

    def point_haut_gauche(self):
        return Point(self.__bg.get_x(), self.__bg.get_y() + self.__hauteur)

    def point_haut_droit(self):
        return Point(self.__bg.get_x() + self.__longueur, self.__bg.get_y() + self.__hauteur)

    def contient_point(self, p):
        if not isinstance(p, Point):
            raise TypeError("un Point est attendu")
        x_dedans = self.__bg.get_x() <= p.get_x() <= (self.__bg.get_x() + self.__longueur)
        y_dedans = self.__bg.get_y() <= p.get_y() <= (self.__bg.get_y() + self.__hauteur)
        return x_dedans and y_dedans


class TriangleRectangle:
    def __init__(self, c1, c2, p=None):
        if not isinstance(c1, (int, float)) or not isinstance(c2, (int, float)):
            raise TypeError("cotes non reels")
        if c1 <= 0 or c2 <= 0:
            raise ValueError("cotes superieurs a 0")
        if p is None:
            self.__point = Point(0.0, 0.0)
        else:
            if not isinstance(p, Point):
                raise TypeError("sommet invalide")
            self.__point = p
        self.__c1 = float(c1)
        self.__c2 = float(c2)

    def get_c1(self):
        return self.__c1

    def set_c1(self, c1):
        if not isinstance(c1, (int, float)):
            raise TypeError("cote non reel")
        if c1 <= 0:
            raise ValueError("doit etre positif")
        self.__c1 = float(c1)

    def get_c2(self):
        return self.__c2

    def set_c2(self, c2):
        if not isinstance(c2, (int, float)):
            raise TypeError("cote non reel")
        if c2 <= 0:
            raise ValueError("doit etre positif")
        self.__c2 = float(c2)

    def get_point(self):
        return self.__point

    def set_point(self, p):
        if not isinstance(p, Point):
            raise TypeError("un Point est attendu")
        self.__point = p

    def hypothenuse(self):
        return (self.__c1 ** 2 + self.__c2 ** 2) ** 0.5

    def perimetre(self):
        return self.__c1 + self.__c2 + self.hypothenuse()

    def surface(self):
        return (self.__c1 * self.__c2) / 2

    def isocele(self):
        return self.__c1 == self.__c2


def main():
    try:
        pt = Point(1.0, 2.0)
        c = Cercle(4.0, pt)
        print("test perimetre cercle =", c.perimetre())
        Cercle(-3.0)
    except ValueError as err:
        print("erreur valeur interceptee :", err)
    except TypeError as err:
        print("erreur type interceptee :", err)

if __name__ == "__main__":
    main()