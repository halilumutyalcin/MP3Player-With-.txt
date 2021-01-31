######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

from random import choice

class MP3Player:
    def __init__(self,songlist = []):
        self.nowPlayingSong = " "
        self.vol = 100
        self.songlist = songlist
        self.status = True

    def chooseSong(self):
        count = 1
        for sarki in self.songlist:
            print("{}){}".format(count, sarki))
            count += 1

        selectedSong = int(input("Enter the number of the song you want to play:"))

        while selectedSong < 1 or selectedSong > len(self.songlist):
            selectedSong = int(
                input("Enter the correct number of the song you want to select [1- {}]: ".format(len(self.songlist))))

        self.nowPlayingSong = self.songlist[selectedSong - 1]

    def volumaUp(self):
        if self.vol == 100:
            pass
        else:
            self.vol += 10

    def volumeDown(self):
        if self.vol == 0:
            pass
        else:
            self.vol -= 10

    def randomSong(self):
        rs = choice(self.songlist)
        self.nowPlayingSong = rs

    def addSong(self):
        artist = input("Enter the Artist / Group:")
        song = input("Enter the song:")

        self.songlist.append(artist + " - " + song)

    def removeSong(self):
        count = 1
        for song in self.songlist:
            print("{}) {}".format(count, song))
            count += 1

        beDeletedSong = int(input("Enter the number of the song you want to delete:"))

        while beDeletedSong < 1 or beDeletedSong > len(self.songlist):
            beDeletedSong = int(
                input("Enter the correct number of the song you want to delete [1- {}]:".format(len(self.songlist))))

        self.songlist.pop(beDeletedSong - 1)

    def close(self):
        self.status = False

    def show(self):
        print("""
* ---> Welcome to MP3 Player <--- *

Song list : {}
Now Playing Song: {}
Volume: {}

1) Select song.
2) Increase sound.
3) Volume down.
4) Pick a random song.
5) Add songs.
6) Delete song.
7) Close. 
                """.format(self.songlist, self.nowPlayingSong, self.vol))

    def selection(self):
        selection = int(input("Enter your choice:"))

        while selection < 1 or selection > 7:
            selection = int(input("Please enter selections within the specified ranges [1-7]: "))

        return selection

    def run(self):
        self.show()
        selection = self.selection()

        if selection == 1:
            self.chooseSong()
        if selection == 2:
            self.volumaUp()
        if selection == 3:
            self.volumeDown()
        if selection == 4:
            self.randomSong()
        if selection == 5:
            self.addSong()
        if selection == 6:
            self.removeSong()
        if selection == 7:
            self.close()

mp3 = MP3Player()
while mp3.status:
    mp3.run()

print("The program is over. Goodbye.")