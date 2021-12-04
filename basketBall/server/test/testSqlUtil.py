import sys
sys.path.append('../')
from sqlUtil import sqlUtil
from models import Video

def test_bulk_insert():
    sq.bulk_insert([Video()])

if __name__ == '__main__':
    sq = sqlUtil("mysql+mysqldb://root:password@127.0.0.1/dongdong")
    print(sq.query(Video,Video.download_url==None))