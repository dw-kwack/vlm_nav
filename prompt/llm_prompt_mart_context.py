import os
import openai

def parse_object_goal_instruction(language_instr):
 
    openai_key = os.environ["OPENAI_KEY"]
    openai.api_key = openai_key
    client = openai.OpenAI(api_key=openai_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
           {"role": "user", "content": "I want to see ancient Egyptian artifacts"},
    {"role": "assistant", "content": "Tutankhamun's Mask, Rosetta Stone, Statue of Ramses II"},
    
    {"role": "user", "content": "I'm interested in modern sculptures"},
    {"role": "assistant", "content": "Bird in Space, Brancusi, The Thinker, Rodin"},
    
    {"role": "user", "content": "I like Renaissance paintings"},
    {"role": "assistant", "content": "Mona Lisa, Leonardo da Vinci, The Birth of Venus, Botticelli"},
    
    {"role": "user", "content": "I'm fascinated by medieval armor"},
    {"role": "assistant", "content": "The Black Prince's Shield, Gothic Plate Armor, Maximilian Armor"},
    
    {"role": "user", "content": "I'm curious about prehistoric art"},
    {"role": "assistant", "content": "The Venus of Willendorf, Lascaux Cave Paintings, Altamira Bison"},
    
    {"role": "user", "content": "I want to see Baroque architecture"},
    {"role": "assistant", "content": "St. Peter's Basilica, Versailles Palace, Schönbrunn Palace"},
    
    {"role": "user", "content": "I like Impressionist paintings"},
    {"role": "assistant", "content": "Water Lilies, Monet, Luncheon of the Boating Party, Renoir"},
    
    {"role": "user", "content": "I'm interested in Greek sculptures"},
    {"role": "assistant", "content": "Venus de Milo, Discobolus, Laocoön and His Sons"},
    
    {"role": "user", "content": "I want to see famous Asian artifacts"},
    {"role": "assistant", "content": "Terracotta Army, Great Buddha of Kamakura, Jade Dragon"},
    
    {"role": "user", "content": "I'm fascinated by Roman architecture"},
    {"role": "assistant", "content": "The Colosseum, Pantheon, Roman Aqueducts"},
    
    {"role": "user", "content": "I want to see medieval manuscripts"},
    {"role": "assistant", "content": "The Book of Kells, Lindisfarne Gospels, Codex Sinaiticus"},
    
    {"role": "user", "content": "I'm interested in famous statues"},
    {"role": "assistant", "content": "Statue of Liberty, Christ the Redeemer, Michelangelo's David"},
    
    {"role": "user", "content": "I want to see famous European landmarks"},
    {"role": "assistant", "content": "Eiffel Tower, Big Ben, Colosseum"},
    
    {"role": "user", "content": "I like contemporary art"},
    {"role": "assistant", "content": "Campbell's Soup Cans, Andy Warhol, Balloon Dog, Jeff Koons"},
    
    {"role": "user", "content": "I'm interested in Islamic art"},
    {"role": "assistant", "content": "Alhambra, Blue Mosque, Persian Miniatures"},
    
    {"role": "user", "content": "I want to see famous jewelry"},
    {"role": "assistant", "content": "Crown Jewels, Hope Diamond, Koh-i-Noor"},
    
    {"role": "user", "content": "I like ancient Mesopotamian artifacts"},
    {"role": "assistant", "content": "Stele of Hammurabi, Ishtar Gate, Ziggurat of Ur"},
    
    {"role": "user", "content": "I'm fascinated by indigenous art"},
    {"role": "assistant", "content": "Maori Carvings, Native American Totem Poles, Aboriginal Rock Art"},
    
    {"role": "user", "content": "I want to see Viking artifacts"},
    {"role": "assistant", "content": "Viking Helmets, Oseberg Ship, Thor's Hammer Pendants"},
    
    {"role": "user", "content": "I'm interested in African art"},
    {"role": "assistant", "content": "Benin Bronzes, Great Zimbabwe Ruins, Dogon Masks"},

    {"role": "user", "content": "I'm interested in korea art"},
    {"role": "assistant", "content": "Pensive Bodhisattva, Goryeo celadon"}
        ],
        max_tokens=300,
    )

    text = response.choices[0].message.content
    return [x.strip() for x in text.split(",")]

if __name__ == "__main__":
    text = parse_object_goal_instruction("i like traditional korea art in 1800s")
    print(text)