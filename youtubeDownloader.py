from pytube import YouTube

# This is a main function
def youtubeDownload(downloadURL, saveLocation):
        try:
            yt_obj = YouTube(downloadURL)
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download(output_path=saveLocation)
            print("Youtube Video Downloaded")
            return True
        except Exception as e:
            print(e)