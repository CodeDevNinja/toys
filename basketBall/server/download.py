import os,sys
sys.path.append('../')
from sqlUtil import sqlUtil
from models import Video
import json
from pathlib import Path

base_url ="mysql+mysqldb://root:password@127.0.0.1/dongdong"
def exec_sh(cmd):
    f = os.popen(cmd)
    return f.read()

def playlist(play_id):
    cmd = 'youtube-dl --flat-playlist --print-json \
    https://www.youtube.com/watch?list={}'.format(play_id)
    r = exec_sh(cmd)
    l = r.split('\n')
    datas = []
    for i in l:
        if i=='':
            continue
        data = json.loads(i)
        data.pop('_type')
        data['origin'] = data.pop('ie_key')
        data['play_id'] = play_id
        datas.append(Video(url=data['url'], 
                            play_id=data['play_id'], 
                            origin=data['origin'],title=data['title'],
                            description=data['description'],uploader=data['uploader']
                            ))
    sq = sqlUtil(base_url)
    sq.bulk_insert(datas)

def down_load_video(base_dir):
    sq = sqlUtil(base_url)
    rows = sq.query(Video,Video.download_url==None)
    for row in rows:
        Path("{}/{}/{}".format(base_dir, row.uploader, 
        row.play_id)).mkdir(parents=True, exist_ok=True)
        cmd = 'youtube-dl -o "{}/{}/{}/%(title)s.%(ext)s" \
        https://www.youtube.com/watch?v={}'.format(base_dir, row.uploader, 
        row.play_id,row.url)
        # f = os.popen(cmd)
        os.system(cmd)
        # print(f.read())
        location = '{}/{}/{}/{}.{}'.format(base_dir, row.uploader, 
        row.play_id,row.title,'mp4')
        sq.update(Video, Video.url==row.url, {"location":location})

if __name__ == '__main__':
    # playlist('PLvn6tsSyFhW3C3bnrdHsdStBKQp0pK7dd')
    down_load_video('.')