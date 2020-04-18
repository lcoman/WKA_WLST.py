# WKA WLST.pλ
Well Known Attributes (WKA) WLST.pλ

Please find all the full details on my blog: http://leonardsoa.blogspot.com/2020/04/well-known-attributes-wlstp.html

# How to run the script: 

1. Download the attached (9) files and in the same location create an "output" folder.
2. Open the appropriate OS file (.sh or .cmd) in an editor and change the environment variable settings to suit your system.
2.1. You can generate the output html file inside the "output" folder or any other custom folder. 
3. Open a terminal and run the appropriate OS file (.sh or .cmd).
e.g. ./start_WKA_WLST.sh
3.1 Accept the License
3.2 Provide the AdminServer connection details: URL, user and password. 
4. Once the script is done: open the generated html file. 

# The flow 

There are 2 main flows:

1. WLST flow:

.sh/.cmd -> Start_WKA_WLST.py -> WKA_WLST_UI.py -> wka_wlstPy.py

.sh/.cmd will define the envrionment variables. 

Start_WKA_WLST.py will cover the license and will connect to the domain. 

WKA_WLST_UI.py  covers the UI around the WLST output. 

wka_wlstPy.py covers the WLST-related functions to gather the data. 

2. OS flow per each main OS: 

Windows_OS_UI.py - > Windows_OS_Details.py  

Linux_OS_UI.py -> Linux_OS_Details.py

The UI file will identify the above generated html file and will append the UI template. 
The OS_Details file covers the OS-related functions to gather the OS data. 
