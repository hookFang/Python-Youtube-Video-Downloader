from pytube import YouTube
import sys

arguments = len(sys.argv) - 1

# This is a main function
def youtubeDownload():
    if(arguments == 0):
        print("Please provide link to youtube video as an argument. More info --help me")
    else:
        try:
            youtube_video_url = sys.argv[1]
            yt_obj = YouTube(youtube_video_url)
            yt_obj.register_on_progress_callback(show_progress_bar)
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download(output_path='C:/Users/edwin/Downloads', filename='yt_video.mp4')
            print("Youtube Video Downloaded")
        except Exception as e:
            print(e)

def percent(self, tem, total):
    perc = (float(tem) / float(total)) * float(100)
    return perc

def show_progress_bar(stream, chunk, file_handle, bytes_remaining):
    size = video.filesize
    p = 0
    while p <= 100:
        progress = p
        print(str(p)+'%')
        p = percent(bytes_remaining, size)


youtubeDownload()