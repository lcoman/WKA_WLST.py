#!/usr/bin/env sh
import os
import platform
import sys

OUTPUT_FILE_PATH = os.environ["WLST_OUTPUT_PATH"]
OUTPUT_FILE = os.environ["WLST_OUTPUT_FILE"]
cwd = os.chdir(OUTPUT_FILE_PATH)
pathFiles= os.listdir(cwd)

for x in pathFiles:
 if ".html" in x and OUTPUT_FILE in x:
    #f= open(x,"a")
    f= open(x,"a" ,  encoding='utf-8')

# --------------------------------------------------
      



# --------------------------------------------------
# Environment Variables
# printenv


def EnvironmentVariablesTable(id_table):
 envVar= os.popen('printenv').readlines()

 f.write (  """<p> <kbd> Environment Variables  <i class=\"fas fa-chevron-circle-right\"></i>   printenv  </kbd> </p>""" )
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_12121ABC0ZXCV2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>OS resource </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")

 for x in envVar:
    var= x.split('=', 1)
    f.write (  "<tr class=\"" +  id_table  + "\">" )
    f.write (  "<td>")
    f.write (  var[0])
    f.write (  "</td>")
    f.write (  "<td>")
    f.write (  var[1])
    f.write (  "</td>")
    f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Environment Variables" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------




# --------------------------------------------------
# OS Overview 

def get_platform():
  
 try: 
   distribution = platform.linux_distribution()
   machine = str(platform.machine())
   node = platform.node()
   processor = str(platform.processor())
   release = str(platform.release())
   system = str(platform.system())
   version = str(platform.version())
   platform_info = platform.platform()
   platform_info = platform_info.split ('-')
   platformDetails =  " ".join(platform_info)
   
   hostFQN= os.popen('hostname --fqdn').readlines() 
   hostFQN = hostFQN[0].strip('\n')
   hostnameI= os.popen('hostname -i').readlines() 
   hostnameI = hostnameI[0].strip('\n')
   header = "Node: " + node + " / " + " FQDN: " + hostFQN +  " / " + " Hostname: "  + hostnameI
       

   f.write ("""   
    
          <div class="card">
         <div class="card-header"> <b> """ ) 
   f.write ( header )
   f.write ("""  
         </b>
         </div>
         <ul class="list-group list-group-flush">
               <li class="list-group-item"><b>  Distribution:</b> """ ) 
     
   x = ", ".join(distribution)
   f.write (x)

   f.write ("""</li>
               <li class="list-group-item"> <b> Machine:</b> """ )
   f.write ( machine )
   f.write ("""</li>
               <li class="list-group-item"><b> Node:</b> """ )
   f.write ( node )
   f.write ("""           </li>
              <li class="list-group-item"><b>Architecture:</b> """ )
   f.write (processor  )
   f.write ("""</li>
             <li class="list-group-item"><b> OS release (kernel):</b> """ )
   f.write (release  )
   f.write (""" </li>
             <li class="list-group-item"> <b> System:</b> """ )
   f.write (system  )
   f.write (""" </li>
             <li class="list-group-item"> <b> Version:</b> """ )
   f.write (version  )
              
   f.write (""" </li>
             <li class="list-group-item"> <b> Platform info:</b> """ )
   f.write (platformDetails  )
   f.write ("""             </li>
           </ul>
         </div> </p>

      """ )
     
 except Exception as e: print(e)
 
 return ('')        

# --------------------------------------------------         



# --------------------------------------------------
# CPU Information
# cat /proc/cpuinfo

def cpuInfo(id_table):

 cpuinfo = os.popen('cat /proc/cpuinfo').readlines()
 found = False

 
 f.write (  """<p> <kbd> CPU Information <i class=\"fas fa-chevron-circle-right\"></i>  cat /proc/cpuinfo   </kbd> </p>""")
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_02144QWER2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>OS resource </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")
 procNumber=1

 for x in cpuinfo:
    a= x.split('\t:')
    a= x.split('\t')
    a= x.split(':')
    
    if "processor" in a[0]:
        found= True
        f.write (  "<tr>")
        f.write (  "<td colspan=\"2\" class =\"rowspan_2\">")
        message= "Processor #" + str(procNumber)
        f.write (message)
        procNumber += 1
        f.write (  "</td>")
        f.write (  "<tr>")
    else:
       pass    
   
    if found:
       
       if len (a[0]) > 1:
          f.write (  "<tr class=\"" +  id_table  + "\">")
          f.write (  "<td>")
          f.write (  a[0])
          f.write (  "</td>")
          f.write (  "<td>")
             
          try:
             f.write (  a[1])
          except:
             f.write (  " ")
                
          f.write (  "</td>")
          f.write (  "</tr>")

       else:
          pass
                 
    else:
       pass
    
 f.write (  "</tbody></table>")
 f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "CPU Information" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------



# --------------------------------------------------
# System Kernel Settings 
# /sbin/sysctl -a

def systemKernelSettings(id_table):
 kernelSettings = os.popen('/sbin/sysctl -a').readlines()

 
 f.write (  """<p> <kbd> System Kernel Settings  <i class=\"fas fa-chevron-circle-right\"></i>  /sbin/sysctl -a </kbd> </p>""")
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_789456ABCD" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")

 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>OS resource </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")

 for x in kernelSettings:
    a= x.split(' = ')
    c= a[1].split(' ')
    
    f.write (  "<tr class=\"" +  id_table  + "\">")
    f.write (  "<td>")
    f.write (  a[0])
    f.write (  "</td>")
    f.write (  "<td>")
    f.write (  a[1])
    
    f.write (  "</td>")
    
 
 f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "System Kernel Settings" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------







