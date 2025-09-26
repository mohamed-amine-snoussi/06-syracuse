#### Fonctions secondaires

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n"""
    if n <= 0:
        raise ValueError("n doit être un entier positif")
    l = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse"""
    # le temps de vol est le nombre d’itérations avant d’atteindre 1
    return len(l) - 1 if l else 0

def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse"""
    if not l:
        return 0
    depart = l[0]
    count = -1
    for val in l:  # on ne compte pas le dernier qui est 1
        if val > depart:
            count += 1
    return count

def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse"""
    return max(l) if l else 0


#### Fonction principale

def main():
    # Exemple avec n = 15
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print("Temps de vol :", temps_de_vol(lsyr))
    print("Temps de vol en altitude :", temps_de_vol_en_altitude(lsyr))
    print("Altitude maximale :", altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
