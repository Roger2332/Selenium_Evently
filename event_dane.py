import json
import time
from faker import Faker
import random
from datetime import datetime, timedelta

start_time = time.time()
fake = Faker()

ile_eventow = 10


# Generate a list of 100 fake cities
start_time_places = time.time()
places = [fake.city() for _ in range(ile_eventow * 10)]
end_time_places = time.time()
execution_time_places = end_time_places - start_time_places
print(f"Places wygenerowaly sie w: {execution_time_places}")


# List of event types and topics
event_types = [
    "Conference", "Webinar", "Exhibition", "Seminar", "Workshop", "Forum", "Festival",
    "Round Table", "Expo", "Sport Event", "Concert", "Trade Show", "Summit",
    "Networking Event", "Gala", "Fundraiser", "Lecture", "Panel Discussion",
    "Symposium", "Product Launch", "Awards Ceremony", "Competition", "Meetup",
    "Hackathon", "Art Event", "Film Screening", "Charity Event", "Book Launch",
    "Cooking Class", "Theater Performance", "Dance Show", "Fashion Show",
    "Science Fair", "Tech Demo", "Product Fair", "Community Gathering", "Health Workshop",
    "Startup Pitch", "Yoga Session", "Meditation Retreat", "Photography Exhibit",
    "Cultural Festival", "Pop-up Market", "Culinary Festival", "Career Fair",
    "Job Fair", "Live Podcast", "TEDx Talk", "Music Festival", "Game Jam",
    "Design Sprint", "Innovation Summit", "Climate Summit", "Art Installation",
    "Public Debate", "Social Media Workshop", "Travel Expo", "Real Estate Expo",
    "Investment Forum", "Philosophy Lecture", "Political Debate", "Economic Forum",
    "Mindfulness Workshop", "Leadership Summit", "Employee Training",
    "Customer Appreciation Event", "User Conference", "Virtual Reality Expo",
    "AI Conference", "Blockchain Summit", "Cybersecurity Forum",
    "Environmental Conference", "Space Exploration Forum", "Science and Tech Expo",
    "Artificial Intelligence Workshop", "Digital Transformation Summit"
]

topics = [
    "Technology", "Health", "Education", "Business", "Environment", "Science", "Art",
    "Music", "Literature", "Culture", "Sports", "Innovation", "Leadership",
    "Entrepreneurship", "Marketing", "Finance", "Philosophy", "Politics",
    "Economics", "Mindfulness", "Artificial Intelligence", "Blockchain",
    "Cybersecurity", "Space Exploration", "Digital Transformation"
]

