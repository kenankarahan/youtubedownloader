# Kullanacağımız kütüphaneleri dahil ediyoruz. / Importing libraries we'll use.
from pytubefix import YouTube, Playlist
from pytubefix.exceptions import VideoUnavailable, VideoRegionBlocked, VideoPrivate
from pytubefix.cli import on_progress
from termcolor import colored

# Kullanıcıdan indirmek istediği içeriğin tipini alıyoruz. / Learning which type of content user wanted to download. 
try:
    yorp = int(input(colored("""
                             
Youtube Video Downloader
-------------------------

    Video (1)
    Playlist (2)
    MP3 (3)
        
        
Select the content you want to download: """, "green")))
except ValueError:
    print(colored("Please select one of the given options!","yellow")) 

if yorp == 1:

    # Kullanıcıdan indirmek istenilen içeriğin URL'sini input olarak alıyoruz. Ardından hata durumunda dönebilecek sonuçlara exception ekliyoruz. / Getting content's url and adding exceptions.
    try:
        url = input(colored("\n\n\nURL: ", "green"))
    except VideoUnavailable:
        print(colored("Content is unavailable.", "yellow"))
    except VideoRegionBlocked:
        print(colored("Content is region blocked.", "yellow"))
    except VideoPrivate:
        print(colored("Content is private.", "yellow"))

    # Kullanıcıdan URL'sini aldığımız videoyu Youtube nesnemize parametre olarak gönderip en yüksek çözünürlüğü almasını belirttikten sonra programımızın bulunduğu dizine indirme işlemimizi gerçekleştiriyoruz. / Adding url which user gave us into a Youtube object as a parameter and downloading the content into our directory.
    video = YouTube(url).streams.get_highest_resolution().download()
    print(colored("Please select one of the given options above!","yellow"))
elif yorp == 2:
    
    try:
        url = input(colored("\n\n\nURL: ", "green"))
    except VideoUnavailable:
        print(colored("Content is unavailable.", "yellow"))
    except VideoRegionBlocked:
        print(colored("Content is region blocked.", "yellow"))
    except VideoPrivate:
        print(colored("Content is private.", "yellow"))
    
    # Kullanıcıdan URL'sini aldığımız playlisti Playlist nesnemize parametre olarak gönderip videoları en yüksek çözünürlükte olacak şekilde programımızın bulunduğu dizinde playlistin adında bir klasör oluşturarak videolarımızı klasörün içine indirmeye işlemimizi gerçekleştiriyoruz. / Adding url which user gave us into a Youtube object as a parameter and downloading the content into directory which has playlist's title in our directory.
    play = Playlist(url)
    title = play.title
    for video in play.videos:
        video.streams.get_highest_resolution().download(output_path=title)
        print(colored("İndirme işlemi başarıyla tamamlanmıştır.", "green"))
elif yorp == 3:
    try:
        url = input(colored("\n\n\nURL: ", "green"))
    except VideoUnavailable:
        print(colored("Content is unavailable.", "yellow"))
    except VideoRegionBlocked:
        print(colored("Content is region blocked.", "yellow"))
    except VideoPrivate:
        print(colored("Content is private.", "yellow"))
    
    # Kullanıcıdan URL'sini aldığımız içeriği Youtube nesnemize parametre olarak gönderip sadece sesini almak istediğimizi ve içeriğinin uzantısının mp3 olacağını belirterek programımızın bulunduğu dizinde bir audios klasörü oluşturarak içeriğimizi audios klasörünün içine indirmeye işlemimizi gerçekleştiriyoruz. / Adding url which user gave us into a Youtube object as a parameter and downloading the content into directory which is "audios" in our directory.
    mp3 = YouTube(url).streams.get_audio_only().download(mp3=True, output_path="audios")
else:
    print(colored("Please select one of the given options above!","yellow"))