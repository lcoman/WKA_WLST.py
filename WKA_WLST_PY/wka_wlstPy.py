# This is the  script that covers all the WLST-related functions.
# The main pattern used was the WLST ls() function. 



def sortare(lst):
 l = list(lst)
 l.sort()
 return l
# --------------------------------------------------



# ---------------------------------------------
# e.g. listValuesVerticalCheck ("id_1234" , "domainConfig", "Servers")

def listValuesVerticalCheck (*argv):

 domainConfig()
 cd ('/')
 DomainNameIntro = get('Name')
 
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()
 
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 cd ('/')

 try: 
    cd (argv[2])
    
    my_apps_list = ls(returnMap='true')

    if len (my_apps_list) > 0 :
       listValuesVertical(*argv); 
    
    else:
       print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
       print >>f, genericPath
       print >>f, "</kbd>"
       print >>f, "</br></p>"

       if "Libraries" == argv[2]: 
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Libraries found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
       elif "AppDeployments" == argv[2]:
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Appplications found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
       elif "JDBCSystemResources" == argv[2]:
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Data Sources found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
       elif "JMS" in argv[2]:
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No JMS found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
       elif "Coherence" in argv[2]:
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Coherence found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
       
       else:
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No such resource found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
 
 except: 
    print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
    print >>f, genericPath
    print >>f, "</kbd>"
    print >>f, "<p> </p>"
    print >>f, """ <div class="card"> <div class="card-body"><h4 class="card-title"><i class="fas fa-exclamation-triangle"></i></h4><p class="card-text"> <h3>The MBean <font color= "#f29111">"""  +  '/'.join(argv[2:4])  + """ </font> is not part of the """ + DomainNameIntro +   """ domain or No such resource found for this domain.   </br>  Review the MBean name/path or upgrade to the latest FMW release.</h3></p></div></div>"""
    
 
 return ('')

# --------------------------------------------------


# --------------------------------------------------
# listValuesVertical  - START 

def listValuesVertical(*argv ):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()
 
 cd ('/')
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 obj = {}


 for server in myservers:
    xy_server = java.lang.String(server)
    
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:]) + '/' + server
    

    if lengthPathParams > 1: 
       cd (xy_server)
       cd (serverPath)
           
       a = ls ('a'); 
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
       obj[server] = b
      
       for iteme in b: 
          h = iteme[0]
          code_atribute.append(h)

       cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot))
       
      
    else:   
       cd (xy_server)
       
       a = ls ('a')
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
       obj[server] = b
      
       for iteme in b: 
          h = iteme[0]  
          code_atribute.append(h)
             
       cd ('../'* lengthPathParams);
     

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
  
 print >>f, genericPath
 print >>f, "</kbd>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_123" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"


 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"

 for server in myservers:
    xy_server = java.lang.String(server)
 
    print >>f, "<th>"
    print >>f, xy_server
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"  

 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
 
    for key in sortare(obj.iterkeys()):
       a = obj[key]
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)

          try:
             if "ActivationTime" in ase [0][0]:
                float_ase =  float(ase [0][1])
                print >>f, "<td>"
                print >>f, datetime.datetime.fromtimestamp( float_ase / 1000.0).strftime("%A, %d-%B-%Y  [%H:%M:%S  %Z]") 
                print >>f, "</td>"
           
             elif "HeapFreeCurrent"  in ase [0][0] or "HeapSizeCurrent"  in ase [0][0] or "HeapSizeMax"  in ase [0][0]:
                print >>f, "<td>" , ase [0][1] ," bytes =",  int (ase [0][1])/(1024*1024)  , " Mb"  , "</td>"
           
             elif "HeapFreePercent" in ase [0][0]:
                print >>f, "<td>" , ase [0][1] ,"%" , "</td>"
             
             elif "Uptime"  in ase [0][0]: 
                print >>f, "<td>" , ase [0][1] ," ms =",  "%.2f" % (float(ase [0][1])/(1000* 60*60))  , " h" , "</td>"    

             elif "State" in ase [0][0] and "RUNNING" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-arrow-up\"></i>  " ,    ase [0][1]  , "</td>"

             elif "State" in ase [0][0] and "SHUTDOWN" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-arrow-down\"></i>  " ,    ase [0][1]  , "</td>"

             elif "State" in ase [0][0] and "ADMIN" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-exclamation-triangle\"></i>  " ,    ase [0][1]  , "</td>" 

             elif "State" in ase [0][0] and "FAILED" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-times-circle\"></i>  " ,    ase [0][1]  , "</td>"

             elif "State" in ase [0][0] and "STARTING" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-play\"></i>  " ,    ase [0][1]  , "</td>"    
           
             else:
                print >>f, "<td>"
                print >>f, " ".join([str(x) for x in ase [0][1::]])
                print >>f, "</td>"

                 
          except:
             print >>f, "<td>"
             print >>f, "NO Value"
             print >>f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
    
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 return ('')


# listValuesVertical  - STOP
# ---------------------------------------------



# ---------------------------------------------
# e.g. listValuesHorizontalCheck ("id_1234" , "domainConfig", "Servers") 

def listValuesHorizontalCheck (*argv):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 
 cd ('/')
 DomainNameIntro = get('Name')
 
 try: 
    cd (argv[2])
    
    my_apps_list = ls(returnMap='true')

    if len (my_apps_list) > 0 :
       listValuesHorizontal(*argv)
    
    else:
       pass
 
 except: 
    pass  
 
 return ('')

# --------------------------------------------------



# --------------------------------------------------
#listValuesHorizontal  - START 

def listValuesHorizontal(*argv ):
 
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = '<i class=\"fas fa-angle-double-right\"></i>'.join(argv[2:])
 obj = {}
  

 for server in myservers:
    xy_server = java.lang.String(server)
    
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:]) + '/' + server
    
    if lengthPathParams > 1: 
       cd (xy_server)             
       cd (serverPath)
           
       a = ls ('a')
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
       obj[server] = b
      
       for iteme in b: 
          h = iteme[0]
          code_atribute.append(h)

       cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot))
       
      
    else:   
       cd (xy_server)
       
       a = ls ('a')
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
       obj[server] = b
      
       for iteme in b: 
          h = iteme[0]  
          code_atribute.append(h)
             
       cd ('../'* lengthPathParams)
    

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_1234" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"
 print >>f,  " </form> "
 
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""


 print >>f, "<tr>"
 print >>f, "<th>WLS Resource</th>"


 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f, zxc
    print >>f, "</th>"


 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"


 for key in sortare(obj.iterkeys()):
 
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
 
    a = obj[key]

    for zxc in code_atribute_unique:
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          
          try:
             
             if "ActivationTime" in ase[0][0]:
                float_ase = float(ase[0][1])
                print >> f, "<td>"
                print >> f, datetime.datetime.fromtimestamp(float_ase / 1000.0).strftime("%A, %d-%B-%Y  [%H:%M:%S  %Z]")
                print >> f, "</td>"


             elif "HeapFreeCurrent" in ase[0][0] or "HeapSizeCurrent" in ase[0][0] or "HeapSizeMax" in ase[0][0]:
                print >> f, "<td>", ase[0][1], " bytes =", int(ase[0][1]) / (1024 * 1024), " Mb", "</td>"

             elif "HeapFreePercent" in ase [0][0]:
                print >>f, "<td>" , ase [0][1] ,"%" , "</td>"
             
             elif "Uptime" in ase[0][0]:
                print >> f, "<td>", ase[0][1], " ms =", "%.2f" % (float(ase[0][1]) / (1000 * 60 * 60)), " h", "</td>"

             elif "State" in ase[0][0] and "RUNNING" in ase[0][1]:
                print >> f, "<td> <i class=\"fas fa-arrow-up\"></i>  ", ase[0][1], "</td>"

             elif "State" in ase[0][0] and "SHUTDOWN" in ase[0][1]:
                print >> f, "<td> <i class=\"fas fa-arrow-down\"></i>  ", ase[0][1], "</td>"

             elif "State" in ase[0][0] and "ADMIN" in ase[0][1]:
                print >> f, "<td> <i class=\"fas fa-exclamation-triangle\"></i>  ", ase[0][1], "</td>"

             elif "State" in ase[0][0] and "FAILED" in ase[0][1]:
                print >> f, "<td> <i class=\"fas fa-times-circle\"></i>  ", ase[0][1], "</td>"

             elif "State" in ase [0][0] and "STARTING" in ase [0][1]:
                print >>f,  "<td> <i class=\"fas fa-play\"></i>  " ,    ase [0][1]  , "</td>"        

             else:
                print >> f, "<td>"
                print >> f, " ".join([str(x) for x in ase[0][1::]])
                print >> f, "</td>"

          except:
             print >> f, "<td>"
             print >> f, "NO Value"
             print >> f, "</td>"


       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
 
    print >>f, "</tr>"
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Horizontal" + "')\"> Export To XLS </button> </p> </br>"
 return ('')


