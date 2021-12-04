from sqlUtil import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date, DateTime, Time, Text

class Video(Base):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    origin = Column(String(255)) #来源 youtube
    title = Column(Text)
    description = Column(Text)
    uploader = Column(String(255))
    view_count = Column(Integer())
    like_count = Column(Integer())
    dislike = Column(Integer())
    duration = Column(Integer())
    download_url = Column(String(255))  #下载之后的地址
    video_size = Column(Integer()) #视频大小
    location = Column(String(255)) 
    play_id = Column(String(255)) 
    video_type = Column(String(255)) 