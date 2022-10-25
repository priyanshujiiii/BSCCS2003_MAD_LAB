import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column,Integer,String,ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import session
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autincrement=True, primary_key=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True)

class Article(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)

class ArticleAuthors(Base):
    __tablename__ = 'article_authors'
    user_id = Column(Integer, ForeignKey("user.user_id"),primary_key=True,nullable=False)
    article_id=Column(Integer,ForeignKey("article.article_id"),primary_key=True,nullable=False)

engine = create_engine("sqlite:///./testdb.sqlite3")

if __name__ == '__main__':
    stmt = select(User)
    print("____________QUERY____________")
    print(stmt)

    with engine.connect() as conn:
        print("____________RESULT____________")
        for row in conn.execute(stmt):
            print(row)
