from pytube import YouTube

link_of_vid = input("Enter the URL of the Video you want to download: ")

yt = YouTube(link_of_vid)

print("Title of the linked video is: ", yt.title)
print("views of the linked video is: ", yt.views)

yt_video_res_list = yt.streams.all()

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

print("Video Downloaded. Thanks for using this script.")
