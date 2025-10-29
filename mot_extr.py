from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.video.fx.all import invert_colors, blackwhite
import os

filename = input("Please enter the filename (with extension): ")

current_dir = os.path.dirname(os.path.abspath(__file__))
background_path = os.path.join(current_dir, filename)
overlay_path = os.path.join(current_dir, filename)
output_path = os.path.join(current_dir, "out_" + filename)
if os.path.exists(output_path):
    os.remove(output_path)

background = VideoFileClip(background_path)
overlay = VideoFileClip(overlay_path)
overlay = overlay.set_opacity(0.49)
overlay = overlay.fx(invert_colors)
overlay = overlay.set_start(4/overlay.fps)
overlay = overlay.without_audio()
background = background.fx(blackwhite)
overlay = overlay.fx(blackwhite)
final = CompositeVideoClip([background, overlay])

final.write_videofile(output_path)

# Addition for difference from main
