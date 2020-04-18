# WKA WLST.py [also known as Well Known Attributes WLST.py] script performs Oracle WebLogic Server WLST MBeans data gathering. 
# For the Oracle WebLogic Server details the script is using only the built-in WLST features.   
# The WLST output details are printed to an HTML-CSS-JS file which is built dynamically by this Python-Jython script.
# The generated UI is powered by MDBootstrap.com (MDB) - using the CDN option. Download the MDB on your local machine and update the html to point to the local MDB if the remote CDN is not an option. 
# Several external and open source JavaScript functions were used. 
# In addition to the WLST output, some basic OS-related (Microsoft Windows and Linux) details are included in the generated html report - using a separated Python3 script.
# Repo: github.com/lcoman/WKA_WLST.py
# Author: leonardsoa.blogspot.com
# Date: March-April 2020.
# Version 1.1



import java.util.regex.Matcher
import java.util.regex.Pattern
import os
import string
from java.lang import *
from java.util import Date


	
DOMAIN_HOME = os.environ["DOMAIN_HOME"]
OUTPUT_FILE_PATH = os.environ["WLST_OUTPUT_PATH"]
OUTPUT_FILE = os.environ["WLST_OUTPUT_FILE"]



if DOMAIN_HOME == '':
	DOMAIN_HOME = raw_input('Enter the DOMAIN_HOME, specify full path: ')
	
if OUTPUT_FILE_PATH== '':	
	OUTPUT_FILE_PATH = raw_input('Enter the output directory, specify full path including final trailing slash: ')

if OUTPUT_FILE== '':	
	OUTPUT_FILE = raw_input('Enter the output file name, specify .html as the file extension: ')

if os.path.isdir(DOMAIN_HOME) == false:
 	raise Exception ('Invalid DOMAIN_HOME. The path does not exist. Check the .cmd or .sh file and try again.')

if os.path.isdir(OUTPUT_FILE_PATH) == false:
 	raise Exception ('Invalid Output Directory. The path does not exist. Try again.')


MIT_LICENSE = raw_input(""" 
________________________________   \n
          MIT License 
________________________________   \n
Copyright (c) 2020  leonardsoa.blogspot.com \n
Permission is hereby granted, free of charge, to any person obtaining a copy 
of this software and associated documentation files (the "Software"), to deal 
in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHOR, THE DEVELOPER OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

THE DEVELOPER DOES NOT GUARANTEE THAT THE SOFTWARE WILL PERFORM ERROR-FREE OR 
UNINTERRUPTED OR THAT THE DEVELOPER WILL CORRECT ALL PROGRAMS ERRORS.  

IN NO EVENT WILL THE DEVELOPER OR SOME THIRD PARTY BE LIABLE FOR ANY INDIRECT, INCIDENTAL, 
SPECIAL, PUNITIVE OR CONSEQUENTIAL DAMAGES, OR DAMAGES FOR LOSS OF PROFITS, REVENUE, DATA OR DATA 
USE, INCURRED BY YOU OR ANY THIRD PARTY.

TEST THE SOFTWARE ON A TEST ENVIRONMENT FIRST AND ONLY LATER TEST IT ON PRODUCTION ENVIRONMENTS.

IF YOU SKIP OR AVOID THE LICENSE BY RUNNING DIRECTLY THE OTHER SCRIPTS THEN BY DEFAULT YOU ACCEPT THE LICENSE.
 

By running this script you accept the above License? (Y /N ) :  """).lower()

if MIT_LICENSE == 'y':
 ADMIN_CONNECTION = raw_input('Is your domain Admin Server up and running and do you have the connection details? (Y /N ): ').lower()

 if ADMIN_CONNECTION == 'y':
		
  try:
	 #Capture username / password credentials to connection to the WLS domain
	 URL = raw_input('Enter the connection URL to Admin Server [e.g t3://localhost:7001]: ')
	 username = raw_input('Enter the Admin username [e.g. weblogic]: ')
	 password = "".join(java.lang.System.console().readPassword("Enter the Admin password [e.g. welcome1]: %s", [prompt]))
	 # Note: the value typed in for password will not be echoed back to the console.
	 # connect('weblogic','welcome1','t3://localhost:7001')
	 connect(username, password,URL)
  except:
		print ("There has been a problem connecting to the Admin Server. Please verify the connection details and try again.")
		exit()
		
  try:
	 execfile('WKA_WLST_UI.py')
  except:
	 print "There has been a problem running WKA_WLST_UI.py."
	 exit()

 else :
  print "Admin Server is down or unavailable so closing the script. For the current release the Admin Server should be up and running."
  exit()


else :
 print "License was not accepted so closing the script. "
 
 exit()


