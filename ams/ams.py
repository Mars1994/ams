#!/usr/bin/env python
# -*- coding: utf-8 -*-


import models

__author__ = 'chengrui'


def article_insert(article_title, article_author, article_content, tag_names):
    '''Insert the articl'''

    tag_ids = []
    for tag_name in tag_names.split(','):
        tag_ids.append(tag_insert(tag_name))
    if tag_ids:
        if models.Article.insert_article(article_title, article_author, article_content, tag_ids):
            print('Insert article successfully')
    else:
        print('Insert article error')


def article_delete(article_id):
    '''Delete the articl'''

    if models.Article.delete_article(article_id):
        print ('Delete successfully')
    else:
        print ('Already Deleted')


def article_modify(article_id, article_title, article_author, article_content, tag_names):
    '''Modify the articl'''

    if article_read(article_id):
        tag_ids = []
        for tag_name in tag_names.split(','):
            tag_ids.append(tag_insert(tag_name))
        return models.Article.modify_article(article_id, article_title, article_author, article_content, tag_names)


def article_read(article_id):
    '''Read the articl'''

    models.Article.read_article(article_id)


def tag_insert(tag_name):
    return models.Tag.insert_tag(tag_name)