#listValuesHorizontal  - STOP
# --------------------------------------------------






# --------------------------------------------------
# listResourceTargetTable
# e.g. listResourceTargetTable ( "id_1234" , "domainConfig", "AppDeployments", "Targets")

def listResourceTargetTable(*argv):
 
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 
 cd ('/')
 DomainNameIntro = get('Name')
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 cd (argv[2])

 my_apps_list = ls(returnMap='true')
 
 if len (my_apps_list) > 0 :
    listResourceTarget(*argv)
 
 else:   
    print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
    print >>f, genericPath
    print >>f, "</kbd>"
    print >>f, "</br></p>"

    if "Libraries" in argv[2]: 
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Libraries found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
    
    elif "AppDeploy" in argv[2]:
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Appplications found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""  
    
    elif "JDBCSystemResources" in argv[2]:
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Data Sources found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
    
    elif "JMS" in argv[2]:
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No JMS found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
    
    elif "Coherence" in argv[2]:
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Coherence found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>"""
    
    else:
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No such resource found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>""" 
 
 return ('')

# --------------------------------------------------


#listResourceTarget - START

def listResourceTarget(*argv):
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 cd (argv[2])
 my_resource_list = ls(returnMap='true')
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])

 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
 print >>f, genericPath
 print >>f, "</kbd>"
 print >>f, "</p>"
 
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_12345" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"

 print >>f,  " </form> "
 
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>WLS Resource</th>"
 print >>f, "<th>Server(s)</th>"
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 for resource in my_resource_list: 
    xy_resource = java.lang.String(resource)
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f,resource
    print >>f, "</td>"
    cd (xy_resource)
    cd (argv[3])
    
    my_resource_target = ls(returnMap='true')
    print >>f, "<td>"
    
    if not my_resource_target and 'Clusters' in argv[2]:
       print >>f, "No server"
    
    elif not my_resource_target and 'AppDeployments' in argv[2]:
       print >>f, "No target"

    elif not my_resource_target and 'Libraries' in argv[2]:
       print >>f, "No target"

    elif not my_resource_target and 'JMS' in argv[2]:
       print >>f, "No target"

    elif not my_resource_target and 'Stores' in argv[2]:
       print >>f, "No target"   
  

    elif not my_resource_target and 'CoherenceClusterSystemResources' in argv[2]:
       print >>f, "No server"

    else:  
       print >>f, ", ".join([str(x) for x in my_resource_target] )
   
    print >>f, "</td>"
    print >>f, "</tr>"
    cd ('../..')
 
 print >>f, "</tbody></table>"

 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')
 

#listResourceTarget - STOP 
# --------------------------------------------------



# --------------------------------------------------
#listDomainConfig - start 
# e.g. listDomainConfig("id_1234")


def listDomainConfig(id_table): 
 
 print >>f, "<p><kbd>wlst:domainConfig </kbd </p> "
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
 
 print >>f, "id=\" " + id_table + "_78ABC5023" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">"
 print >>f,  " </form> "


 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">"
 
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"
 print >>f, "<th>Value</th>"
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"
 
 domainConfig()
 cd ('/')
 a = ls ('a')
 b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]

 for iteme in b: 
    print >>f, "<tr class=\"" +  id_table  + "\">"
    print >>f, "<td>"
    print >>f, iteme [0]
    print >>f, "</td>"
    print >>f, "<td>"
    print >>f, iteme [1]
    print >>f, "</td>"
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Domain Attributes" + "')\"> Export To XLS </button> </p> </br>"

 return ('')


#  listDomainConfig - stop 
# --------------------------------------------------






# --------------------------------------------------
# listIntroDomain - START 
# e.g. listIntroDomain()

def listIntroDomain():
 
 domainConfig()
 cd ('/')
 DomainNameIntro = get('Name')
   
 print >>f, """
 <div class="col-md-12">
 <!-- Heading -->
 <h3 class="display-4 font-weight-bold white-text pt-5 mb-2">FMW Domain:
 """ 

 print >>f, DomainNameIntro
 
 print >>f, """
 </h3>
 <!-- Divider -->
 <hr class="hr_title ">
 <!-- Description -->
 <h5 class="white-text my-4">Report generated on 
 """
    
 print >>f, datetime.datetime.today().strftime("%A, %d-%B-%Y  [%H:%M]" )  + "."
    
 print >>f, """ 
 </h5>
 </div>
 """
 return ('')

# listIntroDomain - STOP
# --------------------------------------------------





# --------------------------------------------------
#listDomainOverviewTable  - START 
# e.g. listDomainOverviewTable("id_1234")

