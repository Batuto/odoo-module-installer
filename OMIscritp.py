#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import argparse

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
module_id = connection.execute(DB, uid, PASSWORD, 'ir.module.module', 'search',
                               [('name', '=', MODULES)])
install = connection.execute(DB, uid, PASSWORD, "ir.module.module",
                                "button_immediate_install", module_id)

#module_id = [connection.execute_kw(DB, uid, PASSWORD, 'ir.module.module',
#                                   'search',[('name', '=', MODULE)]) for MODULE
#           in MODULES] 
#module_id = connection.execute_kw(DB, uid, PASSWORD, 'ir.module.module', 'search',
#                               [('name', '=', MODULES)])
#print module_id, "<<"

#install = connection.execute_kw(DB, uid, PASSWORD, "ir.module.module",
#                           "button_immediate_install", MODULES)
#print install

