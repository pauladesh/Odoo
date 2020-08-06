# -*- coding: utf-8 -*-
{
	'name': 'School',
	'version': '12.0.1.0.0',
	'summary': 'Record Student Information',
	'category': 'Tools',
	'author': 'Adesh Paul',
	'website': 'https://www.google.com',
	'depends': ['base'],
	'data': [
		'security/ir.model.access.csv',
	    'views/student_view.xml',
		'views/class_view.xml',
		'views/subject_view.xml',
		'views/library_view.xml',
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}