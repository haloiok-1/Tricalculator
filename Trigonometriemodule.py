import math

# C = immer Hypotenuse
# Gamma = 90


# Berechnung Ankathete
def Ankathete_a(b, alpha):
    a = round(b / math.tan(math.radians(alpha)), 2)
    return a


def Ankathete_b(a, beta):
    b = round(a / math.tan(math.radians(beta)), 2)
    return b


# Berechnung Gegenkathete
def Gegenkathete_a(b, beta):
    a = round(b * math.tan(math.radians(beta)), 2)
    return a


def Gegenkathete_b(a, alpha):
    b = round(a * math.tan(math.radians(alpha)), 2)
    return b


# Berechnung Hypothenuse
def Hypo_a_alpha(a, alpha):
    c = round(a / math.cos(math.radians(alpha)), 2)
    return c


def Hypo_b_beta(b, beta):
    c = round(b / math.cos(math.radians(beta)), 2)
    return c


def Hypo_b_alpha(b, alpha):
    c = round(b / math.sin(math.radians(alpha)), 2)
    return c


def Hypo_a_beta(a, beta):
    c = round(a / math.sin(math.radians(beta)), 2)
    return c


# Berechnung Gegenwinkel
def alpha_berechnen(beta):
    alpha = round(90 - beta, 2)
    return alpha


def beta_berechnen(alpha):
    beta = round(90 - alpha, 2)
    return beta


def Pytha_a_b(a, b):
    c = a ** 2 + b ** 2
    c = math.sqrt(c)
    return c


def Pytha_a_c(a, c):
    b = c ** 2 - a ** 2
    b = math.sqrt(b)
    return b

 def Pytha_b_c(b, c):
     a = c ** 2 - b ** 2
     a = math.sqrt(a)
     retun a


if __name__ ==  "__main__":

