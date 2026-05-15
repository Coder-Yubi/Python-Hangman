import random
import math
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load("mixkit-light-it-up-boy-849.mp3")  # your music file
pygame.mixer.music.play(-1)  # -1 means loop forever

correct_sound = pygame.mixer.Sound("dragon-studio-correct-472358.mp3")
wrong_sound = pygame.mixer.Sound("mixkit-wrong-answer-fail-notification-946.wav")
win = pygame.mixer.Sound("mixkit-game-level-completed-2059.wav")
lost = pygame.mixer.Sound("mixkit-sad-game-over-trombone-471.wav")

word_list = ["computer", "apple", "banana", "teacher", "chair", "table", "mango", "programming", "python","guitar", "football", "elephant", "airplane", "bicycle", "camera", "diamond", "flower", "galaxy", "happiness", "island", "jungle", "kangaroo", "lemon", "mountain", "notebook", "ocean", "pencil", "queen", "rainbow", "sunflower", "turtle", "umbrella", "volcano", "watermelon", "xylophone", "yacht", "zebra", "programming", "galaxy", "classroom", "adventure", "butterfly", "chocolate", "dinosaur", "envelope", "fireworks", "giraffe", "helicopter", "infinity", "jazz", "koala", "lighthouse", "marathon", "nebula", "octopus", "paradise", "quarantine", "robotics", "symphony", "treasure", "universe", "vampire", "wizard", "xenophobia", "yogurt", "zodiac,", "challenge", "mystery", "puzzle", "strategy", "fun", "entertainment", "guessing", "word", "game", "player", "score", "win", "lose", "lives", "letters", "alphabet", "random", "selection"]

chosen_word = random.choice(word_list)

word_letters_list = list(chosen_word)

unique_letters_list = []
for char in word_letters_list:
    if char not in unique_letters_list:
        unique_letters_list.append(char)

duplicate = []
for char in unique_letters_list:
    if(chosen_word.count(char) > 1):
        duplicate.append(char)

already_guessed_len = math.ceil(len(chosen_word)/2)
already_guessed_len = min(already_guessed_len, len(unique_letters_list))
guessed_letters_list = random.sample(unique_letters_list, already_guessed_len)

def display_user_problem(word_letters_list, guessed_letters_list):
    display = []
    for char in word_letters_list:
        if char in guessed_letters_list and (char not in display or char in guessed_by_user):
            display.append(char)
        else:
            display.append("_")
    return " ".join(display)


lives = len(chosen_word) - already_guessed_len + 2
lives_gone = 0

print("""
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")

# print("🎮 Welcome to Hangman Game! 🎮")

print("""
╔════════════════════════════════════╗
║   🎮 WELCOME TO HANGMAN GAME 🎮    ║
║   Guess the word before you die!   ║
╚════════════════════════════════════╝
""")

guessed_by_user = []
print(display_user_problem(word_letters_list, guessed_letters_list))

while True :
    print(f"You have {lives} lives left :{lives * ' ❤️'}{lives_gone * ' 🩶'}")

    ch = input("Enter a letter : ")
    ch = ch.lower()

    if len(ch) != 1 or not ch.isalpha():
        print("⚠️ Enter a valid single letter!")
        continue

    elif ch in guessed_by_user :
        print("⚠️ You already guessed that letter!")
        continue

    else:
       
        if ch in chosen_word and (ch not in guessed_letters_list or ch in duplicate):
            print("✅ Correct guess!")
            correct_sound.play()   # 🔊 play correct sound
            guessed_by_user.append(ch)
            guessed_letters_list.append(ch)  
            print(display_user_problem(word_letters_list,guessed_letters_list))
        
        elif ch in guessed_letters_list:
            print("⚠️ You already guessed that letter!")
            continue
        
        else:
            print("❌ Wrong guess!")
            wrong_sound.play()   # 🔊 play wrong sound
            print(display_user_problem(word_letters_list,guessed_letters_list))
            lives = lives - 1
            lives_gone = lives_gone + 1
    
    current_progress = display_user_problem(word_letters_list,guessed_letters_list)
    
    if "_" not in current_progress:
        print("🎉 Congratulations! You won the game! 🎉")
        pygame.mixer.music.pause()
        win.play()   # 🔊 play win sound
        time.sleep(3)  # Pause for 2 seconds before showing the correct word
        break

    if lives == 0:
        print("💀 Game Over! You lost the game! 💀")
        print(f"The correct word was: {chosen_word}")
        pygame.mixer.music.pause()
        lost.play()   # 🔊 play lost sound
        time.sleep(5)  # Pause for 2 seconds before showing the correct word
        break



