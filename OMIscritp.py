#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import argparse

#URL = "localhost:8069"  # localhost address : odoo port
#DB = "script"
#USERNAME = "admin"
#PASSWORD = "admin"

COMMONPATH = 'xmlrpc/2/common'
OBJECTPATH = 'xmlrpc/2/object'

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--user",
					metavar = 'user',
					help = "The username",
					default = 'admin',)

parser.add_argument("-p", "--password",
					metavar = 'password',
					help = 'The password',
					default = 'admin',)

parser.add_argument('-i', '--instance_url',
					metavar = 'url',
					help = '''This is the instance url/ip.
					\nExample: odoo.com | 10.209.1.44''',
					default = 'localhost',)

parser.add_argument('--port',
					metavar = 'port_number',
					help = 'Port for the connection \
					Example: [host]:[port] | localhost:8069',
					default = '8069')

parser.add_argument('--database',
					metavar = 'database',
					help = 'Database name',
					required = True)

parser.add_argument("-m", "--module",
					metavar = 'module',
					help = 'Uninstall the indicated modules\
					| Pass it as a list: «example1 example2 example3»\
					| None comma is needed',
					type = str,
					nargs = '+',
					default = None)

args = vars(parser.parse_args())
print args

URL = args['instance_url']
DB = args['database']
USERNAME = args['user']
PASSWORD = args['password']
PORT = args['port']
MODULES = args['module']


connection = xmlrpclib.ServerProxy('http://{0}:{1}/{2}'.format(URL, PORT,
																COMMONPATH))
uid = connection.login(DB, USERNAME, PASSWORD)
connection = xmlrpclib.ServerProxy('http://{0}:{1}/{2}'.format(URL, PORT,
																OBJECTPATH))
print connection


print connection.execute_kw(DB, uid, PASSWORD, 'ir.module.module', 'search',
								[('name', '=', MODULES[0])])


#module_id = [connection.execute_kw(DB, uid, PASSWORD, 'ir.module.module',
#									'search',[('name', '=', MODULE)]) for MODULE
#			in MODULES] 
#module_id = connection.execute_kw(DB, uid, PASSWORD, 'ir.module.module', 'search',
#								[('name', '=', MODULES)])
print module_id, "<<"

#install = connection.execute_kw(DB, uid, PASSWORD, "ir.module.module",
#							"button_immediate_install", MODULES)
#print install














"""
connection = xmlrpclib.Serverproxy("http://{0}:{1}/{2}".format(URL, PORT,
																COMMONPATH))
uid = connection.login(DB, USERNAME, PASSWORD,)
common = xmlrpclib.ServerProxy("http://{}/xmlrpc/2/object".format(URL))
mod_id = common.execute(DB, uid, PASSWORD, 'ir.module.module', 'search',
						[('name', '=', 'calendar')])
common.execute_kw(DB, uid, PASSWORD, "ir.module.module",
					"button_immediate_install", mod_id)


#uid = common.login(DB, USERNAME, PASSWORD)
#version_mesg = common.version()

#print version_mesg
#help = common.__doc__()
#print help
# X.....................DatabaseName - UserID - UserPassword - ModelName          -  MethodName              -  [Parameters]
#install = common.execute_kw(DB,             uid,   PASSWORD,      "ir.module.module", "button_inmediate_install", ["stock"])
#some = common.execute_kw(DB, uid, PASSWORD, "sale.order", "onchange_partner_id", [[], [1]])
#print some
#install = common.execute_kw(DB, uid, ["stock"])
#uid = 1
#print install
"""