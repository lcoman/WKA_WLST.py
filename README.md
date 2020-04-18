# WKA WLST.pλ
Well Known Attributes (WKA) WLST.pλ

Please find all the full details on my blog: [Well Known Attributes WLST.pλ ](http://leonardsoa.blogspot.com/2020/04/well-known-attributes-wlstp.html)

## How to run the script: 
## The flow 

There are 2 main flows:

1. WLST flow:

> .sh/.cmd -> Start_WKA_WLST.py -> WKA_WLST_UI.py -> wka_wlstPy.py

* .sh/.cmd will define the envrionment variables. 
* Start_WKA_WLST.py will cover the license and will connect to the domain. 
* WKA_WLST_UI.py  covers the UI around the WLST output. 
* wka_wlstPy.py covers the WLST-related functions to gather the data. 

2. OS flow per each main OS: 

> Windows_OS_UI.py - > Windows_OS_Details.py  
> Linux_OS_UI.py -> Linux_OS_Details.py

* The UI file will identify the above generated html file and will append the UI template. 
* The OS_Details file covers the OS-related functions to gather the OS data. 
