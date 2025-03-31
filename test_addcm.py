import datetime
from pymongo import MongoClient
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
DB_url=config['MONGODB']['DB_URL']


client = MongoClient(DB_url)
db = client['database']

comments = [
    {"name": 'Dune', 'comment': 'A visually stunning and immersive experience that expertly adapts the complex source material. The cinematography and score are breathtaking, immersing the audience in the vastness of Arrakis. Timothée Chalamet delivers a compelling performance as Paul Atreides.', "datetime": datetime.datetime.now()},
    
    {"name": 'Spider-Man: No Way Home', 'comment': 'An emotional rollercoaster that brilliantly integrates multiple universes and beloved characters. The film captures the essence of Spider-Man while exploring Peter Parker’s growth and the consequences of his choices. A must-watch for fans!', "datetime": datetime.datetime.now()},
    
    {"name": 'The Power of the Dog', 'comment': 'An intricately woven tale that explores masculinity, repression, and family dynamics. The performances, especially from Benedict Cumberbatch, are exceptional, and Jane Campion’s direction is masterful. A haunting and thought-provoking film.', "datetime": datetime.datetime.now()},
    
    {"name": 'No Time to Die', 'comment': 'A fitting farewell to Daniel Craigs Bond, this film balances action with emotional depth. It ties up loose ends while introducing new characters and challenges. The stunning visuals and intense action sequences make it a thrilling ride.', "datetime": datetime.datetime.now()},
    
    {"name": 'Encanto', 'comment': 'A heartwarming animated film that beautifully showcases Colombian culture. The music is catchy, and the themes of family and self-acceptance resonate deeply. Disney has created another magical experience that appeals to all ages.', "datetime": datetime.datetime.now()},
    
    {"name": 'The French Dispatch', 'comment': 'A delightful homage to journalism, filled with quirky characters and rich storytelling. Wes Andersons unique visual style shines through, creating a whimsical yet profound narrative. Its a treat for fans of both cinema and the written word.', "datetime": datetime.datetime.now()},
    
    {"name": 'Ghostbusters: Afterlife', 'comment': 'A nostalgic return that honors the original films while introducing a new generation to the Ghostbusters legacy. The humor, heart, and homage to the past make it a fun and enjoyable experience for fans old and new.', "datetime": datetime.datetime.now()},
    
    {"name": 'West Side Story', 'comment': 'A beautifully crafted remake that captures the spirit of the original while adding modern sensibilities. The choreography, music, and performances are superb, making it a spectacular musical that stands on its own.', "datetime": datetime.datetime.now()},
    
    {"name": 'Licorice Pizza', 'comment': 'A charming and authentic coming-of-age story that captures the essence of youthful love and adventure in the 1970s. Paul Thomas Anderson’s direction brings warmth and nostalgia, with standout performances that make it a delightful watch.', "datetime": datetime.datetime.now()},


    # Dune
    {"name": 'Dune', 'comment': 'An epic journey that brilliantly tackles themes of power and prophecy. The performances are strong, especially from Rebecca Ferguson and Oscar Isaac, adding an emotional layer to the story.', "datetime": datetime.datetime.now()},
    {"name": 'Dune', 'comment': 'The attention to detail in the world-building is incredible. Each element feels meticulously crafted, from the costumes to the landscapes. A true cinematic achievement!', "datetime": datetime.datetime.now()},
    {"name": 'Dune', 'comment': 'While the pacing may be slow for some, it allows for a deeper understanding of the characters and their motivations. A film that demands patience but rewards it handsomely.', "datetime": datetime.datetime.now()},
    {"name": 'Dune', 'comment': 'Hans Zimmer’s score elevates the film to another level, creating an atmosphere that feels both alien and familiar. It’s a character in its own right.', "datetime": datetime.datetime.now()},
    {"name": 'Dune', 'comment': 'The cinematography is breathtaking, making Arrakis feel like a character itself. It’s a feast for the eyes that leaves you eager for the next chapter.', "datetime": datetime.datetime.now()},

    # Spider-Man: No Way Home
    {"name": 'Spider-Man: No Way Home', 'comment': 'An exhilarating ride that pays homage to the entire Spider-Man legacy. It’s filled with nostalgia that brought tears to many fans’ eyes.', "datetime": datetime.datetime.now()},
    {"name": 'Spider-Man: No Way Home', 'comment': 'The chemistry between Tom Holland and the returning characters is fantastic, adding rich layers to the story. It feels like a celebration of everything Spider-Man.', "datetime": datetime.datetime.now()},
    {"name": 'Spider-Man: No Way Home', 'comment': 'The visual effects are spectacular, bringing the multiverse to life in a stunning way. The action sequences are both thrilling and well choreographed.', "datetime": datetime.datetime.now()},
    {"name": 'Spider-Man: No Way Home', 'comment': 'A great blend of humor, action, and emotional depth. The narrative takes bold risks that pay off beautifully, making it one of the best Spider-Man films yet.', "datetime": datetime.datetime.now()},
    {"name": 'Spider-Man: No Way Home', 'comment': 'This film raises the stakes for Peter Parker in a way that feels authentic and impactful. It’s a painful journey that layers the character with rich depth.', "datetime": datetime.datetime.now()},

    # The Power of the Dog
    {"name": 'The Power of the Dog', 'comment': 'A masterclass in subtlety, where every glance and silence holds meaning. The character development is profound, keeping the viewer engaged on multiple levels.', "datetime": datetime.datetime.now()},
    {"name": 'The Power of the Dog', 'comment': 'The cinematography captures the vast landscapes beautifully, complementing the tense narrative. It’s as much a visual experience as it is an emotional one.', "datetime": datetime.datetime.now()},
    {"name": 'The Power of the Dog', 'comment': 'The film weaves its themes of jealousy and masculinity with such skill that it leaves you pondering long after the credits roll. A remarkable achievement.', "datetime": datetime.datetime.now()},
    {"name": 'The Power of the Dog', 'comment': 'With its pacing and tension, the film feels like a slow burn that ultimately leads to a stunning climax. A must-see for lovers of character-driven stories.', "datetime": datetime.datetime.now()},
    {"name": 'The Power of the Dog', 'comment': 'A haunting score perfectly complements the film’s atmosphere, deepening the emotional impact of every scene. A thoughtful exploration of human nature.', "datetime": datetime.datetime.now()},

    # No Time to Die
    {"name": 'No Time to Die', 'comment': 'A thrilling farewell to James Bond that delivers everything fans have come to expect. The action is intense and the stakes have never felt higher.', "datetime": datetime.datetime.now()},
    {"name": 'No Time to Die', 'comment': 'The emotional depth adds a significant layer to the typical Bond formula, making it stand out in the franchise. Craig’s performance is deeply impactful.', "datetime": datetime.datetime.now()},
    {"name": 'No Time to Die', 'comment': 'Stunning cinematography showcases beautiful locations that elevate the storytelling. It truly feels like an international adventure.', "datetime": datetime.datetime.now()},
    {"name": 'No Time to Die', 'comment': 'The balance between action, humor, and heartfelt moments is expertly handled, resulting in a film that appeals to a wide audience.', "datetime": datetime.datetime.now()},
]

db['comment'].insert_many(comments)