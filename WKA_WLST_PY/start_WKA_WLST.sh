#!/bin/bash

# Use the setDomainEnv.sh for the below paths: 
export WL_HOME=DEMO_PATH/wlserver
export DOMAIN_HOME=DEMO_PATH
export JAVA_HOME=DEMO_PATH
export PATH=$PATH:$JAVA_HOME/bin

# Use a custom location for the below paths.
# The WLST_OUTPUT_PATH directory value must have a trailing slash!
# The WLST_OUTPUT_FILE must be an html file
export WLST_OUTPUT_PATH=DEMO_PATH/
export WLST_OUTPUT_FILE=WLST_Output.html

#export JAVA_OPTIONS="-Xms1g -Xmx1g"

# Please invoke the wlst.sh script under oracle_common/common/bin and only if not possible from the old WL_HOME/common/bin path:
DEMO_PATH/oracle_common/common/bin/wlst.sh Start_WKA_WLST.py

# The recommendation is to use Python 3 for the below row:
python3 Linux_OS_UI.py


# If Python 2 is the only one available then try: python Linux_OS_UI.py
# However, the recommendation is to use Python 3.




