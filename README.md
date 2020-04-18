# WKA WLST.pλ
Well Known Attributes (WKA) WLST.pλ

Please find all the full details on my blog: [Well Known Attributes WLST.pλ ](http://leonardsoa.blogspot.com/2020/04/well-known-attributes-wlstp.html)

## How to run the script: 

1. Download the attached (9) files from the WKA_WLST_PY folder and, on your machine, in the same location create an "output" folder.
2. Open the appropriate OS file (.sh or .cmd) in an editor and change the environment variable settings to suit your system.
- You can generate the output html file inside the "output" folder or any other custom folder. 
3. Open a terminal and run the appropriate OS file (.sh or .cmd).
- e.g. ./start_WKA_WLST.sh
- Accept the License
- Provide the AdminServer connection details: URL, user and password. 
4. Once the script is done: open the generated html file.

## The flow 

There are 2 main flows:

1. WLST flow:

> .sh/.cmd -> Start_WKA_WLST.py -> WKA_WLST_UI.py -> wka_wlstPy.py

* .sh/.cmd defines the environment variable settings. 
* Start_WKA_WLST.py will cover the license and will connect to the domain. 
* WKA_WLST_UI.py covers the UI around the WLST output. 
* wka_wlstPy.py covers the WLST-related functions to gather the data frm the domain. 

2. OS flow (per each main OS): 

> Windows_OS_UI.py - > Windows_OS_Details.py  
> Linux_OS_UI.py -> Linux_OS_Details.py

* The UI file will identify the above wlst generated html and will append the OS-related UI template. 
* The OS_Details file covers the OS-related functions to gather the OS data. 
