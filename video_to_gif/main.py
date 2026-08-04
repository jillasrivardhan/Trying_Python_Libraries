from moviepy.editor import VideoFileClip

clip = VideoFileClip("video-1.mp4")
clip.write_gif("output.gif")