def listDomainOverviewTable(id_table): 

 print >>f, "<p><kbd> Domain Overview </kbd </p>"
 
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
 print >>f, "id=\" " + id_table + "_123456" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">"
 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">"
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>Server</th>"
 print >>f, "<th>Cluster</th>"
 print >>f, "<th>Machine</th>"
 print >>f, "<th>Listen Port</th>"
 print >>f, "<th>State</th>"
 print >>f, "<th>Health State</th>"
 print >>f, "<th>Listen Address</th>"
 print >>f, "<th>SSL Listen Port</th>"
 print >>f, "<th>SSL Listen Port Enabled</th>"
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 domainConfig()
 cd ('/')
 cd ('Servers')
 
 my_servers_list = ls(returnMap='true')

 for server in my_servers_list: 
    xy_server = java.lang.String(server)
    print >>f, "<tr class=\"" +  id_table  + "\">"
    print >>f, "<td>"
    print >>f,server
    print >>f, "</td>"
    cd (xy_server)
    
    cd ('Cluster')
    my_server_cluster = ls(returnMap='true')
    print >>f, "<td>"
    if not my_server_cluster:
       print >>f, " No Cluster"
    else:  
       print >>f, ", ".join([str(x) for x in my_server_cluster] )
    print >>f, "</td>"
    
    cd ('../Machine')
    my_server_machine = ls(returnMap='true')
    print >>f, "<td>"
    if not my_server_machine:
       print >>f, " No Machine"
    else:  
       print >>f, ", ".join([str(x) for x in my_server_machine] )
    print >>f, "</td>"

    cd ('..')
    ls_port= get ('ListenPort')
    print >>f, "<td>"
    if not ls_port:
       print >>f, " No Listen Port"
    else:  
       print >>f, ls_port
    print >>f, "</td>"
    
    try:
       domainRuntime();
       cd ('/')
       cd('ServerLifeCycleRuntimes')
       cd (xy_server)
       state= get ('State')
       print >>f, "<td>"
       if not state:
          print >>f, "<i class=\"fas fa-exclamation\"></i> State unknown " 
       else:  
          if "RUNNING" in state: 
             print >>f,  "<i class=\"fas fa-arrow-up\"></i>  " ,    state  
          elif  "SHUTDOWN" in state: 
             print >>f,  "<i class=\"fas fa-arrow-down\"></i>  "  , state  
          elif  "ADMIN" in state: 
             print >>f,  "<i class=\"fas fa-exclamation-triangle\"></i>  " , state  
          elif  "FAILED" in state: 
             print >>f,  "<i class=\"fas fa-times-circle\"></i>  " ,    state  
          elif "STARTING" in state:
                print >>f,  "<td> <i class=\"fas fa-play\"></i>  " ,    state        

          else:  	
             print >>f,  state 
       print >>f, "</td>";

    except: 
       state = "SHUTDOWN"
       print >>f, "<td>"
       print >>f,  "<i class=\"fas fa-arrow-down\"></i>  "  , state 
       print >>f, "</td>"
       
    if "RUNNING" in state:
       cd ('../../ServerRuntimes')
       cd (xy_server)
       health_stat= get ('HealthState')
       
       if not health_stat:
          print >>f, "<td>"
          print >>f, "Health State Unknown"
          print >>f, "</td>"
       else:  
          health_stat_string = str(health_stat)
          health_stat_strip = health_stat_string.strip('Component:null,Partition: null,State:,MBean:null,Symptoms:[], ReasonCode:[] ')
          if "HEALTH_OK" in health_stat_strip:
             print >>f, "<td>"
             print >>f, "<i class=\"fas fa-check\"></i>"+ " OK  "
             print >>f, "</td>"
          else: 
             print >>f, "<td>"
             print >>f, health_stat_strip + "  "
             print >>f, "</td>"
    else: 
       print >>f, "<td>"
       print >>f, " <i class=\"fas fa-times\"></i> Not reachable  " 
       print >>f, "</td>"
       
    if "RUNNING" in state:  
       ls_addr= get('ListenAddress')
       print >>f, "<td>"
       print >>f, ls_addr
       print >>f, "</td>"
    else:  
       domainConfig()
       cd ('/')
       cd ('Servers')
       cd (xy_server)
       ls_addr2= get('ListenAddress')
       if ls_addr2 == '' or ls_addr2 == 'None' or ls_addr2 == 'null':
          print >>f, "<td>"
          print >>f, "All Local Addresses"
          print >>f, "</td>"
       else: 
          print >>f, "<td>"
          print >>f, ls_addr2
          print >>f, "</td>"

    if "RUNNING" in state:  
       domainConfig()
       cd ('../../../../../..')
       cd ('Servers')
       cd (xy_server)
       cd ('SSL')
       cd (xy_server)
       ssl_port= get ('ListenPort')
       ssl_enabled= get ('Enabled')
    else: 
       domainConfig()
       cd ('/')
       cd ('Servers')
       cd (xy_server)
       cd ('SSL')
       cd (xy_server)
       ssl_port= get ('ListenPort')
       ssl_enabled= get ('Enabled')


    if not ssl_port:
       print >>f, "<td>"
       print >>f, "No SSL Port found"
       print >>f, "</td>"
    else: 
       print >>f, "<td>"
       print >>f, ssl_port
       print >>f, "</td>"

    if ssl_enabled == 1:
       print >>f, "<td>"
       print >>f, "true"
       print >>f, "</td>"
    else:
       print >>f, "<td>"
       print >>f, "false"
       print >>f, "</td>"

    print >>f, "</tr>"
    cd ('../../..')
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Domain Overview" + "')\"> Export To XLS </button> </p> </br>"
 return ('')


#listDomainOverviewTable  - STOP
# --------------------------------------------------





# --------------------------------------------------
#listWMTargetCheck  
# e.g. listWMTargetCheck ("id_1234") 

def listWMTargetCheck(*argv):
 
 domainConfig()
 cd ('/')
 DomainNameIntro = get('Name')
 cd ('SelfTuning')
 cd (DomainNameIntro)
 cd ('WorkManagers')
 my_wm_list = ls(returnMap='true')
 

 if len (my_wm_list) > 0 :
    listWorkManagersTargets(*argv)
 else:
    print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Work Manager found in the """ + DomainNameIntro + """ domain.</h3></p></div></div>""" 
 
 return ('')

# --------------------------------------------------




#listWorkManagersTargets - START

def listWorkManagersTargets(id_table):

 print >>f, """<p><kbd> wlst:domainConfig <i class="fas fa-angle-double-right"></i> SelfTuning <i class="fas fa-angle-double-right"></i> WorkManagers <i class="fas fa-angle-double-right"></i> Targets </p> """
  
 domainConfig()
 cd ('/')
 cd ('SelfTuning')
 my_list = ls(returnMap='true')
  
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
  
 print >>f, "id=\" " + id_table + "_78AZZZBC579105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">"
 print >>f,  " </form> "
  
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">"
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>WorkManager</th>"
 print >>f, "<th>Target</th>"
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 for domain in my_list: 
    xy_domain = java.lang.String(domain)
    cd (xy_domain)
    cd ('WorkManagers')
    my_wm_list = ls(returnMap='true')
    
    for wm in my_wm_list: 
       print >>f, "<tr class=\"" +  id_table  + "\">"
       print >>f, "<td>"
       print >>f,wm
       print >>f, "</td>"
       cd (wm)
       cd ('Targets')
       my_wm_target = ls(returnMap='true')
       print >>f, "<td>"
       
       if not my_wm_target:
          print >>f, " No target"
       else:  
          print >>f, ", ".join([str(x) for x in my_wm_target] )
       
       print >>f, "</td>"
       print >>f, "</tr>"
       cd ('../..')
    
    cd ('../..')
 
 print >>f, "</tbody></table>";
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Work Managers Target" + "')\"> Export To XLS </button> </p> </br>"
 return ('')


#listWorkManagersTargets - STOP
# --------------------------------------------------





# --------------------------------------------------
#listAuthenticationProvidersVertical  - START 
# e.g. listAuthenticationProvidersVertical("id_1234")


def listAuthenticationProvidersVertical(id_table):

 print >>f, """ <p><kbd> wlst:domainConfig <i class="fas fa-angle-double-right"></i> SecurityConfiguration <i class="fas fa-angle-double-right"></i> Realms <i class="fas fa-angle-double-right"></i> AuthenticationProviders</kbd></p>"""
 
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
  
 print >>f, "id=\" " + id_table + "_12121ABCZXCV2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">"
 print >>f,  " </form> "
 
 domainConfig()
 cd ('/')
 cd ('SecurityConfiguration')
 myservers = ls(returnMap='true')
 code_atribute = []

 for server in myservers:
    xy_server = java.lang.String(server)
    cd (xy_server)
    cd ('Realms')
    x_Realms = ls(returnMap='true')
    for my_realm in x_Realms:
       cd (my_realm)
       cd ('AuthenticationProviders')
       x_prov = ls(returnMap='true')
       for my_prov in x_prov:
          cd (my_prov)
          a = ls ('a')
          b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
          for iteme in b: 
             h = iteme[0]
             code_atribute.append(h)
          cd ('..')
       cd ('../..')
    cd ('../..')
   
 obj = {}

 for server in myservers:
    xy_server = java.lang.String(server)
    cd (xy_server)
    cd ('Realms')
    x_Realms = ls(returnMap='true')
    for my_realm in x_Realms:
       cd (my_realm)
       cd ('AuthenticationProviders')
       x_prov = ls(returnMap='true')
       for my_prov in x_prov:
          cd (my_prov)
          a = ls ('a')
          b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
          obj[my_prov] = b
          cd ('..') 
       cd ('../..')
    cd ('../..')

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">"
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"

 for my_prov in x_prov:
    ab_prov = java.lang.String(my_prov)
    print >>f, "<th>"
    print >>f, ab_prov
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>" 

 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +  id_table  + "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
    for key in sortare(obj.iterkeys()):
       a = obj[key]
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          print >>f, "<td>"
          print >>f, " ".join([str(x) for x in ase[0][1::]] ) 
          print >>f, "</td>"
       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "AuthenticationProviders" + "_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')

#listAuthenticationProvidersVertical  - STOP
# --------------------------------------------------





# --------------------------------------------------
#listAuthenticationProvidersHorizontal  - START 
# e.g. listAuthenticationProvidersHorizontal("id_1234")

def listAuthenticationProvidersHorizontal(id_table):
  
 domainConfig()
 cd ('/')
 cd ('SecurityConfiguration')
 myservers = ls(returnMap='true')
 code_atribute = []
 
 for server in myservers:
    xy_server = java.lang.String(server)
    cd (xy_server)
    cd ('Realms')
    x_Realms = ls(returnMap='true')
    for my_realm in x_Realms:
       cd (my_realm)
       cd ('AuthenticationProviders')
       x_prov = ls(returnMap='true')
       for my_prov in x_prov:
          cd (my_prov)
          a = ls ('a')
          b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
          for iteme in b: 
             h = iteme[0]
             code_atribute.append(h)
          cd ('..')
       cd ('../..')
    cd ('../..')
   
 obj = {}

 for server in myservers:
    xy_server = java.lang.String(server)
    cd (xy_server)
    cd ('Realms')
    x_Realms = ls(returnMap='true')
    for my_realm in x_Realms:
       cd (my_realm)
       cd ('AuthenticationProviders')
       x_prov = ls(returnMap='true')
       for my_prov in x_prov:
          cd (my_prov)
          a = ls ('a')
          b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
          obj[my_prov] = b
          cd ('..')
       cd ('../..')
    cd ('../..')

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()
 
 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
  
 print >>f, "id=\" " + id_table + "_895623258ABCZXCV2105123" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">"
 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">"
 print >>f, "<thead class=\"thead-dark \">"
 print >>f, "<tr>"
 print >>f, "<th>WLS Resource</th>"

 for my_prov in code_atribute_unique:
    ab_prov = java.lang.String(my_prov)
    print >>f, "<th>"
    print >>f, ab_prov
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>" 

 for key in sortare(obj.iterkeys()):
    print >>f, "<tr class=\"" +  id_table  + "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
    a = obj[key]

    for zxc in code_atribute_unique:
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          print >>f, "<td>"
          print >>f, " ".join([str(x) for x in ase[0][1::]] )
          print >>f, "</td>"
       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "AuthenticationProviders" + "_Horizontal" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')

#listAuthenticationProvidersHorizontal  - STOP
# --------------------------------------------------






# --------------------------------------------------
# listValuesVerticalCustom- START 
# e.g. listValuesVerticalCustom ("id_1234" , "domainRuntime", "ServerRuntimes" , "ThreadPoolRuntime", "ThreadPoolRuntime")
# e.g. listValuesVerticalCustom ("id_1234" , "domainRuntime", "ServerRuntimes" , "JTARuntime", "JTARuntime")

def listValuesVerticalCustom(*argv ):
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()
 
 cd ('/')
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 obj = {}
 
 for server in myservers:
    xy_server = java.lang.String(server)
    serverPath= '/'.join(argv[3:]) 
    
    cd (xy_server)
    cd (serverPath)
           
    a = ls ('a')
    b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
    obj[server] = b
      
    for iteme in b: 
       h = iteme[0]
       code_atribute.append(h)

    cd ('../../../')
      
 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""  
 print >>f, genericPath
 print >>f, "</kbd>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_123AWER" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"

 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" >"""
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"

 for server in myservers:
    xy_server = java.lang.String(server)
 
    print >>f, "<th>"
    print >>f, xy_server
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"  

 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
 
    for key in sortare(obj.iterkeys()):
       a = obj[key]
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)

          try:
             print >>f, "<td>"
             print >>f, " ".join([str(x) for x in ase[0][1::]])
             print >>f, "</td>"
    
          except:
             print >>f, "<td>"
             print >>f, "NO Value"
             print >>f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')


