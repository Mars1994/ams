#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ams import ams


__author__ = 'chengrui'


while (True):
    print('+++++---------------------------++++')
    print('+++++ The Article Manage System ++++')
    print('+++++ 1.Insert Articles         ++++')
    print('+++++ 2.Delete Articles         ++++')
    print('+++++ 3.Modify Articles Info    ++++')
    print('+++++ 4.Query Articles Info     ++++')
    print('+++++ 5.Quit the ams            ++++')
    print('+++++---------------------------++++')
    opt = raw_input('Choose the opt: ')
    if opt == '1':
        article_title = raw_input('Title    : ')
        article_author = raw_input('Author   : ')
        article_content = raw_input('Content  : ')
        tag_names = raw_input('New Tags  :')
        ams.article_insert(article_title, article_author, article_content, tag_names)
    elif opt == '2':
        article_id = raw_input('The id of the article you want to delete: ')
        ams.article_delete(article_id)
    elif opt == '3':
        article_id = raw_input('The id of the article you want to modify: ')
        ams.article_read(article_id)
        article_title = raw_input('New Title    : ')
        article_author = raw_input('New Author   : ')
        article_content = raw_input('New Content  : ')
        tag_names = raw_input('New Tags  :')
        ams.article_modify(article_id, article_title, article_author, article_content, tag_names)
    elif opt == '4':
        article_id = raw_input('ArtilceId: ')
        ams.article_read(article_id)
        pass
    elif opt == '5':
        quit()
    else:
        print('error opt')

