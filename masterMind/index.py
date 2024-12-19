import random


def generate_combination(colors, length=4):
    return random.sample(colors, length)


def get_feedback(secret, guess):
    black_pegs = sum(s == g for s, g in zip(secret, guess))
    white_pegs = sum(min(secret.count(color), guess.count(color)) for color in set(guess)) - black_pegs
    return black_pegs, white_pegs


def mastermind_game():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Available colors
    secret_combination = generate_combination(colors)
    attempts = 3

    print("Bienvenue au jeu Mastermind!")
    print("Les couleurs disponibles sont: R (Rouge), G (Vert), B (Bleu), Y (Jaune), O (Orange), P (Violet)")
    print("Devinez la combinaison secrète de 4 couleurs. Vous avez 3 essais.")

    while attempts > 0:
        guess = input(f"Tentative {4 - attempts}: Entrez 4 couleurs séparées par un espace: ").upper().split()

        if len(guess) != 4 or any(color not in colors for color in guess):
            print("Entrée invalide. Veuillez entrer 4 couleurs valides séparées par un espace.")
            continue

        black_pegs, white_pegs = get_feedback(secret_combination, guess)

        if black_pegs == 4:
            print("Félicitations! Vous avez découvert la combinaison secrète.")
            break

        print(f"Pions noirs (bien placés): {black_pegs}, Pions blancs (mal placés): {white_pegs}")
        attempts -= 1

        if attempts == 0:
            print("Vous avez épuisé tous vos essais.")
            print(f"La combinaison secrète était: {' '.join(secret_combination)}")
            break


if __name__ == "__main__":
    mastermind_game()
