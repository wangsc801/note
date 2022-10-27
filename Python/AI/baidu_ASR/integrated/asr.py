import json
import base64
import time
from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from sys import argv
from pathlib import Path
timer = time.perf_counter

# API_KEY = 'C6LCfz61gehseuEglItnb24C'
# SECRET_KEY = 'ncvYflFNkGbEwqizrxmmABFVgPddsfwH'
KEY_FILE_NAME='private_key.txt'
key_file_lines=open(KEY_FILE_NAME,'rt').readlines()

API_KEY = key_file_lines[0].strip()
SECRET_KEY = key_file_lines[1].strip()

CUID = '123456PYTHON'
RATE = 16000
DEV_PID = 1537  # 1537 表示识别普通话，使用输入法模型。根据文档填写PID，选择语言及识别模型
ASR_URL = 'http://vop.baidu.com/server_api'
SCOPE = 'audio_voice_assistant_get'  # 有此scope表示有asr能力，没有请在网页里勾选，非常旧的应用可能没有

class DemoError(Exception):
    pass

TOKEN_URL = 'http://aip.baidubce.com/oauth/2.0/token'

def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    post_data = post_data.encode( 'utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()
    result_str =  result_str.decode()

    #print(result_str)
    result = json.loads(result_str)
    #print(result)
    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if SCOPE and (not SCOPE in result['scope'].split(' ')):  # SCOPE = False 忽略检查
            raise DemoError('scope is not correct')
        print('SUCCESS WITH TOKEN: %s  EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
        return result['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

    
def audio_to_text(audio_file,result_dir):
    audio_file=Path(audio_file)
    format = audio_file.suffix[1:]

    speech_data = []
    with open(audio_file, 'rb') as speech_file:
        speech_data = speech_file.read()
    length = len(speech_data)
    if length == 0:
        raise DemoError('file %s length read 0 bytes' % audio_file)
    speech = base64.b64encode(speech_data)
    speech = str(speech, 'utf-8')
    params = {'dev_pid': DEV_PID,
              'format': format,
              'rate': RATE,
              'token': fetch_token(),
              'cuid': CUID,
              'channel': 1,
              'speech': speech,
              'len': length
              }
    post_data = json.dumps(params, sort_keys=False)
    req = Request(ASR_URL, post_data.encode('utf-8'))
    req.add_header('Content-Type', 'application/json')
    try:
        begin = timer()
        f = urlopen(req)
        result_str = f.read()
        print ("Request time cost %f" % (timer() - begin))
    except URLError as err:
        print('asr http response http code : ' + str(err.code))
        result_str = err.read()

    result_str = str(result_str, 'utf-8')
    print(f"【result】\n{result_str}")
    import os
    with open(f"{result_dir}{os.sep}{audio_file.stem}.txt","wt",encoding='gbk') as of:
        of.write(result_str)
    
# if __name__ == '__main__':
#     token = fetch_token()