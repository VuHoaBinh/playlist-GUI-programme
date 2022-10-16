import webbrowser

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



#### VIDEOS

def read_video():
    title = input("Enter title: ") + "\n"
    link = input("Enter link: ") + "\n"
    video = Video(title,link)    ### class
    return video

def print_video(video):
    print("Video title: ", video.title, end="")
    print("Video link: ", video.link, end="")

def read_videos():
    user = int(input("Enter how many videos: "))
    videos = []
    for i in range(user):
        print("Video: ", i+1)
        videos.append(read_video())
    return videos

def print_videos(videos):
    print("\n----")
    total = len(videos)
    for i in range(int(total)):
        print("Video " + str(i+1) + " :")
        print_video(videos[i])

def write_video_txt(video, file):
    file.write(video.title + "\n")
    file.write(video.link + "\n")

def write_videos_txt(videos,file):
    print("\n")
    total = len(videos)
    file.write(str(total) + "\n")
    for i in range(len(videos)):
        write_video_txt(videos[i],file)

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



###### PLAYLIST

def read_playlist():
    name = input("Enter playlist name: ") + '\n'
    description = input("Enter playlist description: ") + '\n'
    rating = int(input("Enter playlist rating(1-5): ") + '\n')
    video = read_videos()
    playlist = Playlist(name, description, rating, video) ### class PLaylist
    return playlist


def write_playlist_txt(playlist,file):
    with open("binh.txt", "w") as file:
        file.write(playlist.name + "\n")
        file.write(playlist.description + "\n")
        file.write(str(playlist.rating) + "\n")
        write_videos_txt(playlist.videos, file)
    print("Successfully write playlist to txt")


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


def print_playlist(playlist):
    print("============================================")
    print("\nPlaylist name: " + playlist.name, end = "")
    print("\nPlaylist description: " + playlist.description, end = "")
    print("\nPlaylist rating: " + str(playlist.rating), end = "")
    print_videos(playlist.videos)

def show_menu():
    print("-----------------------")
    print("Option 1: Create playlist")
    print("Option 2: Show playlist")
    print("Option 3: Play a video")
    print("Option 4: Add a video")
    print("Option 5: Update playlist")
    print("Option 6: Remove playlist")
    print("Option 7: Save and Exit")
    print("-----------------------")


def select_in_range(prompt, min, max):  # check value
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max :
        choice = input(prompt)

    choice = int(choice)    
    return choice

def play_video(playlist):
    print_videos(playlist.videos)
    choice = select_in_range("Select a video: ", 1, len(playlist.videos))
    print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end="")
    playlist.videos[choice-1].open()

def add_video(playlist):
    print("Enter new infornation video:")
    new_video_title = input("Enter video title: ") +"\n"
    new_video_link = input("Enter video link: ")+"\n"
    new_video = Video(new_video_title,new_video_link)
    playlist.videos.append(new_video)
    return playlist

def update_playlist(playlist):
    print("-- Update playlist --")
    print("1.Name")
    print("2.description")
    print("3.rating")
    choice = select_in_range("Enter what you want to update(1-3): ",1,3);
    if choice == 1:
        new_playlist_name = input("Enter new playlist name: ") + "\n"
        playlist.name = new_playlist_name
        print("Update Succesfully!!")
        return playlist
    elif choice == 1:
        new_playlist_description = input("Enter new playlist description: ")+ "\n"
        playlist.description = new_playlist_description
        print("Update Succesfully!!")
        return playlist
    else:
        new_playlist_rating = str(select_in_range("Enter new playlist rating(1-5): ",1,5))+ "\n"
        playlist.rating = new_playlist_rating
        print("Update Succesfully!!")
        return playlist

def remove_video(playlist):
    print_videos(playlist.videos)
    choice = select_in_range("Enter video you want to delete: ", 1, len(playlist.videos))
    del playlist.videos[choice-1]
    return playlist


def main(): 
    print("Welcom to programe music ");
    user_name=input("Your name: ");
    print("HELLO " + str(user_name));
    try:
        playlists = read_playlists_from_txt()
        playlist = playlists[0]
        print("Loaded data Succesfully!!")
    except:
        print("Welcom first user!!!")

    while True:
        show_menu();
        choice = select_in_range("Select an option (1-7): ", 1 ,7)
        if choice == 1:
            playlist = read_playlist()
            input("\nPress Enter to continue.\n")
        elif choice == 2:
            print_playlist(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 3:
            play_video(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 4:
            playlist = add_video(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 5:
            update_playlist(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 6:
            playlist = remove_video(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 7:
            write_playlist_txt(playlist)
            break
        else:
            print("exit!!!")
   

main()