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
try:
    alpha = int(input_alpha)
except:
    alpha = 0
    alpha_lost = True

try:
    beta = int(input_beta)
except:
    beta = 0
    beta_lost = True


#umwandlung in floats(Seiten)
try:
    a = int(input_a)
except:
    a = 0
    a_lost = True

try:
    b = int(input_b)
except:
    b = 0
    b_lost = True

try:
    c = int(input_c)
except:
    c = 0
    c_lost = True


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