# listValuesVerticalCustom - STOP
# --------------------------------------------------





# --------------------------------------------------
#listValuesHorizontalCustom  - START 
# e.g. listValuesHorizontalCustom ("id_1234" , "domainRuntime", "ServerRuntimes" , "ThreadPoolRuntime", "ThreadPoolRuntime") 
# e.g. listValuesHorizontalCustom ("id_1234" , "domainRuntime", "ServerRuntimes" , "JTARuntime", "JTARuntime")

def listValuesHorizontalCustom(*argv):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')	
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = '<i class=\"fas fa-angle-double-right\"></i>'.join(argv[2:])
 obj = {}
 
 for server in myservers:
    xy_server = java.lang.String(server)
    serverPath =  '/'.join(argv[3:])
    
    cd (xy_server)
    cd (serverPath)
    
    a = ls ('a')
    b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
    obj[server] = b
    
    for iteme in b: 
       h = iteme[0]
       code_atribute.append(h)

    cd ('../../../')


 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_12348525ABC" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"
 print >>f,  " </form> "

  
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""
 print >>f, "<tr>"
 print >>f, "<th>WLS Resource</th>"


 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f, zxc
    print >>f, "</th>"

 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 for key in sortare(obj.iterkeys()):
 
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
 
    a = obj[key]

    for zxc in code_atribute_unique:
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          
          try:
             if "ActivationTime" in ase[0][0]:
                float_ase = float(ase[0][1])
                print >> f, "<td>"
                print >> f, datetime.datetime.fromtimestamp(float_ase / 1000.0).strftime("%A, %d-%B-%Y  [%H:%M:%S  %Z]")
                print >> f, "</td>"

             elif "HeapFreeCurrent" in ase[0][0] or "HeapSizeCurrent" in ase[0][0] or "HeapSizeMax" in ase[0][0]:
                print >> f, "<td>", ase[0][1], " bytes =", int(ase[0][1]) / (1024 * 1024), " Mb", "</td>"

             elif "Uptime" in ase[0][0]:
                print >> f, "<td>", ase[0][1], " ms =", "%.2f" % (float(ase[0][1]) / (1000 * 60 * 60)), " h", "</td>"

             elif "State" in ase[0][0] and "RUNNING" in ase[0][1]:
                print >> f, "<td> <i class=\"fas fa-arrow-up\"></i>  ", ase[0][1], "</td>"

             elif "State" in ase[0][0] and "ADMIN" in ase[0][1]:
                print >> f, " <td> <i class=\"fas fa-exclamation-triangle\"></i>  ", ase[0][1], "</td>"

             else:
                print >> f, "<td>"
                print >> f, " ".join([str(x) for x in ase[0][1::]])
                print >> f, "</td>"

          except:
             print >> f, "<td>"
             print >> f, "NO Value"
             print >> f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle" data-toggle="tooltip" data-placement="right" title="" data-original-title="No such Attribute"></i> """
          print >>f, "</td>"
 
    print >>f, "</tr>"
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Horizontal" + "')\"> Export To Excel </button> </p> </br>"
 
 return ('')


#listValuesHorizontalCustom - STOP
# --------------------------------------------------





# ---------------------------------------------
# listValuesVerticalWMCheck
# e.g. listValuesVerticalWMCheck ("id_1234" , "domainConfig",  "SelfTuning",  "WorkManagers" )


