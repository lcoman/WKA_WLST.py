import os
import platform
import sys
import csv
from csv import DictReader


OUTPUT_FILE_PATH = os.environ["WLST_OUTPUT_PATH"]
OUTPUT_FILE = os.environ["WLST_OUTPUT_FILE"]
cwd = os.chdir(OUTPUT_FILE_PATH)
pathFiles= os.listdir(cwd)

for x in pathFiles:
 if ".html" in x and OUTPUT_FILE in x:
    f= open(x,"a" ,  encoding='utf-8')
      

# --------------------------------------------------



# --------------------------------------------------
def EnvironmentVariablesTable(id_table):
 
 envVar =  os.popen('set').readlines()
 
 f.write (  """<p> <kbd> Environment Variables  <i class=\"fas fa-chevron-circle-right\"></i>   set  </kbd> </p>""" )
 f.write (  """ <form class="form-inline md-form form-sm mt-0">
                    <i class="fas fa-search" aria-hidden="true"></i>
                    <input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
 f.write (  "id=\" " + id_table + "_12121ABCZXCV2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
 f.write (   " </form> ")
 f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
 f.write (  "<thead class=\"thead-dark \">")
 f.write (  "<tr>")
 f.write (  "<th>Environment Variable </th>")
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
def get_systeminfo(id_table):
  
 try: 
  f.write (  """<p> <kbd> System Information <i class=\"fas fa-chevron-circle-right\"></i>  systeminfo /fo csv   </kbd> </p>""")
  f.write (  """ <form class="form-inline md-form form-sm mt-0"><i class="fas fa-search" aria-hidden="true"></i><input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
  f.write (  "id=\" " + id_table + "_0216244QWER2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
  f.write (   " </form> ")
    
  system_info= os.popen('systeminfo /fo csv').readlines()
  data = csv.DictReader(system_info)
  fieldname = data.fieldnames
  
  
  
  f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
  f.write (  "<thead class=\"thead-dark \">")
  f.write (  "<tr>")
  f.write (  "<th>System Info Item </th>")
  f.write (  "<th>Value</th>")
  f.write (  "</tr>")
  f.write ( "</thead>")
  f.write (  "<tbody>")
 
  for name in fieldname: 
   f.write (  "<tr class=\"" +  id_table  + "\">")
   
   f.write (  "<td>")
   f.write (  name)
   f.write (  "</td>")
   data = csv.DictReader(system_info)
   
   for row in data:
    if "Hotfix" in row[name]:
     y = row[name]
     y= y.split(',')
     f.write (  "<td>")
     for a in y:
      f.write (a)
      f.write ("</br>")
     f.write (  "</td>")
    
    elif "Network" in row[name]:
     y = row[name]
     y= y.split(',')
     f.write (  "<td>")
     for a in y:
      if "[" in a:
       f.write ("<span>&#8226; </span>")
       f.write (a)
      else:
       f.write (a)
      f.write ("</br>")
     f.write (  "</td>")
    
    
    else:
     f.write (  "<td>")
     f.write (  row[name])
     f.write (  "</td>")
   
   f.write (  "</tr>")

  f.write (  "</tbody></table>")
  f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Systeminfo" + "')\"> Export To XLS </button> </p> </br>")
 
 
                
 except Exception as e: f.write(e)
 
 return ('')   

# --------------------------------------------------







# --------------------------------------------------

def get_DiskSpace_wmic(id_table):
  
 try: 
  f.write (  """<p> <kbd> Disk Space <i class=\"fas fa-chevron-circle-right\"></i>  wmic logicaldisk get caption, size, freespace </kbd> </p>""")
  f.write (  """ <form class="form-inline md-form form-sm mt-0"><i class="fas fa-search" aria-hidden="true"></i><input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
  f.write (  "id=\" " + id_table + "_8765444QWER9805" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
  f.write (   " </form> ")
    
  DiskSpace_wmic= os.popen('wmic logicaldisk get caption, size, freespace').readlines()
  data = csv.DictReader(DiskSpace_wmic)
  fieldname = data.fieldnames
  
  
  
  f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
  f.write (  "<thead class=\"thead-dark \">")
  f.write (  "<tr>")
  
  for name in fieldname:
   line = name.split()
   for b in line:   
    f.write (  "<th>")
    f.write ( b)
    f.write ( "</th>")
   
  f.write (  "</tr>")
  f.write ( "</thead>")
  f.write (  "<tbody>")
 
  for name in fieldname: 
   
   data = csv.DictReader(DiskSpace_wmic)
   for row in data:
     lrd=row[name].split(" ")
     lrd =  [s for s in lrd if s != '']
     
     if len(lrd) == 3:
      f.write (  "<tr class=\"" +  id_table  + "\">")
      for abc in lrd:
       f.write (  "<td>")
       f.write (  abc)
       f.write (  "</td>")
      f.write (  "</tr>")
     else:
      pass;





  f.write (  "</tbody></table>")
  f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Disk Space" + "')\"> Export To XLS </button> </p> </br>")
 
 
                
 except Exception as e: f.write(e)
 
 return ('')   

# --------------------------------------------------






# --------------------------------------------------

def get_systeminfo_memory(id_table):
  
 try: 
  f.write (  """<p> <kbd> Memory Information <i class=\"fas fa-chevron-circle-right\"></i>  systeminfo /fo csv <i class="fas fa-caret-right"></i>  Memory  </kbd> </p>""")
  f.write (  """ <form class="form-inline md-form form-sm mt-0"><i class="fas fa-search" aria-hidden="true"></i><input class="form-control form-control-sm ml-3 w-75" type="text" placeholder="Search" aria-label="Search"  """)
  
  f.write (  "id=\" " + id_table + "_0987567321QWER2105" + "  \" oninput=\"w3.filterHTML(\'#"  + id_table  +  "\', \'." + id_table + "\', this.value)\">")
  f.write (   " </form> ")
    
  system_info= os.popen('systeminfo /fo csv').readlines()
  data = csv.DictReader(system_info)
  fieldname = data.fieldnames
  
  
  
  f.write (  "<table class=\"table table-sm table-hover table-dark sortable\"  id=\"" + id_table + "\">")
  f.write (  "<thead class=\"thead-dark \">")
  f.write (  "<tr>")
  f.write (  "<th>Memory Info Item </th>")
  f.write (  "<th>Value</th>")
  f.write (  "</tr>")
  f.write ( "</thead>")
  f.write (  "<tbody>")
 
  for name in fieldname: 
   if "Memory" in name:
     f.write (  "<tr class=\"" +  id_table  + "\">")
     f.write (  "<td>")
     f.write (  name)
     f.write (  "</td>")
     data = csv.DictReader(system_info)
     for row in data:
      f.write (  "<td>")
      f.write (  row[name])
      f.write (  "</td>")
     f.write (  "</tr>") 
     
     
   else:
     pass
   
    

  f.write (  "</tbody></table>")
  f.write (  "<p>  <button type=\"button\" class=\"btn btn-blue-grey\"   onclick=\"exportTableToExcel('" + id_table + "', '" + "Memory Info" + "')\"> Export To XLS </button> </p> </br>")
 
 
                
 except Exception as e: f.write(e)
 
 return ('')   

# --------------------------------------------------