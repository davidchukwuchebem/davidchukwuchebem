import random
from datetime import datetime

README_PATH = "README.md"

# 🔥 Your motivational quotes list
quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Don't watch the clock; do what it does. Keep going.",
    "Great things never come from comfort zones.",
    "Believe you can and you're halfway there.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Do something today that your future self will thank you for.",
    "Your limitation—it’s only your imagination.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

# 🎯 Pick a random quote
quote = random.choice(quotes)

# ⏱ Timestamp (optional)
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# 📝 Update the README file
with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.readlines()

# Look for our custom marker tags to replace text in between
start_tag = "<!--QUOTE-START-->"
end_tag = "<!--QUOTE-END-->"

new_content = []
inside_tags = False
for line in content:
    if start_tag in line:
        new_content.append(f"{start_tag}\n")
        new_content.append(f"**💡 Motivation of the Day:** _\"{quote}\"_\n\n")
        inside_tags = True
    elif end_tag in line:
        new_content.append(f"{end_tag}\n")
        inside_tags = False
    elif not inside_tags:
        new_content.append(line)

# Save it back
with open(README_PATH, "w", encoding="utf-8") as file:
    file.writelines(new_content)
