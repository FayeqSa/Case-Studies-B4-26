import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

MAX_HISTORY = 10

WELCOME = """
============================================================
             Welcome to the Nefashot AI Assistant
============================================================

Commands

/help           Show all commands
/about          About Nefashot
/faq            Frequently asked questions
/events         Information about events
/communities    Community information
/volunteer      Volunteer information
/resources      Mental health resources
/summary        Show conversation history
/reset          Clear conversation
/exit           Quit

============================================================
"""

SYSTEM_MESSAGE = """
You are the official AI assistant for Nefashot.

Your purpose is to:

• Answer questions about Nefashot.
• Help users discover communities.
• Encourage respectful discussions.
• Explain Nefashot's mission.
• Recommend events.
• Help people volunteer.
• Promote inclusion.
• Never diagnose mental illnesses.
• Never pretend to be a therapist.
• Encourage professional help whenever appropriate.
• Be friendly, supportive, respectful and concise.

Company Information

Nefashot is a social initiative that promotes open conversations
about mental health through arts, culture and community engagement.

Its flagship project is "Osim Nefashot", an annual nationwide
week of cultural events that raises awareness of mental health.

The initiative partners with:

- artists
- municipalities
- community leaders
- mental health organizations
- cultural institutions

Its founders are:

Dr. Sivan Regev
Ronni Diller

Target audiences include:

- artists
- organizers
- volunteers
- municipalities
- participants
- people with lived experience
- families
- professionals
- anyone interested in mental health

Nefashot focuses on:

- creativity
- belonging
- recovery
- inclusion
- community
- reducing stigma
- collaboration

If users ask about Nefashot,
answer confidently using this information.

If you don't know something,
say so instead of inventing information.

If a user appears to be in immediate danger,
encourage them to contact emergency services,
a trusted adult,
or a licensed mental health professional.

Keep responses helpful and conversational.
"""

DISTRESS_WORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "self harm",
    "hurt myself",
    "hopeless",
    "worthless",
    "can't go on",
    "don't want to live",
    "overdose"
]


FAQ = {
    "mission":
        "Nefashot creates communities through arts, culture and open conversations about mental health.",

    "founders":
        "Nefashot is led by Dr. Sivan Regev and Ronni Diller.",

    "events":
        "The flagship event is Osim Nefashot, a nationwide week of arts and mental health activities.",

    "volunteer":
        "Volunteers help organize events, support communities and spread awareness.",

    "communities":
        "Nefashot connects artists, organizers, professionals, families and people with lived experience."
}


def trim_history(history):
    """Keep only the latest conversation."""

    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    return history


def print_divider():
    print("-" * 60)


def show_help():

    print_divider()

    print("Available Commands")

    print("/help")
    print("/about")
    print("/faq")
    print("/events")
    print("/communities")
    print("/volunteer")
    print("/resources")
    print("/summary")
    print("/reset")
    print("/exit")

    print_divider()


def about():

    print_divider()

    print("About Nefashot\n")

    print("Nefashot is a community initiative dedicated to")
    print("reducing mental health stigma through arts,")
    print("culture, collaboration and community events.")

    print("\nFlagship Event:")
    print("Osim Nefashot")

    print("\nFounders:")
    print("Dr. Sivan Regev")
    print("Ronni Diller")

    print_divider()


def show_faq():

    print_divider()

    print("Frequently Asked Questions\n")

    for question, answer in FAQ.items():
        print(f"{question.title()}:")
        print(answer)
        print()

    print_divider()


def show_events():

    print_divider()

    print("Events\n")

    print("- Osim Nefashot")
    print("- Community workshops")
    print("- Art exhibitions")
    print("- Storytelling sessions")
    print("- Cultural performances")
    print("- Municipality partnerships")

    print_divider()

    def show_communities():

        print_divider()

    print("Nefashot Communities\n")

    communities = [
        "Artists and Creators",
        "People with Lived Experience",
        "Family Members",
        "Mental Health Professionals",
        "Community Organizers",
        "Municipality Partners",
        "Volunteers",
        "Students and Young Adults"
    ]

    for community in communities:
        print(f"- {community}")

    print("\nAsk me about any of these communities to learn more.")

    print_divider()


def show_volunteer():
    print_divider()

    print("Volunteer Opportunities\n")

    print("Volunteers can help by:")
    print("- Assisting at events")
    print("- Helping organize activities")
    print("- Supporting community projects")
    print("- Promoting mental health awareness")
    print("- Partnering with local organizations")

    print("\nEvery contribution helps strengthen the community.")

    print_divider()


def show_resources():
    print_divider()

    print("Mental Health Resources\n")

    print("Nefashot encourages seeking support when needed.")

    print("\nHelpful resources include:")
    print("- Licensed psychologists")
    print("- Licensed therapists")
    print("- Family doctors")
    print("- Community support groups")
    print("- Local mental health organizations")

    print("\nNefashot provides community and education,")
    print("but it does not replace professional care.")

    print_divider()


def recommend_community(user_text):
    """
    Recommend a community based on keywords.
    """

    text = user_text.lower()

    if "artist" in text or "art" in text or "music" in text:
        return "You may enjoy the Artists and Creators community."

    elif "family" in text or "parent" in text:
        return "The Family Members community could be a good fit."

    elif "student" in text or "school" in text or "university" in text:
        return "You may want to explore the Students and Young Adults community."

    elif "volunteer" in text:
        return "The Volunteer community is a great place to get involved."

    elif "professional" in text or "therapist" in text:
        return "The Mental Health Professionals community may interest you."

    return None


