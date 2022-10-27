import subprocess
from pathlib import Path
from video_duration import get_video_duration
from video_duration import ffmpeg_format_time


def get_number_digits(number):
    digits = 0
    while number != 0:
        number = int(number/10)
        digits = digits+1
    return digits

#video_path = 'E:\\bilibili\\五四运动打断了宝贵的文化启蒙？这个荒谬的观点来自胡适【大师计划·傅正01】\\64-傅正01·新文化运动和五四运动.mp4'

def video_cut(video_path,audio_dir):
    video_duration = get_video_duration(video_path)
    time_list=ffmpeg_format_time(video_duration,59)
    digits=get_number_digits(video_duration/60)
    # execute ffmpeg commands
    for i in range(0,len(time_list),2):
        cmd=f'ffmpeg -ss {time_list[i]} -to {time_list[i+1]} -i {Path(video_path)} -c:a pcm_s16le -ar 16000 -ac 1 -vn -f wav {Path(audio_dir)}/{str(int((i+2)/2)).zfill(digits)}.wav'
        print(subprocess.run(cmd,shell=True))
