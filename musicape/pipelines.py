# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, String, create_engine, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 数据库连接信息
db_host = '**'
db_user = '**'
db_pawd = '**'
db_name = '**'
db_port = 3306

# 创建对象的基类:
Base = declarative_base()


# 定义Channel对象:
class Music(Base):
    # 表名
    __tablename__ = 'music'
    # 表结构
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(1024))
    names = Column(String(1024))
    area = Column(String(128))
    form = Column(String(512))
    types = Column(String(128))
    length = Column(String(128))
    language = Column(String(128))
    data_time = Column(String(32))
    baidu_url = Column(String(512))
    baidu_se = Column(String(32))
    music_info = Column(Text)
    words = Column(String(128))
    music = Column(String(128))
    url = Column(String(64))


class MusicapePipeline(object):
    def __init__(self):
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def process_item(self, item, spider):
        # print(item["name"])
        info = Music(
            name=item["name"],
            names=item["names"],
            area=item["area"],
            form=item["form"],
            types=item["types"],
            length=item["length"],
            language=item["language"],
            data_time=item["data_time"],
            baidu_url=item["baidu_url"],
            baidu_se=item["baidu_se"],
            url=item["url"],
            words=item["words"],
            music_info=item["music_info"],
            music=item["music"],
        )
        self.session.add(info)
        self.session.commit()
        return item


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                           .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    Base.metadata.create_all(engine)

