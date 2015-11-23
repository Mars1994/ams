#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import exists
from settings import AMS_DB_SETTINGS


__author__ = 'chengrui'


engine = create_engine(AMS_DB_SETTINGS)
DB_Session = sessionmaker(bind=engine)
Base = declarative_base()


class Article(Base):
    '''ORM for artile table'''

    __tablename__ = 'article'

    article_id = Column(Integer, primary_key=True)
    article_title = Column(String)
    article_author = Column(String)
    article_content = Column(String)

    def __init__(self, article_title, article_author, article_content):
        '''Construct the object of Article class'''

        self.article_title = article_title
        self.article_author = article_author
        self.article_content = article_content

    @classmethod
    def insert_article(cls, article_name, article_author, article_content, tag_ids):
        '''Insert the article to the DB

        :exception: error: cannot add the article to the DB
        :return: Return the status of inserting the article to the DB
        '''

        session = DB_Session()
        status = 0
        try:
            article = cls(article_name, article_author, article_content)
            session.add(article)
            session.commit()
            for tag_id in tag_ids:
                tag_article = TagArticle(tag_id, article.article_id)
                session.add(tag_article)
            session.commit()
        except:
            session.rollback()
            status = -1
            raise
        finally:
            session.close()
        return status

    @classmethod
    def delete_article(cls, article_id):
        # this method is deleting by id, deleting by article_title also work, but it is not the same
        '''Delete the article from the DB

        :exception: error: cannot delete the article from the DB
        :return: return the status of deleting the article from the DB
        '''

        session = DB_Session()
        status = 0
        try:
            session.query(Article).filter(Article.article_id == article_id).delete()  # 可能有错误
            session.commit()
        except:
            session.rollback()
            status = -1
            raise
        finally:
            session.close()
        return status

    @classmethod
    def modify_article(cls, article_id, article_title, article_author, article_content, tag_ids):
        '''modify the article in the DB

        :param: article: the new article used to replace the article but it's id
        :param: tags: the tags to be modified of the article
        :exception: error: cannot modify the article in the DB
        :return: return the status of modify the article in the DB
        '''

        session = DB_Session()
        status = 0
        try:
            session.query(Article).filter(Article.article_id == article_id).update(
            {
                Article.article_title: article_title,
                Article.article_author: article_author,
                Article.article_content: article_content
            })

            # Modify tags of the article
            # firstly, drop the association between the article and tags
            session.query(TagArticle).filter(Article.article_id == article_id).delete()
            # then, construct new association between the articles and new tags
            for tag_id in tag_ids:
                tag_article = TagArticle(tag_id, article_id)
                session.add(tag_article)
            session.commit()
        except:
            session.rollback()
            status = -1
            raise
        finally:
            session.close()
        return status

    @classmethod
    def read_article(cls, article_id):
        # this method is reading by id, reading by article_title also work, but it is not the same
        '''read the article from the DB

        :exception: error: cannot read the article from the DB
        :return: return the status of read the article from the DB
        '''

        session = DB_Session()
        status = 0
        try:
            # article = cls()
            article = session.query(Article).filter(Article.article_id == article_id).first()
            if (article):
                print('Title: ' + article.article_title)
                print('Author: ' + article.article_author)
                print('Content: ' + article.article_content)
                # print tags
            else:
                print('Not exist')
            session.commit()
        except:
            session.rollback()
            status = -1
            raise
        finally:
            session.close()
        return status


class Tag(Base):
    '''ORM for Tag'''

    __tablename__ = 'tag'

    tag_id = Column(Integer, primary_key=True)
    tag_name = Column(String)
    tag_use_count = Column(Integer)

    def __init__(self, tag_name):
        '''Construct the object of Tag class'''
        self.tag_name = tag_name
        self.tag_use_count = 0

    @classmethod
    def insert_tag(cls, tag_name):
        '''Insert the tag to the DB

        :exception: error: cannot add the tag to the DB
        :return: Return the tag_id of inserting the tag to the DB
        '''

        session = DB_Session()
        try:
            tag = session.query(Tag).filter(Tag.tag_name == tag_name).first()
            if tag:
                rtn_tag_id = tag.tag_id
            else:
                tag = cls(tag_name)
                session.add(tag)
                session.commit()
                rtn_tag_id = tag.tag_id
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return rtn_tag_id


class TagArticle(Base):
    '''ORM for Tag'''

    __tablename__ = 'tag_article'

    associate_id = Column(Integer, primary_key=True)
    tag_id = Column(Integer)
    article_id = Column(Integer)

    def __init__(self, tag_id, article_id):
        '''Construct the object of TagArticle class'''

        self.tag_id = tag_id
        self.article_id = article_id