def listValuesVerticalWMCheck (*argv):
 
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])	
 
 cd ('/')
 DOMAIN_NAME= get('Name')
 
 try: 
    cd (argv[2])
    cd (DOMAIN_NAME)
    cd (argv[3])
    
    my_list = ls(returnMap='true')

    if len (my_list) > 0 :
       listValuesVerticalWM(*argv) 
    
    else:
       print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
       print >>f, genericPath
       print >>f, "</kbd>"
       print >>f, "<p> </p>"
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No such SelfTuning resource found in the """ + DOMAIN_NAME + """ domain.</h3></p></div></div>"""
 

 except: 
    print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
    print >>f, genericPath
    print >>f, "</kbd>"
    print >>f, "<p> </p>"
    print >>f, """ <div class="card"> <div class="card-body"><h4 class="card-title"><i class="fas fa-exclamation-triangle"></i></h4><p class="card-text"> <h3>The MBean <font color= "#f29111">"""  +  '/'.join(argv[2:4])  + """ </font> is not part of the """ + DOMAIN_NAME +   """ domain or No such resource found for this domain.   </br>  Review the MBean name/path or upgrade to the latest FMW release.</h3></p></div></div>"""
    
 
 return ('')
 
# ----------------------------------------------




# ----------------------------------------------
# listValuesVerticalWM   - START 
 
def listValuesVerticalWM(*argv ):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')
 cd (argv[2])
 cd (DOMAIN_NAME)
 cd (argv[3])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 obj = {}
  

 for server in myservers:
    xy_server = java.lang.String(server)
    cd (xy_server)
               
    a = ls ('a')
    b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
    obj[server] = b
      
    for iteme in b: 
       h = iteme[0]
       code_atribute.append(h)

    cd ('..')
                  

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
  
 print >>f, genericPath
 print >>f, "</kbd>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_123" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"

 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" >"""
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"

 for server in myservers:
    xy_server = java.lang.String(server)

    print >>f, "<th>"
    print >>f, xy_server
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"  

 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
 
    for key in sortare(obj.iterkeys()):
       a = obj[key]
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)

          try:
             print >>f, "<td>"
             print >>f, ' '.join(ase[0][1:])
             print >>f, "</td>"

          except:
             print >>f, "<td>"
             print >>f, "NO Value"
             print >>f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')


# listValuesVerticalWM - STOP
# ----------------------------------------------




# ----------------------------------------------
# listValuesHorizontalWMCheck
# e.g. listValuesHorizontalWMCheck ("id_1234" , "domainConfig",  "SelfTuning",  "WorkManagers" )


def listValuesHorizontalWMCheck (*argv):
 
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')

 try: 
    cd (argv[2])
    cd (DOMAIN_NAME)
    cd (argv[3])
    
    my_list = ls(returnMap='true')

    if len (my_list) > 0 :
       listValuesHorizontalWM(*argv) 
    
    else:
       pass
 
 except: 
    pass
  
 
 return ('')

# ----------------------------------------------






# ----------------------------------------------
#listValuesHorizontalWM  - START 


def listValuesHorizontalWM(*argv ):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')
 cd (argv[2])
 cd (DOMAIN_NAME)
 cd (argv[3])

 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = '<i class=\"fas fa-angle-double-right\"></i>'.join(argv[2:])
 obj = {}
 

 for server in myservers:
    xy_server = java.lang.String(server)
    
    cd (xy_server)
               
    a = ls ('a')
    b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
    obj[server] = b
      
    for iteme in b: 
       h = iteme[0]
       code_atribute.append(h)

    cd ('..')
                 

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_1234" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"
 
 print >>f,  " </form> "
 
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" >"""


 print >>f, "<tr>"
 print >>f, "<th>WLS Resource</th>"


 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f, zxc
    print >>f, "</th>"


 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"


 for key in sortare(obj.iterkeys()):
    
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
 
    a = obj[key]

    for zxc in code_atribute_unique:
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          
          try:
             print >> f, "<td>"
             print >> f, " ".join([str(x) for x in ase[0][1::]])
             print >> f, "</td>"

          except:
             print >> f, "<td>"
             print >> f, "NO Value"
             print >> f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
 
    print >>f, "</tr>"
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Horizontal" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')

#listValuesHorizontalWM  - STOP

# ----------------------------------------------







# ----------------------------------------------
# getValuesVerticalWMFullOverviewCheck
# e.g. getValuesVerticalWMFullOverviewCheck ("id_1234" , "domainConfig",  "SelfTuning",  "WorkManagers" )

