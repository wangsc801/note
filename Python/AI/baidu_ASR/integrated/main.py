from video_cut import video_cut
from asr import audio_to_text
from sys import argv
from pathlib import Path
import shutil

def recreate_dir(dir_name):
    dir=Path(dir_name)
    if dir.exists():
        shutil.rmtree(dir)
    Path.mkdir(dir)

if __name__ == '__main__':
    video_path=argv[1]
    audio_dir=argv[2]
    result_dir=argv[3]
    recreate_dir(audio_dir)
    recreate_dir(result_dir)
    summary_filename='summary.txt'
    import os 
    os.remove(summary_filename)

    video_cut(video_path,audio_dir)
    for item in Path(audio_dir).iterdir():
        audio_to_text(item,result_dir)
    # read json result then write result to a text file
    result_dir=Path(result_dir)
    summary=open(summary_filename,'wt')
    for json_reuslt in Path(result_dir).iterdir():
        import json
        with open(json_reuslt,'rt') as f:
            json_object=json.loads(f.read())
            summary.write(json_object['result'][0])

