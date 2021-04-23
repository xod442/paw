
'''
 2016 wookieware..
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "1.0.0"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Prototype"

Manages strain strain database
'''
from flask import Blueprint, render_template, request, redirect, session, url_for, abort, flash


strains_app = Blueprint('strains_app', __name__)

@strains_app.route('/strainnew', methods=('GET', 'POST'))
def strainnew():
    '''
    Adds a new strain strain to the strain database
    Reads form variables, creates a strain variable and
    saves it to the mongo database.
    '''

    return render_template('strain/newstrain.html', form=form)

@strains_app.route('/strainlist', methods=('GET', 'POST'))
def strainlist():
    '''
    Lists all the strain strains in the database
    '''

    return render_template('strain/strainlist.html', strain=strain)

@strains_app.route('/strainedit', methods=('GET', 'POST'))
def strainedit():
    '''
    Get selected strain from database and fill out edit form
    '''

    return render_template('strain/straineditselect.html', strain=strain)


@strains_app.route('/straindelete', methods=('GET', 'POST'))
def straindelete():
    '''
    Get selected strain strain from database and delete it
    '''

    return render_template('strain/straineditdelete.html', strain=strain)

@strains_app.route('/straincopy', methods=('GET', 'POST'))
def straincopy():
    '''
    Copy a strain
    '''

    return render_template('strain/straindbdrop.html')

@strains_app.route('/strainbulk', methods=('GET', 'POST'))
def strainbulk():
    '''
    Bulk Load the strain database
    '''


    return render_template('strain/bulkgood.html')