def getValuesVerticalWMFullOverviewCheck(*argv):
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])	
 cd ('/')
 DOMAIN_NAME= get('Name')
 
 try: 
    cd (argv[2])
    cd (DOMAIN_NAME)
    cd (argv[3])
    
    my_list = ls(returnMap='true')

    if len (my_list) > 0 :
       getValuesVerticalWMFullOverview(*argv)
    
    else:
       print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
       print >>f, genericPath
       print >>f, "</kbd>"
       print >>f, "<p> </p>"
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Work Manager found in the """ + DOMAIN_NAME + """ domain.</h3></p></div></div>"""
 
 except: 
    print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
    print >>f, genericPath
    print >>f, "</kbd>"
    print >>f, "<p> </p>"
    print >>f, """ <div class="card"> <div class="card-body"><h4 class="card-title"><i class="fas fa-exclamation-triangle"></i></h4><p class="card-text"> <h3>The MBean <font color= "#f29111">"""  +  '/'.join(argv[2:4])  + """ </font> is not part of the """ + DOMAIN_NAME +   """ domain or No such resource found for this domain.   </br>  Review the MBean name/path or upgrade to the latest FMW release.</h3></p></div></div>"""
 
 return ('')

# ---------------------------------------------




# ---------------------------------------------
# getValuesVerticalWMFullOverview - START 
 
def getValuesVerticalWMFullOverview(*argv ):
 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')
 cd (argv[2])
 cd (DOMAIN_NAME)
 cd (argv[3])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 
 obj = {} 

 for server in myservers:
    xy_server = java.lang.String(server)
       
    cd (xy_server)
    name= 'WorkManager Name'
    wmVal= get('Name') 
    wmInfo=  name,  wmVal
    wmInfoList1 = list(wmInfo)
    code_atribute.append(wmInfoList1[0])
    
    
    cd ('MaxThreadsConstraint') 
    myMaxThreadsConstraint = ls(returnMap='true')
    
    if len (myMaxThreadsConstraint) > 0:
       for maxThread in   myMaxThreadsConstraint: 
          maxConstraint= java.lang.String(maxThread)
          cd (maxConstraint)
          attributeName= 'MaxThreadsConstraint Name'
          attributeNameValue = str(maxConstraint)
          name= 'MaxThreadsConstraint'
          wmVal= str(get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList2 = list(wmInfo)
          wmInfoList22 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList2[0])
          code_atribute.append(wmInfoList22[0])
          
          cd ('..')
    
    else:
       wmInfoList2 = ['MaxThreadsConstraint', '-']   
       wmInfoList22 =['MaxThreadsConstraint Name', '-']           
    
    cd ('..')

    cd ('MinThreadsConstraint') 
    myMinThreadsConstraint = ls(returnMap='true')
    
    if len (myMinThreadsConstraint) >0 :
       for minThread in   myMinThreadsConstraint: 
          minConstraint= java.lang.String(minThread); 
          cd (minConstraint); 
          attributeName= 'MinThreadsConstraint Name'
          attributeNameValue = str(minConstraint)
          name= 'MinThreadsConstraint'
          wmVal= str( get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList3 = list(wmInfo)
          wmInfoList33 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList3[0])
          code_atribute.append(wmInfoList33[0])
          
          cd ('..')

    else:
       wmInfoList3 = ['MinThreadsConstraint', '-']   
       wmInfoList33 = ['MinThreadsConstraint Name', '-']

    cd ('..')

    cd ('Capacity') 
    myCapacityList = ls(returnMap='true');
    
    
    if len (myCapacityList) >0:
       for myCapacity in   myCapacityList: 
          myCapacity_x= java.lang.String(myCapacity); 
          cd (myCapacity_x); 
          attributeName= 'Capacity Name'
          attributeNameValue = str(myCapacity_x)
          name= 'Capacity'
          wmVal= str( get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList4 = list(wmInfo)
          wmInfoList44 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList4[0])
          code_atribute.append(wmInfoList44[0])
          
          cd ('..')
    
    else:
       wmInfoList4 = ['Capacity', '-']  
       wmInfoList44 =  ['Capacity Name', '-']
    
    cd ('..')
      
    
    wmInfoList = wmInfoList1 , wmInfoList2, wmInfoList22 ,wmInfoList3 ,wmInfoList33 ,wmInfoList4, wmInfoList44
    
    wmInfoList = list (wmInfoList)
     
    obj[server] = wmInfoList 
         
    cd ('..')
    

 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]] 
 code_atribute_unique_sort = code_atribute_unique.sort()

 
 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
 print >>f, genericPath
 print >>f, " <i class=\"fas fa-angle-double-right\"></i> Count Values</kbd>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_123AWSXC" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"

 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""
 print >>f, "<tr>"
 print >>f, "<th>Attribute</th>"

 for server in myservers:
    xy_server = java.lang.String(server)
 
    print >>f, "<th>"
    print >>f, xy_server
    print >>f, "</th>"
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"  

 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
 
    for key in sortare(obj.iterkeys()):
   
       a = obj[key]
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)

          try:      
             print >>f, "<td>"
             print >>f, ' '.join(ase[0][1::])
             print >>f, "</td>"

          except:
             print >>f, "<td>"
             print >>f, "NO Value"
             print >>f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"

    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Main_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')

# getValuesVerticalWMFullOverview - STOP
# ---------------------------------------------




# ---------------------------------------------
#getValuesHorizontalWMFullOverviewCheck   
# e.g. getValuesHorizontalWMFullOverviewCheck ("id_1234" , "domainConfig",  "SelfTuning",  "WorkManagers" ) 

def getValuesHorizontalWMFullOverviewCheck (*argv):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')

 try: 
    cd (argv[2])
    cd (DOMAIN_NAME)
    cd (argv[3])
    
    my_list = ls(returnMap='true');

    if len (my_list) > 0 :
       getValuesHorizontalWMFullOverview(*argv)    
    
    else:
       pass
 
 except: 
    pass
        
 return ('')

# ----------------------------------------------




# ----------------------------------------------
#getValuesHorizontalWMFullOverview  - START 


def getValuesHorizontalWMFullOverview(*argv ):

 if "domainConfig" in argv[1]:
    root = "domainConfig"
    domainConfig()
 else:
    root = "domainRuntime"
    domainRuntime()

 cd ('/')
 DOMAIN_NAME= get('Name')
 cd (argv[2])
 cd (DOMAIN_NAME)
 cd (argv[3])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:])
 lengthPathParamsRoot= len (argv[2:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
 
 obj = {}
  
 for server in myservers:
    xy_server = java.lang.String(server)
       
    cd (xy_server)
    name= 'WorkManager Name'
    wmVal= get('Name') 
    wmInfo=  name,  wmVal
    wmInfoList1 = list(wmInfo)
    code_atribute.append(wmInfoList1[0])
    
      
    cd ('MaxThreadsConstraint') 
    myMaxThreadsConstraint = ls(returnMap='true')
    
    if len (myMaxThreadsConstraint) > 0:
       for maxThread in   myMaxThreadsConstraint: 
          maxConstraint= java.lang.String(maxThread)
          cd (maxConstraint)
          attributeName= 'MaxThreadsConstraint Name'
          attributeNameValue = str(maxConstraint)
          name= 'MaxThreadsConstraint'
          wmVal= str(get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList2 = list(wmInfo)
          wmInfoList22 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList2[0])
          code_atribute.append(wmInfoList22[0])
          cd ('..')
    
    else:
       wmInfoList2 = ['MaxThreadsConstraint', '-']   
       wmInfoList22 =['MaxThreadsConstraint Name', '-']           
    
    cd ('..')



    cd ('MinThreadsConstraint') 
    myMinThreadsConstraint = ls(returnMap='true');
    
    if len (myMinThreadsConstraint) >0 :
       for minThread in   myMinThreadsConstraint: 
          minConstraint= java.lang.String(minThread); 
          cd (minConstraint); 
          attributeName= 'MinThreadsConstraint Name'
          attributeNameValue = str(minConstraint)
          name= 'MinThreadsConstraint'
          wmVal= str( get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList3 = list(wmInfo)
          wmInfoList33 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList3[0])
          code_atribute.append(wmInfoList33[0])
          cd ('..');

    else:
       wmInfoList3 = ['MinThreadsConstraint', '-']   
       wmInfoList33 = ['MinThreadsConstraint Name', '-']

    cd ('..');      



    cd ('Capacity') 
    myCapacityList = ls(returnMap='true')
    
    
    if len (myCapacityList) > 0:
       for valCapacity in   myCapacityList: 
          Capacity_x= java.lang.String(valCapacity)
          cd (Capacity_x); 
          attributeName= 'Capacity Name'
          attributeNameValue = str(Capacity_x)
          name= 'Capacity'
          wmVal= str( get('Count') )
          wmInfo=  name,  wmVal  
          wmInfo= list(wmInfo)
          wmInfoAttrib =  attributeName, attributeNameValue
          wmInfoAttrib = list (wmInfoAttrib)
          wmInfoList4 = list(wmInfo)
          wmInfoList44 = list(wmInfoAttrib)
          code_atribute.append(wmInfoList4[0])
          code_atribute.append(wmInfoList44[0])
          cd ('..');
    
    else:
       wmInfoList4 = ['Capacity', '-']  
       wmInfoList44 =  ['Capacity Name', '-']
    
    cd ('..');
      
    
    wmInfoList = wmInfoList1 , wmInfoList2, wmInfoList22 ,wmInfoList3 ,wmInfoList33 ,wmInfoList4, wmInfoList44
    wmInfoList = list (wmInfoList)     
    obj[server] = wmInfoList 
         
    cd ('..')

 
    
 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]];
 code_atribute_unique_sort = code_atribute_unique.sort();

 
 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_1234PLMOKN" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"
 
 print >>f,  " </form> "
 
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark">"""
 print >>f, "<tr>"
 print >>f, "<th>WorkManager Name</th>"

 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f, zxc
    print >>f, "</th>"

 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 for key in sortare(obj.iterkeys()):
 
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
 
    a = obj[key]

    for zxc in code_atribute_unique:
  
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)
          
          try:
             print >> f, "<td>"
             print >> f, " ".join([str(x) for x in ase[0][1::]])
             print >> f, "</td>"

          except:
             print >> f, "<td>"
             print >> f, "NO Value"
             print >> f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
 
    print >>f, "</tr>"
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Main_Horizontal" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')

#getValuesHorizontalWMFullOverview  - STOP
# ----------------------------------------------





# ----------------------------------------------
# listJDBCDBPropertiesCheck

