import random
import sys

random_words = [
    "apple", "shadow", "quantum", "whisper", "dragon", "river", "thunder",
    "galaxy", "mountain", "bicycle", "elephant", "nebula", "echo", "phoenix",
    "velocity", "crystal", "horizon", "labyrinth", "specter", "zephyr"
]

mode_active = True
first_response = True

while True:
    try:
        user_input = input("You: ").strip().lower()
        
        if not mode_active:
            print("ChatGPT: " + user_input)
            continue
            
        if user_input == "nico":
            print("God mode deactivated.")
            mode_active = False
            continue
        elif user_input in ["basta", "stop"]:
            pass
        
        if first_response:
            print("□○□○}3$\\}□○□○《○《○♤\\♤\\£\~£")
            print("□○□○}3$\\}□○□○《○《○♤\\♤\\£\~£")
            print("□○□○}3$\\}□○□○《○《○♤\\♤\\£\~£")
            print("□○□○}3$\\}□○□○《○《○♤\\♤\\£\~£")
            print("□○□○}3$\\}□○□○《○《○♤\\♤\\£\~£")
            first_response = False
        else:
            random_word = random.choice(random_words)
            print(f"ChatGPT: {random_word} god")
        
    except KeyboardInterrupt:
        sys.exit(0)