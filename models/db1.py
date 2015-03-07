# -*- coding: utf-8 -*-
db.define_table('Book_List',
                Field('Book_Id','integer'),
                Field('Book_Name','string'),
                Field('Availability','string'),
                Field('Author_Name','string'),
                Field('Publication_Date','date'))
                #Field('Section','string'))
db.define_table('Issue_table',
                Field('Book_Id','integer'),
                Field('Book_Name','string'),
                Field('Book_Issued_To','string'),
                Field('E_Mail','string'),
                Field('Phone_No','integer'),
                Field('Issue_Date','datetime'),
                Field('Due_Date','datetime'),
                Field('Fines_Due','integer'))