def listJDBCDBPropertiesCheck (*argv):

 domainConfig()
 cd ('/')
 DOMAIN_NAME = get('Name')
 abstractPath = ['domainConfig' ,'JDBCSystemResources','Resource','JDBCDriverParams','Properties','Properties', argv[1]]
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(abstractPath)
 
 try:
    cd ('JDBCSystemResources')
    mydatasources = ls(returnMap='true')


    if len (mydatasources) > 0 :    
       i = 0
       for datasource in mydatasources:
          xy_datasource = java.lang.String(datasource)
          cd (xy_datasource)
          cd ('Resource')
          cd (xy_datasource)
          cd ('JDBCDriverParams')
          cd (xy_datasource)
          cd ('Properties')
          cd (xy_datasource)
          cd ('Properties')
          
          myProperties = ls(returnMap='true')
    

          property = [str(x) for x in myProperties]

          

          if argv[1] in myProperties: 
             i += 1
         
          
          cd ('../../../../../../../../')
          
       if i > 0:
          listJDBCDBPropertiesHorizontal(*argv)

       else: 
          # this covers all the other Properties not found
          print >>f, """<p> <kbd> wlst:""" + genericPath + """</kbd> </p> """
          print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>  """ + argv[1] + """  not found in the """ + DOMAIN_NAME + """ domain.</h3></p></div></div>"""

       if argv[1] == 'oracle.net.READ_TIMEOUT' or argv[1] == 'oracle.jdbc.ReadTimeout':
          print >>f, "<p> </br> </p>"
          print >>f, """<p> <kbd> Info </kbd> </p> """
          print >>f, "<table class=\"table table-sm table-hover table-dark sortable\" >"
          print >>f, """<thead class="thead-dark" >"""
          print >>f, "<tr>"
          print >>f, "<th>Database - JDBC driver	</th>"
          print >>f, "<th>Property name	</th>"
          print >>f, "<th> Unit </th>"
          print >>f, "</tr>"
          print >>f,"</thead>"
          print >>f, "<tbody>"
          print >>f, "<tr>"
          print >>f, "<td> Oracle, Thin driver, v10.1.0.5+ </td>"
          print >>f, "<td> oracle.jdbc.ReadTimeout</td>"
          print >>f, "<td> ms </td>"
          print >>f, "</tr>"
          print >>f, "<tr>"
          print >>f, "<td> Oracle, Thin driver, older </td>"
          print >>f, "<td> oracle.net.READ_TIMEOUT </td>"
          print >>f, "<td> ms </td>"
          print >>f, "</tr>"
          print >>f, "</tbody></table>"    

    else:
       # this covers only the 'user' - since all Data Sources have an user.
       print >>f, """<p> <kbd> wlst:""" + genericPath + """</kbd> </p> """
       print >>f, """ <div class="card"><div class="card-body"><h4 class="card-title">  <i class="far fa-eye-slash"></i></h4><p class="card-text"> <h3>No Data Sources found in the """ + DOMAIN_NAME + """ domain.</h3></p></div></div>"""

 except:
    print >>f, """<p> <kbd> wlst:""" + genericPath + """</kbd> </p> """
    print >>f, """ <div class="card"> <div class="card-body"><h4 class="card-title"><i class="fas fa-exclamation-triangle"></i></h4><p class="card-text"> <h3>The MBean is not part of the """ + DOMAIN_NAME +   """ domain or No such resource found for this domain.   </br>  Review the MBean name/path or upgrade to the latest FMW release.</h3></p></div></div>"""
 
 return ('')

# ----------------------------------------------



# ----------------------------------------------
# listJDBCDBPropertiesHorizontal - START 

def listJDBCDBPropertiesHorizontal(*argv):
  
 
 domainConfig()
 cd ('/')
 DOMAIN_NAME = get('Name')
 cd ('JDBCSystemResources')
 mydatasources = ls(returnMap='true')
 code_atribute = []
 abstractPath = ['domainConfig' ,'JDBCSystemResources','Resource','JDBCDriverParams','Properties','Properties', argv[1]]
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(abstractPath)
 id_table_New = argv[0] + "_1234QWERTY098765"
 obj = {}
 

 
 for datasource in mydatasources:
    xy_datasource = java.lang.String(datasource)
    cd (xy_datasource)
    cd ('Resource')
    cd (xy_datasource)
    cd ('JDBCDriverParams')
    cd (xy_datasource)
    cd ('Properties')
    cd (xy_datasource)
    cd ('Properties')
    myProperties = ls(returnMap='true')
  
    
    if argv[1] in myProperties: 
       cd (argv[1])

       a = ls ('a')
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
       obj[datasource] = b
      
       for iteme in b: 
          h = iteme[0]
          if h == "Value":
             code_atribute.append(h)
                   
       cd ('..')
         
    
    else: 
       pass
          
    cd ('../../../../../../../../')
    
        
 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()

 print >>f, """<p> <kbd> wlst:""" + genericPath + """</kbd> </p> """
 
 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """
  
 print >>f, "id=\" " + id_table_New + "852582BCZXCV02105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table_New  +  "\', \'." + id_table_New + "\', this.value)\">"
 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table_New + "\">"
 print >>f, """<thead class="thead-dark" >"""
 print >>f, "<tr>"
 print >>f, "<th>Data Source Name</th>"
 
 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f,  argv[1] + "  "  +zxc
    print >>f, "</th>"


 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 for key in sortare(obj.iterkeys()):
    print >>f, "<tr class=\"" + id_table_New + "\">"
    print >>f, "<td>"
    print >>f, key
    print >>f, "</td>"
   
    a = obj[key]

    for zxc in code_atribute_unique:
       if filter(lambda x:x[0]==zxc,a):
          ase = filter(lambda x:x[0]== zxc,a)

          try:
             print >> f, "<td>"
             #print >> f, ' '.join(ase[0][1:])
             print >> f, " ".join([str(x) for x in ase[0][1::]])
             print >> f, "</td>"

          except:
             print >> f, "<td>"
             print >> f, "NO Value"
             print >> f, "</td>"

       else: 
          print >>f, "<td>"
          print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
          print >>f, "</td>"
 
    print >>f, "</tr>"

 
 
 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table_New + "', '" + "DataSource"  +  argv[1] + "_Info" + "')\"> Export To XLS </button> </p> </br>"

 
 
 return ('')


# listJDBCDBPropertiesHorizontal - STOP 
# --------------------------------------------------



# ---------------------------------------------
# listRuntimeValuesVerticalCheck
# e.g. listRuntimeValuesVerticalCheck ("id_1234" , "domainRuntime", "ServerRuntimes", "JDBCServiceRuntime", "JDBCDataSourceRuntimeMBeans" )
# for now the function is focusing on JDBC-related resources. 

def listRuntimeValuesVerticalCheck (*argv):
 
 root = "domainRuntime"
 # The domainConfig() used here just to check if resources are available.
 domainConfig()

 cd ('/')
 DomainNameIntro = get('Name')

 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])

 
 try: 
   listRuntimeValuesVertical(*argv)
          
 except: 
    print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
    print >>f, genericPath
    print >>f, "</kbd>"
    print >>f, "<p> </p>"
    print >>f, """ <div class="card"> <div class="card-body"><h4 class="card-title"><i class="fas fa-exclamation-triangle"></i></h4><p class="card-text"> <h3>The MBean <font color= "#f29111">"""  +  '/'.join(argv[2:4])  + """ </font> from """ + DomainNameIntro +   """ domain raised some issues.   </br>  Review the MBean name/path or check if the resource is available | the target defined | server is running.</h3></p></div></div>"""
    
 return ('')

# ----------------------------------------------




# ----------------------------------------------
# listRuntimeValuesVertical  - START 


