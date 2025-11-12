import random
import time

SYMBOLS = {
    "pierre": "🪨",
    "feuille": "📜",
    "ciseaux": "✂️",
}

REGLES = [
    ("pierre", "ciseaux"),
    ("ciseaux", "feuille"),
    ("feuille", "pierre"),
]

def slow_print(texte, delai=0.02):
    """Affiche un texte lettre par lettre."""
    for caractere in texte:
        print(caractere, end="", flush=True)
        time.sleep(delai)
    print()

def choix_ordinateur():
    """Retourne un choix aléatoire pour l'ordinateur."""
    return random.choice(["pierre", "feuille", "ciseaux"])

def definir_gagnant(joueur, ordinateur):
    """Compare les deux choix et retourne le gagnant."""
    if joueur == ordinateur:
        return "egalite"
    for gagnant, perdant in REGLES:
        if joueur == gagnant and ordinateur == perdant:
            return "joueur"
        elif ordinateur == gagnant and joueur == perdant:
            return "ordinateur"
    return "egalite"

def afficher_resultats(score):
    """Affiche les scores actuels."""
    print(f"📊 Score → Joueur: {score['joueur']} | Ordi: {score['ordinateur']} | Égalités: {score['egalite']}")
