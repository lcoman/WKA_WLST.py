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

           .sh/.cmd -> Start_WKA_WLST.py -> WKA_WLST_UI.py -> wka_wlstPy.py

     * .sh/.cmd defines the environment variable settings. 
     * Start_WKA_WLST.py covers the license and the connection details to the WLS domain. 
     * WKA_WLST_UI.py covers the UI around the WLST output. 
     * wka_wlstPy.py covers the WLST-related functions to gather the data from the domain. 

2. OS flow (per each main OS): 

           Windows_OS_UI.py - > Windows_OS_Details.py  
           Linux_OS_UI.py -> Linux_OS_Details.py

     * The UI script will identify the above wlst-related generated html and will append the OS-related UI template. 
     * The OS_Details script covers the OS-related functions to gather the OS data. 



## The trailing slash output path

   >   Intro: Don't use spaces in folder names.


Inside the .sh/.cmd file you customize some variables like the output path (WLST_OUTPUT_PATH) for the HTML file that will be generated. 

     This WLST_OUTPUT_PATH directory value must have a trailing slash!

There is also a comment in the files about the necessity for a trailing slash.

If there is no trailing slash, the script will raise no error for the WLST sections but the file will be created in a wrong folder based on the path you mentioned; it's actually 1 folder prior the last  one.
The OS details will not be appended to the same HTML file since an error will be raised; in the end you will only have the WLST details but the HTML file will not be fully functional and no OS details will be available.
  
Let's assume the "Videos" folder as the output folder and the below environment variables:

WLST_OUTPUT_FILE=wlst_PY_Output.html
DOMAIN NAME is "bpm_leo".

In addition to the above variables we have the below WLST_OUTPUT_PATH and some 2 basic tests. 
 
   >  Test1

    WLST_OUTPUT_PATH = /home/leo/Videos

    Inside the /home/leo you will have the Videosbpm_leo_wlst_PY_Output.html file plus the below 
    error on the terminal:

    Traceback (most recent call last):
     File "Linux_OS_UI.py", line 9, in <module>
        f.write (  """
        NameError: name 'f' is not defined


   >  Test2

     WLST_OUTPUT_PATH = /home/leo/Videos/

     Inside the /home/leo/Videos  you will have the bpm_leo_wlst_PY_Output.html file. 

     No issues, no errors!


   >  The above also applies to the Windows platform.

       e.g. Use a path like the below one:

       set WLST_OUTPUT_PATH=c:\output_demo\