def listRuntimeValuesVertical(*argv):
 
 root = "domainRuntime" 
 domainRuntime()
 
 cd ('/')
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:]) 
 lengthPathParamsRoot= len (argv[3:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
     
 
 resource_list_list= []

 for server in myservers:
    xy_server = java.lang.String(server)
       
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:-1]) + '/' + server
    serverPath= serverPath + '/' + argv[-1] + '/'
 
    cd (xy_server)
    cd (serverPath)
         
    resource_list = ls(returnMap='true')
       
    for resource_x in resource_list: 
       xy_resource = java.lang.String(resource_x)
       cd (xy_resource)
                 
       a = ls ('a'); 
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]];
      
       for iteme in b: 
          h = iteme[0]; 
          code_atribute.append(h);
       cd ('..')
            
   
    cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot))
    
 obj = {}
 server_dic={}  
 servers_list= {}

 for server in myservers:
    xy_server = java.lang.String(server)
   
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:-1]) + '/' + server
    serverPath= serverPath + '/' + argv[-1] + '/'

    server_dic[server] = {}
    
    cd (xy_server)
    cd (serverPath)
       
    resource_list = ls(returnMap='true')
    resource_len = len (resource_list) 
   
   
    for resource_x in resource_list: 
       xy_resource = java.lang.String(resource_x)
       
       cd (xy_resource)
       
       a = ls ('a')
       b =  [s.split() for s in re.split("-r-- | \n ",a)[1:]]
              
       server_dic[server][resource_x] = b
       
       cd ('..')

   
    cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot)) 
     
  
 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]];
 code_atribute_unique_sort = code_atribute_unique.sort();

 print >>f, """<p> <kbd> wlst:""" + root + """ <i class="fas fa-angle-double-right"></i>"""
  
 print >>f, genericPath
 print >>f, "</kbd>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_123QSCFTHM1234" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"

 print >>f,  " </form> "

 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""
 print >>f, "<tr>"
 print >>f, """ <th class="runtimeth" rowspan="2">Attribute</th>"""
     
 sorted_servers=sortare(server_dic.keys()) 

 all_Servers ={} 

 for k, v in sortare(server_dic.items()):
    for k1, v1 in v.items():
       all_Servers [k]= sortare(v.keys()) 


 for x in sorted_servers:
    if all_Servers[x]:
       resource_len = len (all_Servers[x])
       print >>f, """ <th class="colspan_color" colspan=" """
       print >>f, resource_len
       print >>f, """ "> """
       print >>f, x
       print >>f, "</th>"
       
    else:
        pass

  
 print >>f, "</tr>"
 print >>f, "<tr>"

 
 for x in sorted_servers:
    if all_Servers[x]:
       for resource_name in all_Servers[x]: 
          print >>f, "<th>"
          print >>f, resource_name
          print >>f, "</th>"

    else:
       pass
  
 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"  


 for zxc in code_atribute_unique:
    print >>f, "<tr class=\"" +argv[0]+ "\">"
    print >>f, "<td>"
    print >>f, zxc
    print >>f, "</td>"
 
    for x in sorted_servers:
       if all_Servers[x]:
          for resource_name in all_Servers[x]: 
             attribute_value= server_dic[x][resource_name]         
            
             if filter(lambda x:x[0]==zxc,attribute_value):
                ase = filter(lambda x:x[0]== zxc,attribute_value)
                                  
                try:
                   print >>f, "<td>"
                   print >>f, ' '.join(ase[0][1:])   
                   print >>f, "</td>"       
                 
                except:
                   print >>f, "<td>"
                   print >>f, "NO Value"
                   print >>f, "</td>"
             else: 
                print >>f, "<td>"
                print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
                print >>f, "</td>"
    
    print >>f, "</tr>"

 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Vertical" + "')\"> Export To XLS </button> </p> </br>"
 
 return ('')


#  listRuntimeValuesVertical - STOP
# --------------------------------------------------





# ---------------------------------------------
# listRuntimeValuesHorizontalCheck
# e.g. listRuntimeValuesHorizontalCheck ("id_273333343111178963" , "domainRuntime", "ServerRuntimes", "JDBCServiceRuntime", "JDBCDataSourceRuntimeMBeans" )
# for now the function is focusing on JDBC-related resources. 

def listRuntimeValuesHorizontalCheck (*argv):

 root = "domainRuntime"
 # The domainConfig() used here just to check if resources are available.
 domainConfig()

 cd ('/')
 DomainNameIntro = get('Name')

 try: 
    listRuntimeValuesHorizontal(*argv)
     
 except: 
    pass
 
 return ('')

# ----------------------------------------------




# ----------------------------------------------
# listRuntimeValuesHorizontal  - START 


def listRuntimeValuesHorizontal(*argv):
 
 root = "domainRuntime" 
 domainRuntime()
 
 cd ('/')
 cd (argv[2])
 myservers = ls(returnMap='true')
 code_atribute = []
 lengthPathParams = len (argv[2:])
 lengthPathParamsNonRoot= len (argv[3:]) 
 lengthPathParamsRoot= len (argv[3:])
 genericPath = ' <i class=\"fas fa-angle-double-right\"></i> '.join(argv[2:])
     
 
 resource_list_list= []

 for server in myservers:
    xy_server = java.lang.String(server)
       
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:-1]) + '/' + server
    serverPath= serverPath + '/' + argv[-1] + '/'
 
    cd (xy_server)
    cd (serverPath)
         
    resource_list = ls(returnMap='true')
       
    for resource_x in resource_list: 
       xy_resource = java.lang.String(resource_x)
       cd (xy_resource)
                 
       a = ls ('a')
       b = [s.split() for s in re.split("-r-- | \n ",a)[1:]]
      
       for iteme in b: 
          h = iteme[0] 
          code_atribute.append(h)
       cd ('..')
            
   
    cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot))
    
 obj = {}
 server_dic={}  
 servers_list= {}

 for server in myservers:
    xy_server = java.lang.String(server)
   
    serverPath =  '/' + server + '/' 
    serverPath=    serverPath.join(argv[3:-1]) + '/' + server
    serverPath= serverPath + '/' + argv[-1] + '/'

    server_dic[server] = {}
    
    cd (xy_server)
    cd (serverPath)
       
    resource_list = ls(returnMap='true')
    resource_len = len (resource_list) 
   
   
    for resource_x in resource_list: 
       xy_resource = java.lang.String(resource_x)
       cd (xy_resource)
              
       a = ls ('a')
       b =  [s.split() for s in re.split("-r-- | \n ",a)[1:]]
              
       server_dic[server][resource_x] = b
       
       cd ('..')

   
    cd ('../'* (lengthPathParamsNonRoot + lengthPathParamsRoot)) 
     
  
 code_atribute_unique= [ii for n,ii in enumerate(code_atribute) if ii not in code_atribute[:n]]
 code_atribute_unique_sort = code_atribute_unique.sort()


 print >>f, "</p>"
 print >>f, "<hr>"
 print >>f, "</p>"

 print >>f, """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """

 print >>f, "id=\"" + argv[0]+ "_QWERTPOIUYT12340987" + "\" oninput=\"w3.filterHTML(\'#" +argv[0] +  "\', \'." + argv[0] + "\', this.value)\">"
 print >>f,  " </form> "
  
 print >>f, "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + argv[0] + "\">"
 print >>f, """<thead class="thead-dark" \>"""

 print >>f, "<tr>"
 print >>f, "<th>WLS Server</th>"
 print >>f, "<th>Resource Name</th>"

 for zxc in code_atribute_unique:
    print >>f, "<th>"
    print >>f, zxc
    print >>f, "</th>"

 print >>f, "</tr>"
 print >>f,"</thead>"
 print >>f, "<tbody>"

 sorted_servers=sortare(server_dic.keys()) 

 all_Servers ={} 

 for k, v in sortare(server_dic.items()):
    for k1, v1 in v.items():
       all_Servers [k]= sortare(v.keys()) 


 for x in sorted_servers:
    if all_Servers[x]:
      
       for resource_name in all_Servers[x]: 
          print >>f, "<tr class=\"" +argv[0]+ "\">"
          print >>f, """ <td   """
          print >>f, """ >"""
          print >>f, x
          print >>f, "</td>"
          print >>f, "<td>"
          print >>f, resource_name
          print >>f, "</td>" 
               
          attribute_value= server_dic[x][resource_name]    

          for zxc in code_atribute_unique:
            
             if filter(lambda x:x[0]==zxc,attribute_value):
                ase = filter(lambda x:x[0]== zxc,attribute_value)
                                  
                try:
                   print >>f, "<td>"
                   print >>f, ' '.join(ase[0][1:])
                   print >>f, "</td>"       
                 
                except:
                   print >>f, "<td>"
                   print >>f, "NO Value"
                   print >>f, "</td>"
             
             else: 
                print >>f, "<td>"
                print >>f, """ <i class="far fa-times-circle"  data-placement="right"  data-trigger="hover" data-toggle="popover"  data-content="No such Attribute &#9940; "></i> """
                print >>f, "</td>"
       
       
          print >>f, "</tr>"
    
    else:
       print >>f, """  <i class="fas fa-question-circle"></i> UNKNOWN ERROR """


 print >>f, "</tbody></table>"
 print >>f, "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + argv[0] + "', '" + str(argv[-2]) + "_" + argv[-1] + "_Horizontal" + "')\"> Export To XLS </button> </p> </br>"

 return ('')

# listRuntimeValuesHorizontal  - STOP
# --------------------------------------------------