# --------------------------------------------------
# Disk Space
# df -h

def dfDiskSpace (id_table):
 diskSpace = os.popen('df -h').readlines()
 

 f.write (  """<p> <kbd> Disk Space <i class=\"fas fa-chevron-circle-right\"></i>  df -h </kbd> </p>""")
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_AQZWSX01230" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")

 
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 
 a = diskSpace[0].split()

 i=0    
 while i<5:
    f.write (  "<th>")
    f.write (  a[i])
    i+=1
    f.write (  "</th>")

 f.write (  "<th>")
 f.write (  " ".join(a[5:]))
 f.write (  "</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")
 
 
 for x in diskSpace[1:]:
    f.write (  "<tr class=\"" +  id_table  + "\">")
    
    a = x.split()
    for b in a: 
       f.write (  "<td>")
    
       f.write (  b)
       f.write (  "</td>")

    f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Disk Space" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------



# --------------------------------------------------
# Disk Space
# df -ah

def dfDiskSpace2 (id_table):
 diskSpace = os.popen('df -ah').readlines()
 

 f.write (  """<p> <kbd> Disk Space <i class=\"fas fa-chevron-circle-right\"></i>  df -ah </kbd> </p>""")
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_AQZWSX01230" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")

 
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 
 a = diskSpace[0].split()

 i=0    
 while i<5:
    f.write (  "<th>")
    f.write (  a[i])
    i+=1
    f.write (  "</th>")

 f.write (  "<th>")
 f.write (  " ".join(a[5:]))
 f.write (  "</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")
 
 
 for x in diskSpace[1:]:
    f.write (  "<tr class=\"" +  id_table  + "\">")
    
    a = x.split()
    for b in a: 
       f.write (  "<td>")
    
       f.write (  b)
       f.write (  "</td>")

    f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Disk Space2" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

 # --------------------------------------------------






# --------------------------------------------------
# Memory utilization 
# cat /proc/meminfo

def osMemory (id_table):
 catMemory = os.popen('cat /proc/meminfo').readlines()

 f.write (  """<p> <kbd> Memory utilization <i class=\"fas fa-chevron-circle-right\"></i> cat /proc/meminfo </kbd> </p>""")

 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_0987654BCZXCV2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>Memory  Parameters </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")

 for x in catMemory:
    var= x.split(':', 1)
    f.write (  "<tr class=\"" +  id_table  + "\">")
    f.write (  "<td>")
    f.write (  var[0])
    f.write (  "</td>")
    f.write (  "<td>")
    f.write (  var[1])
    
    var = [x.strip(' ') for x in var]

    if " kB" in var[1]:
        var= var[1].split(' kB')
        try: 
          if int(var[0]) > 0:
             
             mem_mb = round(int(var[0])/1024)
             if mem_mb > 0 :
                f.write (  "&nbsp; [" )
                f.write (  str(int(mem_mb)) )
                f.write (  " MB]")
               
        except:
          pass
             


    f.write (  "</td>")
    f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p> <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Memory utilization" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------




# --------------------------------------------------
# Ulimit  
# /bin/bash -f -c "ulimit -a"

def ulimit (id_table):
 ulimitInfo = os.popen('/bin/bash -f -c "ulimit -a" ').readlines()

 f.write (  """<p> <kbd> Ulimit <i class=\"fas fa-chevron-circle-right\"></i>  /bin/bash -f -c "ulimit -a" </kbd> </p>""")

 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_5895670BCZXCV2" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>Ulimit  Parameters </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")

 for x in ulimitInfo:
    var= x.split(')', 1)
    f.write (  "<tr class=\"" +  id_table  + "\">")
    f.write (  "<td>")
    f.write (  var[0] + ")")
    f.write (  "</td>")
    f.write (  "<td>")
    f.write (  var[1])
    f.write (  "</td>")
    f.write (  "</tr>")

 f.write (  "</tbody></table>")
 f.write (  "<p> <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Ulimit" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------



# --------------------------------------------------
# Java processes  
# ps -ef | grep [j]ava

def osJava (id_table):
 javaProc = os.popen('ps -ef | grep [j]ava').readlines()

 f.write (  """<p> <kbd> Java processes  <i class=\"fas fa-chevron-circle-right\"></i>  ps -ef | grep [j]ava </kbd> </p>""")

 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_956852649731ZXC01V2" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")

 f.write (  " </form> ")
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th> Java process # </th>")
 f.write (  "<th>Value</th>")
 f.write (  "</tr>")
 f.write ( "</thead>")
 f.write (  "<tbody>")

 len_javaProc = len(javaProc)
 i =0 

 while i< len_javaProc:
    f.write (  "<tr class=\"" +  id_table  + "\">" )
    f.write (  "<td>")
    f.write (  "# " + str(i) )
    f.write (  "</td>")
    f.write (  "<td>")
    a = ''.join(javaProc[i]).split()
    for x in a:
       f.write (x + "<br>")
    f.write (  "</td>")
    f.write (  "</tr>")
    i +=1

 f.write (  "</tbody></table>")
 f.write (  "<p> <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Java_processes" + "')\"> Export To XLS </button> </p> </br>")
 return ('')

# --------------------------------------------------