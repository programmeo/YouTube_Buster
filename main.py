#Import Required Modual For Program
from pytube import YouTube, Playlist, Channel
from pytube.cli import on_progress

#App Banner String
app_banner = '''
******************************
******************************
**                          **
** Welcome To YoutubeBuster **
**                          **
******************************
******************************

@ Created By - Yash Vaghasiya
@ Date - 22 June, 2022
-------------------------------
'''
print(f'\033[1;32m{app_banner}')

#Print Option On Terminal
print('\033[1;33m1. Download Video\n2. Download PlayList\n3. Download Audio From Video\n4. Download Audios Of Playlist\n5. Download Video Without Audio\n6. Download All Videos From Channel\n')
user_in = input("\033[1;37mEnter Option 1/2/3/4/5/6 :- ")

url = input("\nEnter URL:- ")
if user_in=='1':
    #Make Object Of YouTube class
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f'\nVideo Title :- "{yt.title}"')
    print('-'*50)
    
    #Filter progressive stream video
    video_list = yt.streams.filter(progressive=True)

    #Show Quality Of Video For Download  
    print("What Type Qulity You Need\n")
    for i in video_list:
        quality = list(str(i).split(' '))
        print(f"Code {quality[1][5:]} = {quality[3][4:]}\n")
    
    #Finally Download The Video
    code = int(input("\033[0;36mEnter Code Number: "))
    print(f'\nFile Size:- {yt.streams.get_by_itag(code).filesize/(1024*1024)}')
    print("\n\033[1;37mStarts Downloading...")
    download_vid = yt.streams.get_by_itag(code)
    download_vid.download('Download/')

elif user_in=='2':
    #Make Object Of PlayList Class
    p = Playlist(url)

    #Download all Video One By One from playlist
    print(f'\033[1;37m\nPlayList Name : {p.title}')
    print('-'*50)
    for video in p.videos:
        print(f'\nDownloading : {video.title}')
        print(f'File Size:- {video.streams.get_highest_resolution().filesize/(1024*1024)}')
        video.streams.get_highest_resolution().download('Download/')

elif user_in=='3':
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f'\nVideo Title :- \n"{yt.title}"')
    print('-'*50)

    #Filter audio File
    audio_list = yt.streams.filter(only_audio=True)
    print("\nWhat Type Qulity You Need\n")
    for i in audio_list:
        quality = list(str(i).split(' '))
        print(f"Code {quality[1][5:]} = {quality[2][4:]}\n")
    
    #Download Only Audio From Video By iTag
    code = int(input("\033[0;36mEnter Code Number: "))
    print(f'\nFile Size:- {yt.streams.get_by_itag(code).filesize/(1024*1024)}')
    print("\n\033[1;37mStarts Downloading...")
    download_vid = yt.streams.get_by_itag(code)
    download_vid.download('Download/')

elif user_in=='4':
    #Make Playlist Object and Print Playlist Name On terminal
    p = Playlist(url)
    print(f'\033[1;37m\nPlayList Name :- {p.title}')
    print('-'*50)

    for i in p.video_urls:
        #Make Youtube object For Targetting Ech video Of playlist
        yt = YouTube(i, on_progress_callback=on_progress)
        print(f'\nDownloading - "{yt.title}"')

        #Download Audio File
        audio_list = yt.streams.filter(only_audio=True)
        code = 140
        print(f'\nFile Size:- {yt.streams.get_by_itag(code).filesize/(1024*1024)}')
        yt.streams.get_by_itag(code).download(f'Download/{p.title}')

elif user_in=='5':
    #Make Object Of YouTube class
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f'\nVideo Title :- \n"{yt.title}"')
    print('-'*50)

    #Filter progressive stream video
    video_list = yt.streams.filter(mime_type="video/mp4", adaptive=True)
    print("\nWhat Type Qulity You Need\n")
    for i in video_list:
        quality = list(str(i).split(' '))
        print(f"Code {quality[1][5:]} = {quality[3][4:]}\n")
    
    #Finally Download The Video
    code = int(input("\033[0;36mEnter Code Number: "))
    print("\n\033[1;37mStarts Downloading...")
    download_vid = yt.streams.get_by_itag(code)
    print(f'\nFile Size:- {yt.streams.get_by_itag(code).filesize/(1024*1024)}')
    download_vid.download('Download/')

elif user_in=='6':
    c = Channel(url)
    print(f'\033[1;37m\nChannel Name: {c.channel_name}')
    print('-'*50)
    for video in c.videos:
        print(f'\nDownloading {video.title}')
        print(f'\nFile Size:- {video.streams.get_highest_resolution().filesize/(1024*1024)}')
        video.streams.get_highest_resolution().download(f'Download/{c.channel_name}')

else:
    print("Please Enter Valid Option")

