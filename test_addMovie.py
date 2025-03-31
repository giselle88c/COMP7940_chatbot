from pymongo import MongoClient
import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
DB_url=config['MONGODB']['DB_URL']


client = MongoClient(DB_url)
db = client['database']
collection = db['movie']

records = [
    {
        "movie_id": 1,
        "name": "Inception",
        "description": "A mind-bending thriller by Christopher Nolan that explores the concept of dreams within dreams. A skilled thief, Dom Cobb, has the rare ability to enter people's dreams and steal their secrets. Tasked with an impossible mission to implant an idea into a target's subconscious, Cobb assembles a team to navigate the complex layers of dreams and confront their own inner demons.",
        "movie_date": "2010-07-16",
        "duration": "148 minutes"
    },
    {
        "movie_id": 2,
        "name": "The Dark Knight",
        "description": "A thrilling tale of Batman and the Joker directed by Christopher Nolan. As Gotham City faces a wave of crime and chaos unleashed by the Joker, Batman must confront moral dilemmas and the consequences of his vigilante actions. The film explores themes of heroism, sacrifice, and the fine line between hero and villain.",
        "movie_date": "2008-07-18",
        "duration": "152 minutes"
    },
    {
        "movie_id": 3,
        "name": "The Shawshank Redemption",
        "description": "An inspiring drama about hope and friendship, centered around the lives of two men imprisoned for life. Andy Dufresne, wrongly convicted of murder, forms a bond with fellow inmate Red during their time at Shawshank State Penitentiary. Together, they navigate the harsh realities of prison life while holding onto their dreams of freedom.",
        "movie_date": "1994-09-23",
        "duration": "142 minutes"
    },
    {
        "movie_id": 4,
        "name": "Pulp Fiction",
        "description": "A stylistic thriller that intertwines various storylines, directed by Quentin Tarantino. The film follows the lives of hitmen, a boxer, a gangster's wife, and more, showcasing a non-linear narrative that redefines conventions of storytelling. With sharp dialogue and complex characters, it explores themes of redemption and morality.",
        "movie_date": "1994-10-14",
        "duration": "154 minutes"
    },
    {
        "movie_id": 5,
        "name": "The Godfather",
        "description": "An epic tale of family and power in the criminal underworld, directed by Francis Ford Coppola. Centered on the Corleone mafia family and their patriarch, Vito Corleone, the film delves into themes of loyalty, betrayal, and the American Dream, as Michael Corleone transforms from reluctant outsider to ruthless mafia boss.",
        "movie_date": "1972-03-24",
        "duration": "175 minutes"
    },
    {
        "movie_id": 6,
        "name": "Fight Club",
        "description": "A tale of identity and consumerism narrated by an unnamed protagonist, who forms an underground fight club as a form of male bonding and rebellion against societal norms. The film critiques consumer culture and explores concepts of masculinity, identity, and self-destruction, culminating in a stunning twist.",
        "movie_date": "1999-10-15",
        "duration": "139 minutes"
    },
    {
        "movie_id": 7,
        "name": "The Matrix",
        "description": "A science fiction classic that explores reality and illusion, directed by the Wachowskis. The film follows hacker Neo as he discovers the truth about his reality and joins a group of rebels fighting against machines that have enslaved humanity. With groundbreaking visuals and philosophical undertones, it questions the nature of existence.",
        "movie_date": "1999-03-31",
        "duration": "136 minutes"
    },
    {
        "movie_id": 8,
        "name": "Forrest Gump",
        "description": "The life journey of a simple man with a big heart, Forrest Gump, who unwittingly influences key historical events while pursuing his childhood love, Jenny. His story illustrates themes of innocence, love, and destiny as he traverses the challenges of life, embodying the spirit of optimism and perseverance.",
        "movie_date": "1994-07-06",
        "duration": "142 minutes"
    },
   
    {
        "movie_id": 9,
        "name": "Interstellar",
        "description": "A visually stunning journey through space and time, directed by Christopher Nolan. As Earth faces an ecological disaster, former NASA pilot Cooper is tasked with leading a team of explorers through a wormhole in search of a new home for humanity. The film delves into the complexities of love, sacrifice, and the limits of human ingenuity while confronting the mysteries of the universe.",
        "movie_date": "2014-11-07",
        "duration": "169 minutes"
    },
    {
        "movie_id": 10,
        "name": "Gladiator",
        "description": "A Roman general, Maximus Decimus Meridius, seeks revenge against a corrupt emperor who murdered his family and sent him into slavery. This epic historical drama directed by Ridley Scott showcases themes of honor, betrayal, and the quest for vengeance, set against the backdrop of ancient Roman society and its brutal gladiatorial games.",
        "movie_date": "2000-05-05",
        "duration": "155 minutes"
    },
    {
        "movie_id": 11,
        "name": "Infernal Affairs",
        "description": "A thrilling tale of undercover police and gangsters in Hong Kong, this film follows two moles: one planted by the Hong Kong police within a triad gang, and the other an undercover cop infiltrating the criminal organization. Their paths intersect in a tense psychological game of cat and mouse, culminating in a gripping showdown between duty and betrayal.",
        "movie_date": "2002-12-12",
        "duration": "101 minutes"
    },
    {
        "movie_id": 12,
        "name": "Chungking Express",
        "description": "A romantic drama interweaving the lives of two police officers and their intricate relationships in bustling Hong Kong. Directed by Wong Kar-wai, the film presents a unique narrative style and explores themes of love, loneliness, and the fleeting nature of time through a series of vignettes and vivid imagery.",
        "movie_date": "1994-05-19",
        "duration": "102 minutes"
    },
    {
        "movie_id": 13,
        "name": "The Grandmaster",
        "description": "A martial arts biopic of the legendary Wing Chun master Ip Man, this film directed by Wong Kar-wai chronicles Ip's life, his struggles, and his philosophy of martial arts. Through breathtaking fight sequences and rich cinematography, it explores themes of honor, tradition, and the impact of historical events on personal destiny.",
        "movie_date": "2013-01-08",
        "duration": "108 minutes"
    },
    {
        "movie_id": 14,
        "name": "Hero",
        "description": "An epic war film showcasing the beauty of martial arts and heroism. Directed by Zhang Yimou, the story unfolds through a series of visually stunning fight sequences and examines the concept of sacrifice for the greater good as a nameless warrior recounts his efforts to defeat an oppressive emperor.",
        "movie_date": "2002-10-24",
        "duration": "99 minutes"
    },
    {
        "movie_id": 15,
        "name": "Kung Fu Hustle",
        "description": "A comedic martial arts film that combines humor and action, directed by Stephen Chow. Set in 1940s Shanghai, the film follows a wannabe gangster who soon discovers his true potential and the hidden martial arts legends within a seemingly ordinary neighborhood, resulting in a vibrant mix of slapstick comedy and exhilarating fight scenes.",
        "movie_date": "2004-04-08",
        "duration": "99 minutes"
    },
    {
        "movie_id": 16,
        "name": "Crouching Tiger, Hidden Dragon",
        "description": "A visually stunning film that tells a tale of love and honor through martial arts, directed by Ang Lee. Set in 19th-century China, the story revolves around a stolen sword and the intertwining lives of warriors, including a noble heroine, a fierce swordswoman, and a mysterious bandit. The film vividly conveys themes of yearning, freedom, and the constraints of societal expectations.",
        "movie_date": "2000-12-08",
        "duration": "120 minutes"
    },
    
    {
        "movie_id": 17,
        "name": "The Killer",
        "description": "A story of an assassin's conflict between duty and love, directed by John Woo. The film follows an assassin who accidentally injures a woman during a hit and is deeply affected by the incident. Torn between his dangerous profession and his growing feelings for her, he seeks redemption while battling rivals, showcasing thrilling action sequences and emotional depth.",
        "movie_date": "1989-05-13",
        "duration": "111 minutes"
    },
    {
        "movie_id": 18,
        "name": "Police Story",
        "description": "A classic action-comedy thriller featuring Jackie Chan's signature stunts, directed by Benny Chan. The film follows Chan Ka-Kui, a cop who finds himself caught up in a battle against gangsters while trying to protect a key witness. Known for its breathtaking action sequences and humor, it blends martial arts with a light-hearted narrative.",
        "movie_date": "1985-12-14",
        "duration": "101 minutes"
    },
    {
        "movie_id": 19,
        "name": "A Better Tomorrow",
        "description": "A film about brotherhood and loyalty that reshaped the Hong Kong action genre, directed by John Woo. The story follows a reformed gangster and his struggle to reconcile his life choices with his younger brother, who is drawn into the world of crime. Featuring intense action sequences and poignant emotional moments, it explores themes of loyalty, sacrifice, and redemption.",
        "movie_date": "1986-05-01",
        "duration": "95 minutes"
    },
    
    {
        "movie_id": 20,
        "name": "The Wong Fei Hung Series",
        "description": "A series of films portraying the legendary martial artist Wong Fei Hung, celebrated for his skills in martial arts and his moral integrity. This franchise, which includes several adaptations, showcases Wong's exploits in fighting injustice while promoting traditional Chinese values. The films blend action, drama, and comedy, capturing the spirit of heroism in the face of adversity.",
        "movie_date": "1939-01-01",  
        "duration": "Varies"
    },

    {
        "movie_id": 21,
        "name": "Dune",
        "description": "A visually stunning adaptation of Frank Herbert's science fiction masterpiece, directed by Denis Villeneuve. The film follows young Paul Atreides as he navigates a world fraught with political intrigue and danger on the desert planet of Arrakis. With themes of destiny, power, and environmentalism, it showcases breathtaking visuals and an ensemble cast.",
        "movie_date": "2021-10-22",
        "duration": "155 minutes"
    },
    {
        "movie_id": 22,
        "name": "Spider-Man: No Way Home",
        "description": "Peter Parker faces unprecedented challenges as his identity as Spider-Man is revealed. In this thrilling continuation of the Spider-Man franchise, directed by Jon Watts, he seeks the help of Doctor Strange while dealing with villains from alternate realities. The film explores themes of responsibility, sacrifice, and the multiverse.",
        "movie_date": "2021-12-17",
        "duration": "148 minutes"
    },
    {
        "movie_id": 23,
        "name": "The Power of the Dog",
        "description": "Directed by Jane Campion, this Western drama explores themes of masculinity and repressed emotions. Set in the 1920s, the story follows Phil Burbank, a domineering rancher who confronts his repressed feelings when his brother marries a widow and brings her son to live on their ranch.",
        "movie_date": "2021-11-17",
        "duration": "126 minutes"
    },
    {
        "movie_id": 24,
        "name": "No Time to Die",
        "description": "Daniel Craig returns as James Bond in this thrilling installment of the iconic series. As Bond comes out of retirement to rescue a kidnapped scientist, he faces a mysterious villain armed with dangerous technology. Directed by Cary Joji Fukunaga, the film delves deep into Bond's emotional journey and legacy.",
        "movie_date": "2021-09-30",
        "duration": "163 minutes"
    },
    {
        "movie_id": 25,
        "name": "Encanto",
        "description": "A magical animated film by Disney that celebrates Colombian culture through the story of the Madrigal family, who possess unique talents except for Mirabel, the only ordinary child. When the magic surrounding their home starts to fade, Mirabel sets out to save the family's encanto, showcasing themes of family, identity, and acceptance.",
        "movie_date": "2021-11-24",
        "duration": "102 minutes"
    },
    {
        "movie_id": 26,
        "name": "The French Dispatch",
        "description": "Directed by Wes Anderson, this film is a love letter to journalists and the art of storytelling. Comprised of several vignettes, it follows the final issue of an American magazine published in a fictional French city, encapsulating whimsical characters and quirky narratives. Its unique visual style and humor make it a standout piece.",
        "movie_date": "2021-10-22",
        "duration": "108 minutes"
    },
    {
        "movie_id": 27,
        "name": "Ghostbusters: Afterlife",
        "description": "A nostalgic continuation of the Ghostbusters franchise, directed by Jason Reitman. The film follows a single mother and her two children who discover their connection to the original Ghostbusters in a small town. As supernatural forces awaken, they must embrace their legacy and save their community from a ghostly threat.",
        "movie_date": "2021-11-19",
        "duration": "124 minutes"
    },
    {
        "movie_id": 28,
        "name": "West Side Story",
        "description": "Directed by Steven Spielberg, this musical is a reimagining of the iconic 1961 film. Set in 1950s New York, it tells the timeless love story between Tony and Maria amid gang rivalry. With captivating choreography and a classic score, the film explores themes of love, conflict, and cultural identity.",
        "movie_date": "2021-12-10",
        "duration": "156 minutes"
    },
    {
        "movie_id": 29,
        "name": "Licorice Pizza",
        "description": "Set in the 1970s San Fernando Valley, this coming-of-age film directed by Paul Thomas Anderson follows the romantic and friendship dynamics between a teenage girl and a young man. Through humorous and poignant moments, it captures the essence of youth, love, and the challenges of growing up.",
        "movie_date": "2021-11-26",
        "duration": "133 minutes"
    }
]


# Insert the movie records into the MongoDB collection
collection.insert_many(records)