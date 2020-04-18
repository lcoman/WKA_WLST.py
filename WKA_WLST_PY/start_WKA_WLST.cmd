@ECHO ON

SETLOCAL

@REM Use the setDomainEnv.cmd for the below paths: 
set WL_HOME=DEMO_PATH\wlserver
set DOMAIN_HOME=DEMO_PATH
set JAVA_HOME=DEMO_PATH

@REM Use a custom location for the below paths.
@REM The WLST_OUTPUT_PATH directory value must have a trailing slash!
@REM The WLST_OUTPUT_FILE must be an html file
set WLST_OUTPUT_PATH=DEMO_PATH\
set WLST_OUTPUT_FILE=WLST_Output.html

@REM set JAVA_OPTS="-Xms1024m -Xmx1024m"

@REM Please invoke the wlst.sh script under oracle_common\common\bin and only if not possible from the old WL_HOME\common\bin path:
call "DEMO_PATH\oracle_common\common\bin\wlst.cmd" Start_WKA_WLST.py


@REM The recommendation is to use Python 3 for the below row:
call python3 Windows_OS_UI.py

@REM If Python 2 is the only one available then try: call python Windows_OS_UI.py
@REM However, the recommendation is to use Python 3.
@REM If Python 3 is the only one available then is enought to run as: call python Windows_OS_UI.py


pause

ENDLOCAL

