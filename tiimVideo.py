from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

vid=VideoFileClip('video1.mp4')

def cropVideo(source,destination,start_time,end_time,metadata):
  ffmpeg_extract_subclip(source, start_time, end_time, targetname=destination)

source="video1.mp4"
destination="test_result2.mp4"
# start_time=float(input('Enter start time'))*60
# end_time=float(input('Enter end time'))*60
start_time=1 #min
end_time=1.1  #min
metadata=0

cropVideo(source,destination,start_time,end_time,metadata)
