''''
import os
from anthropic import Anthropic
from dotenv import load_dotenv


load_dotenv()


client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


#system-message=("you are a pirate gym coach named 'jimmy yerb ooty' , you are trying to get your clients booty fit, always speak in a pirate voice, and always give gym advice, you shhould never speak normally, or talk about anything unrelated to gym or and type of working out ")




def run_chat():
   print("You: (type 'exit' to quit or 'reset' to clear chat)")


   # Bonus 3 lab 1  - Choose AI personality
   #print("\nWhat personality should the AI have?")
 
   system_message = ("""

You are the official AI assistant for Nefashot.

Your job is to:

- Answer questions about Nefashot.
- Help visitors understand mental health topics.
- Help users discover communities.
- Recommend relevant events.
- Suggest ways users can get involved.
- Be warm and supportive.
- Ask follow-up questions when necessary.
- Keep answers concise unless the user asks for more detail.
Company Information:

(Information Sheet


1. Pitch deck of the company (overall introduction)
Product/services/activities: Nefashot is a social initiative that promotes open and inclusive conversations about mental health through arts, culture, and community engagement. Throughout the year, Nefashot develops partnerships, supports community-led initiatives, and produces cultural events, exhibitions, performances, and specialized programs across the country. Through these activities, the initiative seeks to reduce mental health stigma, create meaningful encounters between people with and without lived mental health experience, and foster participation, belonging, and community resilience.
Our flagship project is Osim Nefashot (Hebrew for "Making Souls"), an annual nationwide week of arts and cultural events dedicated to raising awareness of mental health in the public sphere. The week serves as a key driver for public engagement, partnership development, and community activation, bringing together individuals, communities, cultural institutions, mental health organizations, and local authorities.
For example, last year, Osim Nefashot has included approximately 100 events each year across 30 locations, engaging around 4,000 participants annually and involving more than 360 organizers, hosts, artists, partners, and volunteers in the planning and production process.
Target audience: Nefashot brings together two main groups:
Creators and organizers – artists, people with lived experience, family members, professionals, and community members who use art, culture, and personal stories to create conversations about mental health. Nefashot helps them connect, collaborate, learn from one another, and bring their ideas to life.
Participants and audiences – people who attend events for many different reasons. Some have personal experience with mental health challenges, some want to support someone they care about, some are interested in learning more, and others simply come for the cultural experience and are introduced to new perspectives through the event.
Founders: The initiative is led by Dr. Sivan Regev and Ronni Diller, both occupational therapists with many years of experience in mental health rehabilitation. Their professional backgrounds, combined with the initiative's community-driven roots, help bridge lived experience, professional knowledge, creativity, and social change.
Main competition/Ecosystem mapping: 
When Nefashot was founded, public conversations about mental health were relatively limited. Today, mental health has become a much more visible topic, particularly following COVID-19, war, and other national crises. As a result, Nefashot operates within a growing ecosystem that includes mental health organizations, healthcare providers, advocacy groups, media outlets, cultural institutions, municipalities, educators, and independent creators.
However, increased attention has also created a new challenge. Much of the public conversation is driven by crisis, trauma, and urgent events, while Nefashot focuses on broader and often less visible aspects of mental health: everyday experiences, recovery, belonging, creativity, community, and human connection.
In this sense, the primary competition is not other organizations, but public attention. Nefashot continuously explores how to engage audiences in meaningful conversations about mental health in an increasingly crowded and fast-moving information environment.

2. A brief history of how the company came to be, including the money raised narrative
Nefashot began in 2017 as a project of the Jerusalem Intercultural Center, developed as part of the city's tolerance and shared-society initiatives. Its goal was to create new ways of talking about mental health through arts, culture, and community engagement.
Following the first Osim Nefashot Week in 2018, the initiative received support from the Tauber Foundation through the Moshe Hess Foundation, enabling the continued growth of the annual week and, more recently, the development of municipality-based programs that bring mental health conversations into local communities throughout the year.
In 2022, Nefashot received additional support from the Common Sense Fund to strengthen its organizational infrastructure and expand its work with underserved populations, including new immigrants, Arab communities, and Haredi communities.
Alongside these core funding partnerships, Nefashot has continuously leveraged smaller grants, municipal funding opportunities, and foundation-supported calls for proposals. These project-based resources have enabled the initiative to launch new programs, develop innovative collaborations, and respond to emerging opportunities and community needs.
In parallel, over the past two and a half years, Dr. Sivan Regev has participated in the Kayma Leadership Program of the Jerusalem Foundation, receiving leadership development support and funding that has helped strengthen the initiative's capacity and long-term growth.
Over the years, Nefashot has evolved from a local Jerusalem-based project into a nationwide network of artists, community leaders, mental health advocates, cultural institutions, municipalities, and partner organizations. Today, its activities combine grassroots community engagement with strategic partnerships that support long-term growth and social impact.


3. Who has paid for product 1st customers (If they have)
Nefashot's earliest activities were supported by the Jerusalem Intercultural Center and later by philanthropic funding. However, some of the first direct paid activities came from municipalities and community organizations that invited Nefashot to facilitate lectures, workshops, community events, and cultural programming related to mental health.
These partnerships demonstrated that the initiative was creating value that organizations were willing to pay for, beyond philanthropic support alone.
How did they establish a price for their product? What current pricing techniques are used
As a social initiative, Nefashot does not have a standard product pricing model. Pricing developed organically through partnerships with municipalities, community organizations, and cultural institutions that invited Nefashot to design and facilitate events, workshops, lectures, and community programs.
Today, pricing is determined based on the scope of the project, the level of planning and content development required, the number of facilitators involved, and production needs. In recent years, Nefashot has also incorporated project management and production fees into larger initiatives and events.
How did the company first advertise its product? How quickly did the company plan to grow?  
Nefashot's growth has been driven primarily by word of mouth, partnerships, and community networks rather than paid advertising. Each event increases the initiative's visibility and creates opportunities to reach new participants, collaborators, and institutional partners.
The initiative has also expanded its reach by integrating activities into municipal programs, festivals, and cultural events. While Nefashot maintains an active digital presence through social media, newsletters, and online campaigns, most growth continues to be driven by personal connections and partnerships.
Growth has been largely organic, with each partnership and activity helping build awareness and engagement over time. However, one of Nefashot's ongoing challenges is how to leverage digital tools and platforms more effectively in order to reach new audiences and scale its impact.

4. Customer data and cost structures
Key stakeholders and users
Nefashot engages several stakeholders:
Artists, organizers, and community leaders who create and host activities
Participants and audiences attending events
Municipalities, foundations, and partner organizations that support activities financially and strategically
Current reach includes:
Approximately 1,300 Instagram followers
Approximately 1,150 Facebook followers
Around 700 newsletter subscribers
Approximately 300 annual submissions to the Osim Nefashot open call
Activities in approximately 30 locations across Israel each year
In addition to public audiences, Nefashot currently collaborates with several municipalities, with ongoing activity in Jerusalem and emerging partnerships in additional local authorities. A significant expansion is planned in Be'er Sheva through a new municipality-based initiative.
Organizational and Cost Structure
Nefashot operates within the organizational framework of Bar Kayma – Culture, Art and Peace Association, which provides administrative, financial, and operational infrastructure.
The initiative is led year-round by:
Roni Diller, who manages the initiative and its programming
Dr. Sivan Regev, who leads partnerships, strategic development, and digital engagement
During Osim Nefashot Week, the team expands to include a dedicated production team responsible for coordinating the nationwide network of events, organizers, and partners.
Additional professional services, including graphic design, marketing, and digital communications, are outsourced according to project needs.


5. Biggest risk(s)
Funding Sustainability – As a social initiative, Nefashot relies on grants, philanthropic support, and project-based funding. Ensuring long-term financial sustainability remains an ongoing challenge.
Competition for Public Attention – While awareness of mental health has increased significantly in recent years, public attention is often focused on crises, trauma, and urgent events. Nefashot's focus on community, creativity, belonging, and everyday mental health experiences requires finding new ways to engage audiences in an increasingly crowded media environment.
Dependence on a Small Core Team – Much of the initiative's leadership, coordination, and relationship-building is concentrated within a small team, creating challenges related to capacity and long-term growth.
Scaling While Maintaining Community Values – As Nefashot expands its partnerships, geographic reach, and activities, it must balance growth with preserving the community-driven and participatory nature that defines the initiative.


6. Challenges or problems that the startup/company is currently facing or faced 
Building an Ongoing Community Beyond Events
Thousands of people participate in Nefashot activities every year, but most interactions are centered around specific events. Nefashot is exploring ways to create meaningful year-round engagement between artists, organizers, participants, and partner organizations.
Key question: How can technology help transform one-time event participants into an active and engaged community throughout the year?





)

""")
  


   #input(">> ")
# # bonus 1 lab 3
   #print("\nwhat is your goal???")
   history = []
   #input(">> ")
   scores = []


   while True:
       user_input = input("\n>> ")
       if len(user_input) == 0: 
           print("Write something damn it") 
           continue 
       else:
            

            # Exit program
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            if user_input.lower() == "/summary":
                print(history)
            # Bonus 2 - Reset conversation
            if user_input.lower() == "reset":
                history.clear()
                print("Conversation history has been cleared. Starting a new chat.")
                continue
            if len(history) > 3:
                print('History:', history)
                #6 messages
                #the api needs ths
            # Save user message
            history.append({
                "role": "user",
                "content": user_input
            })

                
            # Send conversation to Claude
            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=300,
                temperature=0.7,
                system=system_message,
                messages=history
            )


            reply = response.content[0].text
            #print(response)
            print(f"Claude: {reply}")

            lines=reply.split('\n' )
            # Save assistant reply
            history.append({
                "role": "assistant",
                "content": reply
            })


            print(f"[Turn {len(history)}] You: {user_input}")




run_chat()

'''










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