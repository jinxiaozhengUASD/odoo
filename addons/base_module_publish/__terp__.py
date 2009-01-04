# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution	
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name" : "Module publisher",
    "version" : "1.0",
    "author" : "Tiny",
    "website" : "http://www.openerp.com",
    "category" : "Generic Modules/Base",
    "description": """
This module can be used by developpers to automatically publish their modules
in a few click to the following websites:
* http://OpenERP.com, section module
* http://TinyForge.org
* PyPi, The python offical repository
* http://Freshmeat.net

It adds a button "Publish module" on each module, so that you simply have
to call this button when you want to release a new version of your module.
    """,
    "depends" : ["base"],
    "init_xml" : [ ],
    "demo_xml" : [ ],
    "update_xml" : [ "base_module_publish_wizard.xml" ],
    "installable": True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