descriptions = {
    "Conference": "The {event_type} on {topic} in {place} brings together experts and enthusiasts to discuss the latest trends and innovations in {topic}. Participants will have the opportunity to attend insightful sessions, network with professionals, and engage in stimulating conversations.",
    "Webinar": "Join us for a {event_type} on {topic}, live from {place}. This online event will cover key topics in {topic}, featuring expert speakers and interactive Q&A sessions. Don't miss this opportunity to enhance your knowledge and connect with peers from around the world.",
    "Exhibition": "The {event_type} on {topic} in {place} showcases the latest advancements and trends in {topic}. Attendees will explore a wide range of exhibits and interact with industry leaders.",
    "Seminar": "Attend our {event_type} on {topic} in {place}, where subject matter experts will share their insights and knowledge on {topic}. This event is designed for professionals looking to deepen their understanding of {topic}.",
    "Workshop": "Participate in a hands-on {event_type} on {topic} in {place}. This interactive session will provide practical skills and techniques related to {topic}, ideal for both beginners and seasoned professionals.",
    "Forum": "The {event_type} on {topic} in {place} offers a platform for open dialogue and discussion on pressing issues in {topic}. Join industry leaders and peers in exchanging ideas and finding solutions.",
    "Festival": "The {event_type} on {topic} in {place} is a celebration of culture, creativity, and community. Enjoy a variety of performances, workshops, and activities that highlight the best of {topic}.",
    "Round Table": "Join the {event_type} on {topic} in {place} for an in-depth discussion with experts and thought leaders. This collaborative environment encourages dialogue and the exchange of ideas on {topic}.",
    "Expo": "The {event_type} on {topic} in {place} brings together exhibitors from around the world to showcase the latest products, services, and innovations in {topic}. Discover new trends and network with industry professionals.",
    "Sport Event": "The {event_type} on {topic} in {place} is set to bring together athletes and sports enthusiasts for an exciting day of competition and camaraderie. Cheer on your favorite teams and enjoy the spirit of sportsmanship.",
    "Concert": "Experience the magic of live music at the {event_type} on {topic} in {place}. Join us for an unforgettable night of performances by top artists in the genre of {topic}.",
    "Trade Show": "The {event_type} on {topic} in {place} is the premier event for professionals in the {topic} industry. Explore the latest products, meet with suppliers, and attend informative sessions on industry trends.",
    "Summit": "The {event_type} on {topic} in {place} gathers leaders and influencers to discuss the future of {topic}. Engage in high-level discussions, network with peers, and gain valuable insights into {topic}.",
    "Networking Event": "Expand your professional network at the {event_type} on {topic} in {place}. This event provides an opportunity to meet and connect with like-minded individuals in the {topic} industry.",
    "Gala": "Join us for a glamorous {event_type} on {topic} in {place}. Enjoy an evening of fine dining, entertainment, and celebration, while supporting a worthy cause related to {topic}.",
    "Fundraiser": "The {event_type} on {topic} in {place} is dedicated to raising funds for important causes related to {topic}. Participate in auctions, enjoy performances, and contribute to a meaningful impact.",
    "Lecture": "Attend an enlightening {event_type} on {topic} at {place}. This session will delve into important concepts and discussions surrounding {topic}, offering participants a comprehensive understanding and new perspectives on the subject.",
    "Panel Discussion": "The {event_type} on {topic} in {place} brings together a panel of experts to discuss current issues and developments in {topic}. Engage with thought leaders and gain diverse perspectives on {topic}.",
    "Symposium": "The {event_type} on {topic} in {place} is an academic gathering that fosters deep discussion and exchange of ideas among scholars and professionals. This event will explore cutting-edge research and theories in {topic}.",
    "Product Launch": "Be the first to experience the latest innovations at the {event_type} on {topic} in {place}. Witness live demonstrations, hear from the creators, and get an exclusive look at the newest products in {topic}.",
    "Awards Ceremony": "Celebrate excellence at the {event_type} on {topic} in {place}. This prestigious event honors outstanding achievements in {topic}, recognizing individuals and organizations that have made significant contributions.",
    "Competition": "Showcase your skills at the {event_type} on {topic} in {place}. Compete with the best in the field and strive for victory in this exciting and challenging event.",
    "Meetup": "Connect with fellow enthusiasts at the {event_type} on {topic} in {place}. This casual gathering is a great opportunity to share ideas, collaborate on projects, and build community around {topic}.",
    "Hackathon": "Join us for an intense {event_type} on {topic} in {place}, where participants will collaborate to create innovative solutions to real-world problems in {topic}. Work against the clock, brainstorm ideas, and present your project to a panel of judges.",
    "Art Event": "Explore creativity and expression at the {event_type} on {topic} in {place}. This event showcases diverse artworks and performances that celebrate the beauty and impact of {topic} in the art world.",
    "Film Screening": "Join us for a special {event_type} on {topic} in {place}, featuring thought-provoking films that explore themes related to {topic}. Engage in post-screening discussions and connect with fellow cinephiles.",
    "Charity Event": "The {event_type} on {topic} in {place} is dedicated to supporting charitable causes through fun and engaging activities. Participate in auctions, enjoy live entertainment, and make a difference in the community.",
    "Book Launch": "Celebrate the release of a new literary work at the {event_type} on {topic} in {place}. Meet the author, hear readings, and get an exclusive first look at the book's themes and stories.",
    "Cooking Class": "Learn the art of culinary mastery at the {event_type} on {topic} in {place}. This hands-on class will teach you techniques and recipes from {topic}, perfect for aspiring chefs and food enthusiasts.",
    "Theater Performance": "Experience the magic of live theater at the {event_type} on {topic} in {place}. Enjoy captivating performances, innovative staging, and powerful storytelling in this unique theatrical event.",
    "Dance Show": "Get ready to move and groove at the {event_type} on {topic} in {place}. This vibrant performance will showcase the best of {topic} dance, featuring talented performers and electrifying choreography.",
    "Fashion Show": "Explore the latest trends and styles at the {event_type} on {topic} in {place}. This high-fashion event will feature top designers, models, and stunning collections that define the future of {topic}.",
    "Science Fair": "Discover the wonders of science at the {event_type} on {topic} in {place}. Students and professionals alike will showcase innovative projects and experiments that demonstrate the power and potential of science in {topic}.",
    "Tech Demo": "Get a firsthand look at emerging technologies at the {event_type} on {topic} in {place}. This demonstration event will feature live presentations and interactive exhibits showcasing the latest tech innovations.",
    "Product Fair": "The {event_type} on {topic} in {place} is a marketplace for discovering new products and services related to {topic}. Engage with vendors, explore a wide range of offerings, and find the perfect solutions for your needs.",
    "Community Gathering": "The {event_type} on {topic} in {place} is a celebration of community spirit. Join local residents for a day of activities, socializing, and shared experiences that foster a sense of belonging and camaraderie.",
    "Health Workshop": "Enhance your well-being at the {event_type} on {topic} in {place}. This workshop focuses on practical strategies and techniques for improving your health, featuring expert advice and interactive sessions.",
    "Startup Pitch": "Watch the next big ideas take flight at the {event_type} on {topic} in {place}. Startup founders will pitch their innovative concepts to a panel of investors and industry experts, competing for funding and support.",
    "Yoga Session": "Find your zen at the {event_type} on {topic} in {place}. This yoga session will guide you through relaxing and invigorating practices designed to improve your physical and mental well-being.",
    "Meditation Retreat": "Join us for a serene {event_type} on {topic} in {place}. This retreat offers a peaceful environment for deepening your meditation practice, with guided sessions and workshops designed to promote mindfulness and relaxation.",
    "Photography Exhibit": "Explore stunning visual art at the {event_type} on {topic} in {place}. This exhibit features captivating photographs that capture the essence and diversity of {topic}, presented by talented photographers.",
    "Cultural Festival": "Immerse yourself in diverse traditions at the {event_type} on {topic} in {place}. Enjoy performances, food, and art that celebrate the rich cultural heritage and artistic expressions of {topic}.",
    "Pop-up Market": "Discover unique finds at the {event_type} on {topic} in {place}. This temporary market features a variety of vendors offering artisanal goods, crafts, and local products related to {topic}.",
    "Culinary Festival": "Savor the flavors at the {event_type} on {topic} in {place}. This festival highlights culinary delights from around the world, with food tastings, cooking demonstrations, and gastronomic experiences centered around {topic}.",
    "Career Fair": "Explore job opportunities and career advancement at the {event_type} on {topic} in {place}. Meet with recruiters, attend workshops, and network with professionals to find your next career move in {topic}.",
    "Job Fair": "Connect with potential employers at the {event_type} on {topic} in {place}. This event features a wide range of companies looking to hire talented individuals for positions related to {topic}.",
    "Live Podcast": "Join us for a dynamic {event_type} on {topic} in {place}. This live podcast recording will feature engaging discussions and interviews with experts in {topic}, providing valuable insights and entertainment.",
    "TEDx Talk": "Be inspired at the {event_type} on {topic} in {place}. This TEDx event features a series of thought-provoking talks by innovators and leaders who will share their ideas and experiences on {topic}.",
    "Music Festival": "Enjoy an unforgettable experience at the {event_type} on {topic} in {place}. This festival brings together top musical acts and diverse genres, creating a vibrant atmosphere for music lovers.",
    "Game Jam": "Showcase your game development skills at the {event_type} on {topic} in {place}. This event challenges participants to create innovative games within a set timeframe, with opportunities for collaboration and networking.",
    "Design Sprint": "Participate in a focused {event_type} on {topic} in {place}. This intensive workshop guides teams through a structured process to solve design challenges and develop solutions rapidly.",
    "Innovation Summit": "Explore the future of {topic} at the {event_type} on {topic} in {place}. This summit brings together thought leaders and innovators to discuss groundbreaking ideas and trends shaping the industry.",
    "Climate Summit": "Address global environmental issues at the {event_type} on {topic} in {place}. This summit gathers experts, activists, and policymakers to discuss and develop strategies for combating climate change.",
    "Art Installation": "Experience immersive art at the {event_type} on {topic} in {place}. This event features unique art installations that engage the senses and provoke thought, showcasing the creative possibilities of {topic}.",
    "Public Debate": "Engage in important discussions at the {event_type} on {topic} in {place}. This debate will feature prominent speakers discussing critical issues related to {topic}, encouraging diverse viewpoints and dialogue.",
    "Social Media Workshop": "Enhance your online presence at the {event_type} on {topic} in {place}. This workshop provides practical tips and strategies for effectively using social media platforms to achieve your goals.",
    "Travel Expo": "Discover exciting destinations at the {event_type} on {topic} in {place}. This expo features travel agencies, tour operators, and travel experts showcasing the latest trends and offers in the travel industry.",
    "Real Estate Expo": "Explore property opportunities at the {event_type} on {topic} in {place}. This expo brings together real estate professionals, developers, and potential buyers to discuss trends and find investment opportunities.",
    "Investment Forum": "Gain insights into financial opportunities at the {event_type} on {topic} in {place}. This forum features expert panels and discussions on investment strategies and market trends in {topic}.",
    "Philosophy Lecture": "Delve into profound concepts at the {event_type} on {topic} in {place}. This lecture will explore key philosophical ideas and their relevance to contemporary issues in {topic}.",
    "Political Debate": "Join the conversation at the {event_type} on {topic} in {place}. This debate features political candidates and experts discussing current issues and policies related to {topic}.",
    "Economic Forum": "Analyze global economic trends at the {event_type} on {topic} in {place}. This forum brings together economists, policymakers, and business leaders to discuss economic challenges and opportunities.",
    "Mindfulness Workshop": "Enhance your well-being at the {event_type} on {topic} in {place}. This workshop focuses on mindfulness practices and techniques designed to improve mental health and stress management.",
    "Leadership Summit": "Develop your leadership skills at the {event_type} on {topic} in {place}. This summit offers insights and strategies from top leaders, providing valuable lessons for aspiring and current leaders.",
    "Employee Training": "Improve workplace skills at the {event_type} on {topic} in {place}. This training session offers practical knowledge and techniques for enhancing job performance and professional development.",
    "Customer Appreciation Event": "Show gratitude to your clients at the {event_type} on {topic} in {place}. This event is dedicated to celebrating and acknowledging the support of valued customers with special activities and recognition.",
    "User Conference": "Learn about the latest updates and features at the {event_type} on {topic} in {place}. This conference gathers users and developers to share insights, experiences, and feedback on {topic}.",
    "Virtual Reality Expo": "Explore cutting-edge technology at the {event_type} on {topic} in {place}. This expo showcases the latest advancements in virtual reality, offering interactive experiences and demonstrations.",
    "AI Conference": "Discover the future of artificial intelligence at the {event_type} on {topic} in {place}. This conference features discussions and presentations on AI research, applications, and innovations.",
    "Blockchain Summit": "Understand the impact of blockchain technology at the {event_type} on {topic} in {place}. This summit explores blockchain applications, trends, and future directions in the industry.",
    "Cybersecurity Forum": "Address critical security issues at the {event_type} on {topic} in {place}. This forum brings together cybersecurity experts to discuss the latest threats, solutions, and best practices for protecting digital assets.",
    "Environmental Conference": "Examine sustainability issues at the {event_type} on {topic} in {place}. This conference focuses on environmental challenges and solutions, featuring discussions with experts and activists.",
    "Space Exploration Forum": "Explore the wonders of space at the {event_type} on {topic} in {place}. This forum features discussions on space missions, research, and future exploration endeavors.",
    "Science and Tech Expo": "Discover innovations in science and technology at the {event_type} on {topic} in {place}. This expo showcases groundbreaking research, technology advancements, and emerging trends.",
    "Artificial Intelligence Workshop": "Enhance your AI skills at the {event_type} on {topic} in {place}. This workshop offers hands-on training and insights into the latest developments and techniques in artificial intelligence.",
    "Digital Transformation Summit": "Navigate the digital landscape at the {event_type} on {topic} in {place}. This summit explores strategies for digital transformation and technology adoption in various industries."
}

