class Song(object):
    def __init__(self, lyrics):
        # print(">>>> enter __init__ ", lyrics )
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(['Happy birthday to you', 
                    "I don't want get sued",
                    "So I'll stop right there" ])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

gently_down_the_stream = Song(["Row row row a boat",
                                "gently down the stream"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
gently_down_the_stream.sing_me_a_song()