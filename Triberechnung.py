import Trigonometriemodule as Tm


# Vars
complete = False
alpha_lost = False
beta_lost = False
a_lost = False
b_lost = False
c_lost = False

input_alpha = input("Wie groß ist der Winkel alpha?\n ")
input_beta = input("Wie groß ist der Winkel beta?\n ")

# input Seitenlängen
input_a = input("Wie groß ist Seite a?\n")
input_b = input("Wie groß ist Seite b?\n")
input_c = input("Wie groß ist Seite c?\n")


#umwandlung in floats(Winkel)
if input_alpha != "?":
    alpha = float(input_alpha)
else:
    alpha_lost = True
    alpha = 0.0


if input_beta != "?":
    beta = float(input_beta)
else:
    beta_lost = True
    beta = 0.0


#umwandlung in floats(Seiten)
if input_a != "?":
    a = float(input_a)
else:
    a_lost = True
    a = 0.0

if input_b != "?":
    b = float(input_b)
else:
    b_lost = True
    b = 0.0

if input_c != "?":
    c = float(input_c)
else:
    c_lost = True
    c = 0.0


# Sicherheitsabfragen(beta)

    # unbekannte Hypotenuse berechenen
if a_lost == False and alpha_lost == False and c_lost == True:
    c = Tm.Hypo_a_alpha(a, alpha)
    c_lost = False

if b_lost == False and beta_lost == False and c_lost == True:
    c = Tm.Hypo_b_beta(b, beta)
    c_lost = False

if a_lost == False and beta_lost == False and c_lost == True:
    c = Tm.Hypo_a_beta(a, beta)
    c_lost = False

if b_lost == False and alpha_lost == False and c_lost == True:
    c = Tm.Hypo_b_alpha(b, alpha)
    c_lost = False

# unbekannte Ankatheten berechnen
if a_lost == True and alpha_lost == False:
    a = Tm.Ankathete_a(b, alpha)
    a_lost = False

if b_lost == True and beta_lost == False:
    b = Tm.Ankathete_b(a, beta)
    b_lost = False


# unbekannte Gegenkathete berechenen
if a_lost == True and b_lost == False:
    a = Tm.Gegenkathete_a(b, beta)
    a_lost = False

if b_lost == True and a_lost == False:
    b = Tm.Gegenkathete_b(a, alpha)
    b_lost = False

# unbekannte Winkel berechnen
if alpha_lost == True:
    alpha = Tm.alpha_berechnen(beta)
    alpha_lost = False

if beta_lost == True:
    beta = Tm.beta_berechnen(alpha)
    beta_lost = False


# ergebnischeck
if a_lost == False and b_lost == False and c_lost == False and alpha_lost == False and beta_lost == False:
    complete = True
    print(complete)

    # ergebnisausgabe für den User
    print("----- Das Ergebnis -----\n")
    print("Die Seite a ist " + str(a) + " cm lang.\n")
    print("Die Seite b ist " + str(b) + " cm lang.\n")
    print("Die Seite c ist " + str(c) + " cm lang.\n")
    print("Der Winkel alpha ist " + str(alpha) + "° groß.\n")
    print("Der Winkel beta ist " + str(beta) + "° groß.\n")
    print("Der Winkel Gamma ist 90° groß.\n")
else:
    print("Etwas lief schief bitte probier es nochmal!!")
    print(complete)

# beendet das Script nicht sofort
input("Press Enter to Leave!")