dane_list = []


# Define a function to create a random event
for i in range(ile_eventow):
    event_type = fake.random_element(event_types)
    topic = fake.random_element(topics)
    place = fake.random_element(places)

    today = datetime.today().date()
    days_in_future = random.randint(1, 365)  # Losujemy liczbę dni od 1 do 365
    future_date = today + timedelta(days=days_in_future)

    while True:
        end_start = random.randint(1, 365)  # Losujemy liczbę dni od 1 do 365
        end_start_t = today + timedelta(days=end_start)
        if end_start_t >= future_date:
            break

    # Get the description template for the event type
    description_template = descriptions.get(event_type, "Event description not found.")

    # Generate the description using the template
    description = description_template.format(event_type=event_type, topic=topic, place=place)
    # Return the event details
    data = {
        "event_type": event_type,
        "topic": topic,
        'start_at': str(future_date),
        'end_start': str(end_start_t),
        "place": place,
        "description": description
    }
    dane_list.append(data)

# Ścieżka do pliku, w którym zapisane będą dane
file_path = 'events.json'

# Zapisywanie danych do pliku
with open(file_path, 'w', encoding='utf-8') as json_file:
    json.dump(dane_list, json_file, ensure_ascii=False, indent=4)

print(f"Dane zostały zapisane do pliku {file_path}.")
end_time = time.time()
execution_time = end_time - start_time
print(f"Caly skrypt wykowywal sie: {execution_time}")
execution_time_t = execution_time - execution_time_places
print(f"Zapisywanie wykonywalo sie: {execution_time_t}")