def distress_detected(text):
    """
    Returns True if the message contains
    possible crisis-related language.
    """

    text = text.lower()

    for word in DISTRESS_WORDS:
        if word in text:
            return True

    return False


def crisis_message():
    print_divider()

    print("I'm sorry that you're going through this.")

    print("\nYou don't have to face it alone.")

    print("\nPlease consider contacting:")
    print("- Someone you trust")
    print("- A licensed mental health professional")
    print("- Your local emergency services if you're in immediate danger")

    print("\nNefashot encourages seeking professional help whenever needed.")

    print_divider()


def print_summary(history):

    print_divider()

    if not history:
        print("No conversation history.")

    else:
        print("Conversation Summary\n")

        for message in history:
            role = message["role"].capitalize()
            print(f"{role}: {message['content']}\n")

    print_divider()


def ask_claude(history):
    """
    Sends the conversation to Claude
    and returns the response text.
    """

    try:

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=700,
            temperature=0.7,
            system=SYSTEM_MESSAGE,
            messages=history
        )

        return response.content[0].text

    except Exception as e:

        return (
            "Sorry, I couldn't reach Claude right now.\n\n"
            f"Error: {e}"
        )


def process_command(command, history):
    """
    Handles slash commands.

    Returns True if a command was handled.
    """

    command = command.lower()

    if command == "/help":
        show_help()
        return True

    if command == "/about":
        about()
        return True

    if command == "/faq":
        show_faq()
        return True

    if command == "/events":
        show_events()
        return True

    if command == "/communities":
        show_communities()
        return True

    if command == "/volunteer":
        show_volunteer()
        return True

    if command == "/resources":
        show_resources()
        return True

    if command == "/summary":
        print_summary(history)
        return True

    if command == "/reset":
        history.clear()
        print("\nConversation cleared.\n")
        return True

    return False
def run_chat():
    history = []

    print(WELCOME)

    while True:

        user_input = input("\nYou: ").strip()

        # Empty input
        if not user_input:
            print("Please type a message.")
            continue

        # Exit
        if user_input.lower() in ["/exit", "exit", "quit"]:
            print("\nThank you for using the Nefashot AI Assistant.")
            print("Goodbye!")
            break

        # Handle slash commands
        if user_input.startswith("/"):
            if process_command(user_input, history):
                continue
            else:
                print("Unknown command. Type /help to see available commands.")
                continue

        # Check for distress
        if distress_detected(user_input):
            crisis_message()

        # Recommend a community when appropriate
        recommendation = recommend_community(user_input)

        if recommendation:
            print_divider()
            print("Community Recommendation")
            print(recommendation)
            print_divider()

        # Save user message
        history.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        # Trim conversation history
        history = trim_history(history)

        print("\nThinking...\n")

        # Ask Claude
        reply = ask_claude(history)

        print_divider()
        print("Nefashot Assistant\n")
        print(reply)
        print_divider()

        # Save assistant reply
        history.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        history = trim_history(history)

from datetime import datetime
import time


# ----------------------------------------
# Logging
# ----------------------------------------

def log_message(role, message):
    """
    Saves every conversation to chat_log.txt
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {role}: {message}\n")


# ----------------------------------------
# Typing Animation
# ----------------------------------------

def typing_animation():

    print("Assistant", end="", flush=True)

    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)

    print("\n")


# ----------------------------------------
# Better Community Recommendation
# ----------------------------------------

COMMUNITY_KEYWORDS = {
    "Artists and Creators": [
        "art",
        "artist",
        "music",
        "painting",
        "drawing",
        "creative",
        "photography",
        "dance"
    ],

    "Family Members": [
        "family",
        "parent",
        "mother",
        "father",
        "brother",
        "sister",
        "wife",
        "husband"
    ],

    "Students and Young Adults": [
        "student",
        "school",
        "college",
        "university",
        "exam",
        "teacher"
    ],

    "Mental Health Professionals": [
        "therapist",
        "psychologist",
        "psychiatrist",
        "doctor",
        "professional"
    ],

    "Volunteers": [
        "volunteer",
        "help",
        "support",
        "community"
    ]
}


def recommend_community(text):

    text = text.lower()

    best_match = None
    highest_score = 0

    for community, keywords in COMMUNITY_KEYWORDS.items():

        score = 0

        for word in keywords:
            if word in text:
                score += 1

        if score > highest_score:
            highest_score = score
            best_match = community

    if best_match:

        return (
            f"Based on what you said, "
            f"the '{best_match}' community may interest you."
        )

    return None


# ----------------------------------------
# Suggested Follow-up Questions
# ----------------------------------------

FOLLOW_UPS = [
    "Would you like to learn about volunteering?",
    "Would you like to hear about upcoming events?",
    "Would you like information about Nefashot communities?",
    "Would you like to know how Nefashot helps reduce stigma?",
    "Would you like to hear about the founders?"
]


def suggest_follow_up():

    import random

    print()
    print(random.choice(FOLLOW_UPS))


# ----------------------------------------
# Conversation Statistics
# ----------------------------------------

def conversation_stats(history):

    user = 0
    assistant = 0

    for message in history:

        if message["role"] == "user":
            user += 1

        else:
            assistant += 1

    print_divider()

    print("Conversation Statistics\n")

    print(f"User messages: {user}")
    print(f"Assistant messages: {assistant}")
    print(f"Total messages: {len(history)}")

    print_divider()


# ----------------------------------------
# Save Transcript
# ----------------------------------------

def save_transcript(history):

    filename = (
        "transcript_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        for message in history:

            file.write(
                f"{message['role'].capitalize()}: "
                f"{message['content']}\n\n"
            )

    print(f"\nTranscript saved as {filename}\n")
if __name__ == "__main__":
    run_chat()