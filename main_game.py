from game_utils import slow_print, choix_ordinateur, definir_gagnant, afficher_resultats, SYMBOLS

def jouer():
    scores = {
        "joueur": 0,
        "ordinateur": 0,
        "egalite": 0
    }

    slow_print("=== Bienvenue dans le duel Pierre / Feuille / Ciseaux ===", 0.03)
    print("Entre 'pierre', 'feuille', 'ciseaux' ou 'q' pour quitter le jeu.\n")

    while True:
        choix_joueur = input("Ton choix : ").strip().lower()

        if choix_joueur in ["q", "quit", "quitter"]:
            break

        if choix_joueur not in ["pierre", "feuille", "ciseaux"]:
            print("⛔ Choix invalide, essaie encore.")
            continue

        choix_ordi = choix_ordinateur()

        print(f"Tu joues : {SYMBOLS[choix_joueur]}  ({choix_joueur})")
        print(f"L'ordi joue : {SYMBOLS[choix_ordi]}  ({choix_ordi})")

        gagnant = definir_gagnant(choix_joueur, choix_ordi)

        if gagnant == "joueur":
            print("✅ Tu remportes cette manche !")
            scores["joueur"] += 1
        elif gagnant == "ordinateur":
            print("💻 L'ordinateur gagne ce tour.")
            scores["ordinateur"] += 1
        else:
            print("😐 Égalité parfaite.")
            scores["egalite"] += 1

        afficher_resultats(scores)
        print("-" * 45)

    print("\nFin du duel ⚔️")
    afficher_resultats(scores)

if __name__ == "__main__":
    jouer()
