import requests
import time
import random

# API Configuration
URL = "https://api.hyperbolic.xyz/v1/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer YOUR_API_KEY_HERE"
}

# List of 353 unique questions
questions = [
    
    "How do migratory birds navigate thousands of miles without getting lost?",  
    "What childhood memory still brings a smile to your face whenever you think about it?",  
    "If you could instantly master any musical instrument, which one would you choose?",  
    "Why do some people develop allergies later in life while others never do?",  
    "What fictional world from a book or movie would you want to live in?",  
    "How does the human brain prioritize memories during sleep?",  
    "If you could invent a new holiday, what would it celebrate?",  
    "Why do certain cultures associate specific colors with emotions or events?",  
    "What unexplored ocean depth mystery do you wish scientists could solve?",  
    "If you could grow a garden of mythical plants, what would they do?",  
    "What everyday object would you improve to make life easier for everyone?",  
    "How do animals perceive time compared to humans?",  
    "If you could eliminate one source of stress from modern life, what would it be?",  
    "What historical figure’s diary would you most want to read?",  
    "Why do some languages have words for emotions that others don’t?",  
    "If you could design a utopian society, what rule would you enforce first?",  
    "What natural phenomenon do you find most terrifying yet fascinating?",  
    "How would humanity change if we discovered life on another planet?",  
    "If you could taste a color, which one would you try first?",  
    "What skill do you think every person should learn by age 18?",  
    "Why do certain smells trigger vivid memories more than other senses?",  
    "If you could communicate with plants, what would you ask them?",  
    "What traditional practice from another culture do you admire most?",  
    "How do you think artificial intelligence will redefine creativity?",  
    "What unsolved mystery from history keeps you awake at night?",  
    "If you could erase a single invention from existence, which would it be?",  
    "Why do some people thrive under pressure while others crumble?",  
    "What childhood game or activity do you wish adults still played?",  
    "If you could preserve one aspect of modern life for future generations, what would it be?",  
    "How would you describe the concept of time to an alien species?",  
    "What animal trait would you want to temporarily borrow for a day?",  
    "If you could create a new genre of music, what would it sound like?",  
    "Why do humans feel nostalgia even for unpleasant past experiences?",  
    "What seemingly insignificant invention has had the biggest impact on humanity?",  
    "If you could witness any event from the past in person, what would it be?",  
    "How do you think social dynamics would change if humans could read minds?",  
    "What mythical creature’s existence would most disrupt the modern world?",  
    "If you could make one food taste calorie-free, which would you pick?",  
    "Why do some people find comfort in routines while others crave spontaneity?",  
    "What scientific breakthrough do you hope happens in your lifetime?",  
    "If you could replace all roads in the world with one mode of transport, what would it be?",  
    "How would society be if men were animals?",
    "What is the color of the sky on a clear day?",  
    "Can penguins fly like other birds?",  
    "Why do leaves change color in autumn?",  
    "How does a microwave oven heat food?",  
    "Would you survive on Mars without a spacesuit?",  
    "What causes the Northern Lights to shimmer?",  
    "Are diamonds truly the hardest natural material?",  
    "Who invented the first functional telephone?",  
    "Does time travel violate the laws of physics?",  
    "Which planet has the most moons in our solar system?",  
    "Is laughter the best medicine for stress?",  
    "Can plants communicate with each other?",  
    "What defines the taste of umami?",  
    "Why do humans dream during sleep?",  
    "Will artificial intelligence surpass human intelligence?",  
    "Where is the world’s deepest ocean trench?",  
    "Has a human ever walked on Venus?",  
    "Should voting be mandatory in democracies?",  
    "Does the Great Wall of China span multiple countries?",  
    "How do vaccines train the immune system?",  
    "Are black holes gateways to other universes?",  
    "What triggers a volcanic eruption?",  
    "Can silence truly convey meaning?",  
    "Why do some languages lack words for colors?",  
    "Was Atlantis a real or mythical civilization?",  
    "Which animal has the longest lifespan?",  
    "Does chewing gum digest in your stomach?",  
    "Who wrote the first computer algorithm?",  
    "Are there undiscovered elements in the universe?",  
    "Why do stars twinkle at night?",  
    "Can you hear sounds in outer space?",  
    "What makes the Mona Lisa so famous?",  
    "Is there a genetic basis for creativity?",  
    "Should animals have legal rights?",  
    "How do migratory birds navigate continents?",  
    "Would life exist without photosynthesis?",  
    "Does every culture celebrate birthdays?",  
    "What inspired Shakespeare’s *Hamlet*?",  
    "Are mirror images reversed horizontally or vertically?",  
    "Why do onions make people cry?",
    "Why do people blush when embarrassed?",  
    "How do satellites stay in orbit around Earth?",  
    "What is the evolutionary purpose of laughter?",  
    "Why do some stones spark when struck?",  
    "How do artists create perspective in paintings?",  
    "What causes the different flavors in cheeses?",  
    "Why do tornadoes form in specific regions?",  
    "How do chameleons change their skin color?",  
    "What is the connection between the moon and ocean tides?",  
    "Why do some animals have venomous bites?",  
    "How do virtual assistants like Siri understand speech?",  
    "What is the difference between a virus and a bacterium?",  
    "Why do humans have appendixes if they’re not essential?",  
    "How do architects design earthquake-resistant buildings?",  
    "What causes the green color in auroras?",  
    "Why do tea leaves settle at the bottom of a cup?",  
    "How do roller coasters stay on their tracks during loops?",  
    "What is the function of a neuron in the nervous system?",  
    "Why do some cultures consider certain numbers lucky or unlucky?",  
    "How do electric cars store and use energy?",  
    "What is the composition of Saturn’s rings?",  
    "Why do people develop phobias?",  
    "How do forensic scientists solve crimes using DNA?",  
    "What causes the hissing sound in soda cans when opened?",  
    "Why do some plants trap insects?",  
    "How do time zones work across the globe?",  
    "What is the purpose of a black box in airplanes?",  
    "Why do humans dream in metaphors or symbols?",  
    "How do waterfalls continuously flow without running out of water?",  
    "What is the role of enzymes in digestion?",  
    "Why do some birds mimic human speech?",  
    "How do search engines rank websites?",  
    "What causes the sensation of ‘pins and needles’ in limbs?",  
    "Why do diamonds sparkle more than other gemstones?",  
    "How do astronauts train for zero-gravity environments?",  
    "What is the meaning of life?",
    "Why do some people have lactose intolerance?",  
    "What causes the sound of snoring?",  
    "How do vaccines eradicate diseases?",  
    "Why do some flowers bloom only once a year?",  
    "What is the function of the adrenal glands?",  
    "How do landslides occur?",  
    "Why do humans have different sleep patterns?",  
    "What is the significance of the Statue of Liberty?",  
    "How do voice assistants like Siri understand speech?",  
    "Why do some cultures practice meditation?",  
    "What is the process of composting organic waste?",  
    "How do sharks detect prey from afar?",  
    "Why do humans create art?",  
    "What causes the formation of rainbows at waterfalls?",  
    "How do 3D printers create objects?",  
    "Why do some societies have taboos around food?",  
    "What is the history of the Silk Road?",  
    "How do pain receptors send signals to the brain?",  
    "Why do humans have wisdom teeth?",  
    "What is the impact of deforestation on indigenous communities?",  
    "How do solar-powered calculators work?",  
    "Why do some people have a fear of public speaking?",  
    "What causes the formation of hailstones?",  
    "How do vaccines adapt to new virus strains?",  
    "Why do some animals form symbiotic relationships?",  
    "What is the role of the North Atlantic Treaty Organization?",  
    "How do squid change their skin texture?",  
    "Why do humans collect possessions?",  
    "What causes the northern and southern lights?",  
    "How do biometric scanners identify individuals?",  
    "Why do some cultures celebrate coming-of-age ceremonies?",  
    "What is the history of the Industrial Revolution?",  
    "How do antidepressants affect brain chemistry?",  
    "Why do humans have belly buttons?",  
    "What is the impact of air travel on the environment?",  
    "How do electric trains operate without fuel?",  
    "Why do some people have a natural talent for music?",  
    "What causes the formation of sinkholes?",  
    "How do vaccines use weakened pathogens?",  
    "Why do some plants trap insects?",  
    "What is the function of the pineal gland?",  
    "How do sand dunes shift over time?",  
    "Why do humans have different cultural norms?",  
    "What is the significance of the Great Barrier Reef?",  
    "How do facial recognition systems work?",  
    "Why do some societies value oral traditions?",  
    "What is the process of making chocolate from cocoa beans?",  
    "How do bats use echolocation to navigate?",  
    "Why do humans form emotional attachments to pets?",  
    "What causes the shimmering effect on hot roads?",  
    "How do solar sails propel spacecraft?",  
    "Why do some cultures practice ancestor worship?",  
    "What is the history of the space race?",  
    "How do anti-inflammatory drugs reduce swelling?",  
    "Why do humans have an appendix?",  
    "What is the impact of noise pollution on wildlife?",  
    "How do hydrogen fuel cells generate energy?",  
    "Why do some people have a fear of spiders?",  
    "What causes the formation of stalactites and stalagmites?",  
    "How do vaccines protect future generations?",  
    "Why do some trees live for thousands of years?",  
    "What is the role of the Red Cross in global crises?",  
    "How do cuttlefish blend into their surroundings?",  
    "Why do humans create complex social hierarchies?",  
    "What causes the phenomenon of ball lightning?",  
    "How do quantum computers solve complex problems?",  
    "Why do some cultures emphasize hospitality?",  
    "What is the history of the Declaration of Independence?",  
    "How do antidepressants balance neurotransmitters?",  
    "Why do humans have different types of laughter?",  
    "What is the impact of light pollution on ecosystems?",  
    "How do tidal power plants generate electricity?",  
    "Why do some people have a natural sense of direction?",
    "Have you ever wondered why the sky appears blue during the day but red at sunset?",  
    "What would happen if humans could photosynthesize like plants?",  
    "How do fireflies produce light without generating heat?",  
    "Can a person truly forget how to ride a bicycle once they’ve learned?",  
    "Why do some people hear colors or see sounds through synesthesia?",  
    "What drives the migratory patterns of monarch butterflies across continents?",  
    "Is it possible to measure the weight of a cloud?",  
    "Why do certain smells trigger vivid childhood memories?",  
    "How do whales communicate across vast ocean distances?",  
    "What would Earth look like if all its ice melted overnight?",  
    "Can a machine ever develop a sense of creativity or originality?",  
    "Why do leaves change color in the fall but not in tropical regions?",  
    "How do astronauts cope with the psychological effects of long space missions?",  
    "What causes the sensation of déjà vu, and is it universal?",  
    "Would humanity survive if bees went extinct globally?",  
    "How do desert plants store water for years without rainfall?",  
    "Can silence truly be measured in decibels?",  
    "Why do humans instinctively fear the dark?",  
    "What defines the line between a pond and a lake?",  
    "How do migratory birds navigate using Earth’s magnetic field?",  
    "Can a lie detector ever be 100% accurate?",  
    "Why do some cultures celebrate festivals with fire while others avoid it?",  
    "What would happen if the moon suddenly disappeared?",  
    "How do chameleons change their skin color so rapidly?",  
    "Why do some people remember dreams vividly while others don’t?",  
    "Can animals experience emotions like grief or joy?",  
    "What causes the hypnotic spiral patterns in sunflowers?",  
    "How do glaciers carve entire valleys over millennia?",  
    "Why do humans find symmetry aesthetically pleasing?",  
    "What would happen if all fungi vanished from ecosystems?",  
    "How do octopuses camouflage so effectively without mirrors?",  
    "Can a person survive drinking only seawater?",  
    "Why do some languages have no words for specific colors?",  
    "How do seeds know when to germinate after winter?",  
    "What causes the crackling sound of a campfire?",  
    "Why do humans develop accents when learning new languages?",  
    "Can a computer virus ever infect a human-made device?",  
    "How do tornadoes form with such destructive precision?",  
    "Why do some rocks float on water while others sink?",  
    "What makes yawning contagious across species?",  
    "How do deep-sea creatures survive extreme pressure and darkness?",  
    "Can a plant grow without sunlight using artificial alternatives?",  
    "Why do fingerprints differ even between identical twins?",  
    "What causes the iridescent shimmer on soap bubbles?",  
    "How do schools of fish move in perfect unison?",  
    "Why do some people sneeze when exposed to bright light?",  
    "Can a person’s blood type influence their personality traits?",  
    "How do diamonds form deep within the Earth’s mantle?",  
    "What causes the eerie glow of bioluminescent algae?",  
    "Why do humans build monuments to honor the past?",  
    "How do viruses mutate to evade immune systems?",  
    "Can a pendulum ever swing indefinitely without energy loss?",  
    "Why do some cultures revere certain animals as sacred?",  
    "How do mountains influence local weather patterns?",  
    "What causes the hypnotic effect of flickering flames?",  
    "Why do humans crave sugary foods despite health risks?",  
    "Can a robot ever achieve self-awareness through programming?",  
    "How do cicadas emerge en masse after years underground?",  
    "Why do stars twinkle while planets remain steady in the night sky?",  
    "What drives the formation of hexagonal basalt columns?",  
    "How do memories form and fade in the human brain?",  
    "Why do some people excel at multitasking while others struggle?",  
    "Can a person truly be allergic to water?",
    "What's the best way to learn programming?",
    "How does quantum computing work?",
    "What are some healthy breakfast ideas?",
    "Can you explain blockchain technology?",
    "What's the weather like on Mars?",
    "How do I improve my photography skills?",
    "What are the benefits of meditation?",
    "How does artificial intelligence work?",
    "What's the history of the internet?",
    "Can you suggest some good books to read?",
    "What’s the meaning of life?",
    "How do I make a perfect cup of coffee?",
    "What are the latest space discoveries?",
    "How can I stay motivated to exercise?",
    "What’s the future of electric cars?",
    "How do I start a small business?",
    "What are some fun weekend activities?",
    "Can you explain the theory of relativity?",
    "What’s the best way to learn a language?",
    "How does the stock market work?",
    "What’s the best way to save money?",
    "How do I plan a trip abroad?",
    "What are the effects of climate change?",
    "How does Wi-Fi actually work?",
    "What’s the history of video games?",
    "How can I improve my public speaking?",
    "What’s the science behind rainbows?",
    "How do I grow indoor plants successfully?",
    "What are the benefits of drinking water?",
    "How does cryptocurrency mining work?",
    "What’s the history of chocolate?",
    "How can I reduce stress in my life?",
    "What are some tips for better sleep?",
    "How do solar panels generate electricity?",
    "What’s the best way to cook steak?",
    "How does the human brain process memory?",
    "What are some must-visit places in Europe?",
    "How do I start investing in stocks?",
    "What’s the difference between viruses and bacteria?",
    "How can I make my home more eco-friendly?",
    "What’s the history of the Olympic Games?",
    "How do I train a dog effectively?",
    "What are the benefits of yoga?",
    "How does 3D printing work?",
    "What’s the best way to learn guitar?",
    "How do airplanes stay in the air?",
    "What are some creative writing tips?",
    "How does the immune system fight diseases?",
    "What’s the future of space travel?",
    "How can I improve my time management?",
    "What’s the history of pizza?",
    "How do I create a budget?",
    "What are the benefits of recycling?",
    "How does virtual reality work?",
    "What’s the best way to study for exams?",
    "How do I make homemade bread?",
    "What are the causes of global warming?",
    "How does GPS technology work?",
    "What’s the history of photography?",
    "How can I boost my creativity?",
    "What are some tips for healthy eating?",
    "How do self-driving cars function?",
    "What’s the best way to learn cooking?",
    "How does the moon affect tides?",
    "What are some fun science experiments?",
    "How do I start a podcast?",
    "What’s the history of democracy?",
    "How can I improve my drawing skills?",
    "What are the benefits of journaling?",
    "How does nuclear energy work?",
    "What’s the best way to plan a party?",
    "How do I maintain a car properly?",
    "What are some tips for traveling cheap?",
    "How does the internet of things work?",
    "What’s the history of coffee?",
    "How can I learn to code faster?",
    "What are the benefits of team sports?",
    "How do black holes form?",
    "What’s the best way to declutter my home?",
    "How does machine learning differ from AI?",
    "What are some tips for gardening?",
    "How do I make a good first impression?",
    "What’s the history of the English language?",
    "How can I stay productive working from home?",
    "What are the benefits of learning history?",
    "How does the human eye see color?",
    "What’s the best way to train for a marathon?",
    "How do I start a blog?",
    "What are some unusual animal facts?",
    "How does sound travel through the air?",
    "What’s the history of fashion?",
    "How can I improve my negotiation skills?",
    "What are the benefits of mindfulness?",
    "How do I build a simple website?",
    "What’s the best way to learn math?",
    "How does evolution work?",
    "What are some tips for reducing waste?",
    "How do I choose a good wine?",
    "What’s the future of renewable energy?"
]

# Verify we have 353 questions
print(f"Total questions loaded: {len(questions)}")

# Function to send API request
def send_chat_request(question):
    data = {
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ],
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9
    }
    
    try:
        response = requests.post(URL, headers=HEADERS, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# Main bot loop
def run_chat_bot():
    print("Starting automated chat bot...")
    available_questions = questions.copy()  # Work with a copy to preserve original list
    
    for i in range(353):  # Fixed to 353 since we have exactly 353 questions
        if not available_questions:
            print("Ran out of questions unexpectedly!")
            break
        
        # Pick and remove a random question to avoid repetition
        question = random.choice(available_questions)
        available_questions.remove(question)
        
        # Send request and print results
        print(f"\nQuestion {i + 1}: {question}")
        answer = send_chat_request(question)
        print(f"Answer: {answer}")
        
        # Random delay between 1-2 minutes (60-120 seconds)
        delay = random.uniform(60, 120)
        print(f"Waiting {delay:.1f} seconds before next question...")
        time.sleep(delay)
    
    print("\nCompleted 353 questions!")

# Run the bot
if __name__ == "__main__":
    run_chat_bot()
