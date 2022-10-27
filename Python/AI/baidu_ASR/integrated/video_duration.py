import subprocess
from pathlib import Path


def get_video_duration(video_path):
    path = Path(video_path)
    cmd = f"ffprobe -i {path} -show_entries format=duration -v quiet"
    print(f"\n---------\n{cmd}\n----\n----------\n")
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    # duration=xxx
    print(f"\n\n============\n{output.decode(encoding='utf-8')}\n=======\n==============")
    duration_str = output.decode(encoding='utf-8').split('\n')[1].strip()
    return float(duration_str.split('=')[1])

# def ffmpeg_lib_video_duration(video_path):
#     # pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple ffmpeg-python
#     probe = ffmpeg.probe(video_path)
#     duration = probe['format']['duration']
#     return duration
    
def format(totoal_seconds):
    hours=int(totoal_seconds/(60*60))
    minutes=int(totoal_seconds/60)
    seconds=int(totoal_seconds%60)
    return f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

def ffmpeg_format_time(duration,segment_duration:int):
    duration = int(duration)
    segment_duration_len = int(duration/segment_duration)
    tail_seconds = duration % segment_duration
    times=[]
    for i in range(0,segment_duration_len):
        times.append(format(segment_duration*i))
        times.append(format(segment_duration*(i+1)))
    if tail_seconds!=0:
        last_minute=times[-1]
        times.append(last_minute)
        last=format(duration)
        times.append(last)
    return times

li=ffmpeg_format_time(180,59)
print(li)
