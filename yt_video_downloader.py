from pytube import YouTube
# from sys import argv

# To execute in the CLI you need to manually write 'python filename "YouTube video URL"' and for Linux and OSX write 'python3 filename "YouTube video URL"' . YT video URL should be inside double quotes.
link_of_vid = input("Enter the URL of the Video you want to download: ")
# argv takes the user input.we can't use argv[1] because the first element is the name of the program name.
yt = YouTube(link_of_vid)
# This will create he youtube object from the link that user inputted.

print("Title of the linked video is: ", yt.title)
# prints out the title of the video from the link that the user inputted.
print("views of the linked video is: ", yt.views)
# prints out the views of the video from the link that the user inputted.

yt_video_res_list = yt.streams.all()
# gets all possible resolution avialable on YT for the linked video in the 'yt_video_res_list' List.

# enumerate_vid_list = list(enumerate(yt_video_res_list))
# enumerate gives the list number along with the list element.
# enumerate_vid_list = list(yt_video_res_list)
for i in range(len(yt_video_res_list)):
    print(f"{i+1}. ", end="")
    print(yt_video_res_list[i])
print()

while True:
    user_wanted_quality = int(input(
        "Enter the list number of which of the above resolution you want download the video: "))

    if user_wanted_quality > len(yt_video_res_list) or user_wanted_quality < 1:
        print("Please select a valid number.")
        continue
    else:
        break

yt_video_res_list[user_wanted_quality-1].download()
# Downloads the video to the path specified.If no path is specified then the video will be downloaded in the folder in which this code is located.

print("Video Downloaded. Thanks for using this script.")
