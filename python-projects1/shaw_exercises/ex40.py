class Song(object):
# lyrics = ""
    def __init__(self, lyrics): # dit heet de 'constructor'
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
    
happy_bday = Song(["\tHappy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there...",
                    "---------------------"])

# happy_birthday = ["lyrics"]
# text = Song(happy_birthday)

bulls_on_parade = Song(["\tThey rally around the family",
                        "With pockets full of shells",
                        "---------------------"])

horse_with_no_name = Song(["\tYou see I have been to the desert on a horse with no name",
                            "It felt good to be out of the rain",
                            "In the desert you can remember your name",
                            "'cause there ain't no one for to give you no pain...",
                            "---------------------"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

horse_with_no_name.sing_me_a_song()

# text.sing_me_a_song()