import subprocess
import os

def make_vertical_video(voice_path, title, out_path):
    # Simple FFmpeg command: create video with static background and audio + title overlay
    # Note: in production replace 'background.jpg' with a packaged asset or generated frames.
    bg = 'ffmpeg_bg.jpg'
    if not os.path.exists(bg):
        # create a simple background using ffmpeg color if not exists
        subprocess.run(['ffmpeg','-f','lavfi','-i','color=c=white:s=1080x1920','-frames:v','1',bg], check=True)
    cmd = [
        'ffmpeg','-y',
        '-loop','1','-i',bg,
        '-i', voice_path,
        '-vf', f"scale=1080:1920,drawtext=text='{title}':fontcolor=black:fontsize=48:x=(w-text_w)/2:y=100",
        '-c:v','libx264','-t','30','-c:a','aac','-shortest', out_path
    ]
    subprocess.run(cmd, check=True)
    return out_path
