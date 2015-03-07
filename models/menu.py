# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('IIITS E-Library'),XML('&trade;&nbsp;'),
                  _class="brand",_href="http://www.iiits.ac.in")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Admin Login'), False, URL('default', 'manage')),
    (T('Student Login'), False, URL('default', 'manage')),
    (T('Search By Book Id/Book Name/Author Name'),False, URL('default', 'mean')),
]
if auth.has_membership('managers'):
    response.menu.remove((T('Admin Login'), False, URL('default', 'manage')))
    response.menu.remove((T('Student Login'), False, URL('default', 'manage')))
    response.menu.append((T('Update Book Store'), False, URL('default', 'manage')))
    response.menu.append((T('Update Student Info'), False, URL('default', 'manage1')))
    response.menu.remove((T('Search By Book Id/Book Name/Author Name'), False, URL('default', 'mean')))
   
if auth.has_membership('user'):
    response.menu.remove((T('Admin Login'), False, URL('default', 'manage')))
    response.menu.remove((T('Student Login'), False, URL('default', 'manage')))
    response.menu.append((T('Retrieve Information'), False, URL('default', 'show1')))
    response.menu.remove((T('Search By Book Id/Book Name/Author Name'), False, URL('default', 'mean')))


if "auth" in locals(): auth.wikimenu()
