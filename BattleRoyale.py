import random
import tkinter as tk
from tkinter import ttk

# List of various weapons and methods for more realistic battle outcomes
weapons = [
    "with a sharp sword", "using a bow and arrow", "shot with a sniper rifle",
    "with a poison dart", "with a deadly virus", "using hand-to-hand combat",
    "with a grenade", "with a spear", "using a trap", "with a sledgehammer",
    "with a pistol", "using a booby trap", "with a crossbow", "with a machete",
    "shot point-blank in the head", "sliced up with a katana", "with a flamethrower",
    "using an axe", "with a chainsaw", "with a Molotov cocktail", "using a claymore mine",
    "with a spiked club", "with a throwing knife", "shot with a shotgun",
    "using a rocket launcher", "with a steel garrote", "by pushing them off a cliff",
    "with a baseball bat with nails", "using a grenade launcher", "with a combat knife",
    "with a garrote wire", "bludgeoned with a crowbar", "using a morning star",
    "with brass knuckles", "with a taser and then a knife", "using a combat staff",
    "with a longbow", "with a hunting rifle", "using a garrote wire",
    "with a steel-tipped arrow", "with a poison gas", "using a cyber attack drone",
    "with a plasma rifle", "by setting them on fire", "using a bear trap"
]


# Generate a random battle outcome phrase
def battle_outcome(fighter1, fighter2):
    weapon = random.choice(weapons)
    return f"{fighter1} kills {fighter2} {weapon}."


def battle_royale(phrases):
    remaining_fighters = phrases[:]
    results = []

    while len(remaining_fighters) > 1:
        fighter1, fighter2 = random.sample(remaining_fighters, 2)
        outcome = battle_outcome(fighter1, fighter2)

        results.append(outcome)
        if fighter1 in remaining_fighters:
            remaining_fighters.remove(fighter2)
        else:
            remaining_fighters.remove(fighter1)

    winner = remaining_fighters[0]
    results.append(f"\n{winner.upper()} is the winner!")

    return "\n".join(results)


def start_battle():
    input_text = text_field.get("1.0", tk.END).strip()
    phrases = [phrase.strip() for phrase in input_text.split("\n") if phrase.strip()]

    if len(phrases) < 2:
        result_text.set("At least two phrases/items are required to start the battle.")
        return

    results = battle_royale(phrases)
    result_text.set(results)


# Create main application window
root = tk.Tk()
root.title("Battle Royale")

# Set dark mode theme
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Helvetica", 12))
style.configure("TButton", background="#4D4D4D", foreground="#FFFFFF", font=("Helvetica", 12), padding=6, relief="flat")
style.configure("TText", background="#2E2E2E", foreground="#FFFFFF", font=("Helvetica", 12), borderwidth=0)
style.configure("TFrame", background="#2E2E2E")
style.map("TButton", background=[("active", "#606060")])

# Create a frame to hold the widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

# Create a label
label = ttk.Label(frame, text="Enter phrases/items (one per line):")
label.pack(pady=10)

# Create a text field
text_field = tk.Text(frame, height=10, width=50, bg="#2E2E2E", fg="#FFFFFF", font=("Helvetica", 12),
                     insertbackground="white")
text_field.pack(pady=10)

# Create a button to start the battle
start_button = ttk.Button(frame, text="Start Battle", command=start_battle)
start_button.pack(pady=10)

# Create a text variable to hold the result
result_text = tk.StringVar()

# Create a label to display the result
result_label = ttk.Label(frame, textvariable=result_text, justify="left", wraplength=500)
result_label.pack(pady=10)

# Run the application
root.mainloop()

