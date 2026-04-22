import random
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(level_name, score, lives):
    clear_screen()
    hearts = "❤️ " * lives + "🖤 " * (3 - lives)
    print("==================================================")
    print("          🔤  WORD SCRAMBLE CHALLENGE  🔤         ")
    print("==================================================")
    print(f"| Level: {level_name:<14} | Score: {score:<12} |")
    print(f"| Lives: {hearts:<30}|")
    print("==================================================")

def scramble(word):
    letters = list(word)
    shuffled = letters[:]
    while shuffled == letters and len(word) > 2:
        random.shuffle(shuffled)
    return ''.join(shuffled)

def display_scrambled(word):
    print("\n  Scrambled: ", end="")
    for ch in word:
        print(f"[ {ch} ]", end=" ")
    print()

def main():
    # Configuration: (level_label, points_per_word, word_list_with_hints)
    levels = [
        {
            "name": "1-WARM UP",
            "points": 100,
            "words": [
                ("CAT",      "A furry pet that meows"),
                ("DOG",      "Man's best friend"),
                ("SUN",      "Shines in the sky"),
                ("MAP",      "Helps you find your way"),
            ]
        },
        {
            "name": "2-GETTING WARMER",
            "points": 200,
            "words": [
                ("PIANO",    "A musical instrument with keys"),
                ("STORM",    "Loud weather with lightning"),
                ("GRAPE",    "A small purple fruit"),
                ("FLAME",    "The glow of a fire"),
                ("BLANK",    "Empty, nothing written"),
            ]
        },
        {
            "name": "3-HEATING UP",
            "points": 350,
            "words": [
                ("BRIDGE",   "Crosses over water"),
                ("PLANET",   "Earth is one of these"),
                ("CANDLE",   "Wax with a flame on top"),
                ("FROZEN",   "Extremely cold, like ice"),
                ("JIGSAW",   "A puzzle you piece together"),
            ]
        },
        {
            "name": "4-ON FIRE",
            "points": 500,
            "words": [
                ("BLANKET",  "Keeps you warm in bed"),
                ("DOLPHIN",  "A smart ocean mammal"),
                ("NETWORK",  "Connected computers or people"),
                ("PUMPKIN",  "Carved for Halloween"),
                ("RAINBOW",  "Appears after rain"),
                ("TRUMPET",  "A brass wind instrument"),
            ]
        },
        {
            "name": "5-LEGEND",
            "points": 750,
            "words": [
                ("SOFTWARE",  "Programs running on a computer"),
                ("TWILIGHT",  "The sky just after sunset"),
                ("UNIVERSE",  "Everything that exists"),
                ("ABSTRACT",  "Hard to grasp, conceptual"),
                ("MONGOOSE",  "Animal that hunts snakes"),
                ("PLATINUM",  "A rare, silvery-white metal"),
            ]
        },
    ]

    clear_screen()
    print("==================================================")
    print("          🔤  WORD SCRAMBLE CHALLENGE  🔤         ")
    print("==================================================")
    print("\n  Unscramble the word before you run out of lives!")
    print("  • Use hints for a clue (costs 50% of points)")
    print("  • Skip a word to move on (costs 1 life)")
    print("  • 3 wrong guesses on a word costs 1 life")
    print("  • Chain correct answers for streak bonuses!\n")
    input("  Press [Enter] to begin your challenge...")

    while True:
        score = 0
        lives = 3
        streak = 0

        for level in levels:
            if lives <= 0:
                break

            print_header(level["name"], score, lives)
            print(f"\n  🚀 Starting {level['name']}!")
            print(f"  Each correct word earns {level['points']} points.")
            time.sleep(1.8)

            word_list = random.sample(level["words"], len(level["words"]))

            for idx, (word, hint) in enumerate(word_list):
                if lives <= 0:
                    break

                scrambled = scramble(word)
                wrong_attempts = 0
                hint_used = False
                won_word = False

                while True:
                    print_header(level["name"], score, lives)
                    print(f"\n  Word {idx + 1} of {len(word_list)}  |  "
                          f"Streak: {'🔥 x' + str(streak) if streak >= 2 else str(streak)}")

                    display_scrambled(scrambled)

                    if hint_used:
                        print(f"\n  💡 Hint: {hint}")
                    else:
                        print(f"\n  💡 Hint: [hidden — type 'hint' to reveal, costs 50% pts]")

                    print(f"\n  ⚠️  Wrong attempts this word: {wrong_attempts}/3")
                    print()

                    try:
                        guess = input("  ➤ Your answer (or 'hint' / 'skip'): ").strip().upper()
                    except (EOFError, KeyboardInterrupt):
                        print("\n\n  Game terminated. Thanks for playing! 👋")
                        return

                    if guess == "HINT":
                        if not hint_used:
                            hint_used = True
                            print(f"\n  💡 Hint revealed: {hint}")
                        else:
                            print("  (Hint already shown!)")
                        time.sleep(1.2)
                        continue

                    if guess == "SKIP":
                        lives -= 1
                        streak = 0
                        print(f"\n  ⏭  Skipped! The word was: {word}  (lost 1 life)")
                        time.sleep(2)
                        break

                    if guess == word:
                        pts = level["points"] if not hint_used else level["points"] // 2
                        streak += 1
                        # Streak bonus
                        streak_bonus = 0
                        if streak >= 3:
                            streak_bonus = (streak - 2) * 50
                            pts += streak_bonus

                        score += pts
                        won_word = True

                        msgs = ["✅ CORRECT!", "🎉 NAILED IT!", "⚡ PERFECT!", "🔥 BLAZING!"]
                        msg = msgs[min(streak - 1, len(msgs) - 1)]
                        print(f"\n  {msg}  +{pts} points!", end="")
                        if streak_bonus:
                            print(f"  (includes 🔥 streak bonus +{streak_bonus}!)", end="")
                        print()
                        time.sleep(1.5)
                        break

                    else:
                        wrong_attempts += 1
                        streak = 0
                        if wrong_attempts >= 3:
                            lives -= 1
                            print(f"\n  ❌ Too many wrong guesses! The word was: {word}  (lost 1 life)")
                            time.sleep(2)
                            break
                        else:
                            print(f"\n  ❌ Wrong! Try again. ({3 - wrong_attempts} attempt(s) left this word)")
                            time.sleep(1.2)

            # Level cleared?
            if lives > 0 and (idx + 1) == len(word_list):
                print_header(level["name"], score, lives)
                print(f"\n  🏅 Level {level['name']} complete! Nice work!")
                time.sleep(2)

        # End of all levels
        if lives <= 0:
            print_header("GAME OVER", score, 0)
            print("\n  💀 GAME OVER — You ran out of lives!")
            print(f"\n  🏆 Final Score: {score}")
        else:
            clear_screen()
            print("==================================================")
            print("          🔤  WORD SCRAMBLE CHALLENGE  🔤         ")
            print("==================================================")
            print("\n  🎉 CONGRATULATIONS! You cleared ALL 5 LEVELS! 🎉")
            print(f"\n  🏆 Final Score: {score}")
            print("\n  You are a true Word Wizard! 🧙")

        print()
        try:
            retry = input("  Play again? (y/n): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            retry = 'n'

        if retry != 'y':
            print("\n  Thanks for playing! Goodbye. 👋\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Game terminated. Thanks for playing! 👋\n")
