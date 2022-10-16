import pygame
from random import randint
import webbrowser


class TextButton:
    def __init__(self,text,position):
        self.text = text 
        self.position = position
    def is_mouse_on_text(self):
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if (self.position[0] < mouse_x < (self.position[0]+ self.text_box[2])) and (self.position[1] < mouse_y < (self.position[1] + self.text_box[3])):
            return True
        return False
       
    def draw(self):
        font = pygame.font.SysFont('sans',30)
        text_render = font.render(self.text, True, (0,0,255))
        self.text_box = text_render.get_rect() # rect around text

        if self.is_mouse_on_text() == True:
            text_render = font.render(self.text, True, (0,0,255))
            pygame.draw.line(screen,(0,0,255),(self.position[0], self.position[1]+ self.text_box[3]),(self.position[0] + self.text_box[2], self.position[1]+self.text_box[3]))
        else:
            text_render = font.render(self.text, True, (0,0,0))

        screen.blit(text_render,self.position)# append text square rect


#############################################################
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False
    def open(self):
        webbrowser.open(self.link)
        self.seen = True


class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

## video
def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

def read_videos_from_txt(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        video = read_video_from_txt(file)
        videos.append(video)
    return videos

## playlist
def read_playlist_from_txt(file):
    playlist_name = file.readline()
    playlist_description = file.readline()
    playlist_rating  = file.readline()
    playlist_videos = read_videos_from_txt(file) #### Note: error
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos) ### class Playlist
    return playlist

def read_playlists_from_txt():
    playlists = []
    with open("binh.txt","r") as file:
        total = file.readline()
        for i in range(int(total)):
            playlist = read_playlist_from_txt(file)
            playlists.append(playlist)
    return playlists


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("XXX")
running = True
GREEN = (0,200,0)
RED = (255,0,0)
WHILE = (255,255,255)
BLUE = (0,0,255)
BLACK = (0,0,0)
clock = pygame.time.Clock()

playlists = read_playlists_from_txt()
videos_btn_list = []
playlists_btn_list = []
margin = 50
for i in range(len(playlists)):
    playlist_btn = TextButton(playlists[i].name.rstrip(), (50,50+margin*i))
    playlists_btn_list.append(playlist_btn)

playlist_choice = None


while running:
    clock.tick(60)
    screen.fill(WHILE)

    for playlist_button in playlists_btn_list:
        playlist_button.draw()

    for video_button in videos_btn_list:
        video_button.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                                                                               
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 or event.button == 3:
                for x in range(len(playlists_btn_list)):
                    if playlists_btn_list[x].is_mouse_on_text():
                        playlist = playlists[x]
                        playlist_choice = x
                        videos_btn_list = []
                        for i in range(len(playlist.videos)):
                            video_btn = TextButton(str(i+1) + ". " + playlist.videos[i].title.rstrip(), (250,50+margin*i))
                            videos_btn_list.append(video_btn)
                if playlist_choice != None:
                    for i in range(len(videos_btn_list)):
                        if videos_btn_list[i].is_mouse_on_text():
                             playlist.videos[i].open()
        


    pygame.display.flip()

pygame.quit()

