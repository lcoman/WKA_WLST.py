from Windows_OS_Details import *
import datetime;
import os
import platform
import sys
from csv import DictReader
 
# --------------------------------------------------




f.write (  """

<!-- **********************  -->

<div class="tab-pane fade" id="OS" role="tabpanel" aria-labelledby="OS-tab">
        
  

 <!--  start sub OS tabs -->

 <div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">OS</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-EnvironmentVariables-tab" data-toggle="pill" href="#v-pills-EnvironmentVariables" role="tab" aria-controls="v-pills-EnvironmentVariables" aria-selected="true">  Environment Variables</a>
      <a class="nav-link" id="v-pills-systeminfo-tab" data-toggle="pill" href="#v-pills-systeminfo" role="tab" aria-controls="v-pills-systeminfo" aria-selected="false"> System Information</a>
    
       <a class="nav-link" id="v-pills-dfDiskSpace-tab" data-toggle="pill" href="#v-pills-dfDiskSpace" role="tab" aria-controls="v-pills-dfDiskSpace" aria-selected="false"> Disk Space </a>
      <a class="nav-link" id="v-pills-OSMemory-tab" data-toggle="pill" href="#v-pills-OSMemory" role="tab" aria-controls="v-pills-OSMemory" aria-selected="false"> OS Memory </a>
       


    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-EnvironmentVariables" role="tabpanel" aria-labelledby="v-pills-EnvironmentVariables-tab">  """ )
      
      

f.write (  EnvironmentVariablesTable("id_4999980") )
      
f.write (  """      
      
      </div>
      <div class="tab-pane fade" id="v-pills-systeminfo" role="tabpanel" aria-labelledby="v-pills-systeminfo-tab"> """)

f.write (   get_systeminfo("id_64633364000") )
      

      
f.write (  """      
      </div>


 <div class="tab-pane fade" id="v-pills-dfDiskSpace" role="tabpanel" aria-labelledby="v-pills-dfDiskSpace-tab"> """)

f.write (   get_DiskSpace_wmic ("id_6464642222011000"))


      
f.write (  """      
      </div>   


 <div class="tab-pane fade" id="v-pills-OSMemory" role="tabpanel" aria-labelledby="v-pills-OSMemory-tab"> """)

f.write (   get_systeminfo_memory ("id_20119979034500"))
      
      
f.write (  """ 

<p><button type="button" class="btn btn-lg btn-danger" data-trigger="hover" data-placement="left" data-toggle="popover" title="End time:" data-content="   """)

theEnd=datetime.datetime.today().strftime("%A, %d-%B-%Y  [%H:%M]" )

f.write ( theEnd)

f.write (  """
"><i class="fas fa-info-circle"></i></button></p>


      </div>                     
 
    </div>
  </div>
</div>

<!--  stop sub OS  tabs -->

</div>


<!-- **********************  -->


"""  )


print ("Done printing the OS info.... ")


f.write (  """

<!-- THE END   -->


</div>
 

<!-- https://mdbootstrap.com/docs/jquery/navigation/footer  -> Icons demo --> 

<!-- Footer -->
<footer class="page-footer font-small cyan darken-3">

  <!-- Footer Elements -->
  <div class="container">

    <!-- Grid row-->
    <div class="row">

      <!-- Grid column -->
      <div class="col-md-12 py-5">
        <div class="mb-5 flex-center">


          
          <!-- github -->
           <a class="fb-ic" href = "https://github.com/lcoman/WKA_WLST.py" target="_blank" >
            <i class="fab fa-github fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
          </a>
          <!-- blogger -->
          <a class="tw-ic" href = "http://leonardsoa.blogspot.com/2020/04/well-known-attributes-wlstp.html" target="_blank" >
            <i class="fab fa-blogger fa-lg white-text mr-md-5 mr-3 fa-2x"> </i>
          </a>
          
        
		  <!--MDB Logo -->
		   <a  href = "https://mdbootstrap.com" target="_blank" data-toggle="tooltip" data-placement="bottom" title=" UI powered by MDB">
            <img src="https://z9t4u9f6.stackpathcdn.com/wp-content/uploads/2018/06/logo-mdb-jquery-small.png" alt="MDB logo" width="104" height="38" >
            
          </a>
        </div>
      </div>
      <!-- Grid column -->

    </div>
    <!-- Grid row-->

  </div>
  <!-- Footer Elements -->

  <!-- Copyright -->
  <div class="footer-copyright text-center py-3">© 2020 Copyright:
   leonardsoa.blogspot.com

  </div>
  <!-- Copyright -->
  <!-- add pic here  -->
</footer>
<!-- Footer -->

<script src="https://www.w3schools.com/lib/w3.js"></script>

<!-- below JS link to sort tables; based on https://stackoverflow.com/questions/10683712/html-table-sort/51648529 -> answered Apr 17 '19 at 15:13   -->

<script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>

  <script>
    //Get the button
    var mybutton = document.getElementById("myBtn");
    
    // When the user scrolls down 90px from the top of the document, show the button
    window.onscroll = function() {scrollFunction()};
    
    function scrollFunction() {
      if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    }
    
    // When the user clicks on the button, scroll to the top of the document
    function topFunction() {
      document.body.scrollTop = 0;
      document.documentElement.scrollTop = 0;
    }

    // Tooltips Initialization
     $(function () {
     $('[data-toggle="tooltip"]').tooltip()
     })


//export to Excel  start [based on the https://www.codexworld.com/export-html-table-data-to-excel-using-javascript ]

function exportTableToExcel(tableID, filename = ''){
    var downloadLink;
    // var dataType = 'application/vnd.ms-excel';
    var dataType = 'data:application/vnd.ms-excel;charset=utf-8';
    var tableSelect = document.getElementById(tableID);
    var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');
    // https://www.w3schools.com/tags/ref_urlencode.ASP: escape "#"  with "%23"
	  var tableHTML = tableSelect.outerHTML.replace(/#/g, '%23');

    // Specify file name
    filename = filename?filename+'.xls':'excel_data.xls';

    // Create download link element
    downloadLink = document.createElement("a");

    document.body.appendChild(downloadLink);

    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['\ufeff', tableHTML], {
            type: dataType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        // Create a link to the file
        downloadLink.href = 'data:' + dataType + ', ' + tableHTML;

        // Setting the file name
        downloadLink.download = filename;

        //triggering the function
        downloadLink.click();
    }
}
// excel stop     


	  
// https://www.w3schools.com/howto/howto_js_toggle_dark_mode.asp	  
	  function lightModeFunction() {
   var element = document.body;
   element.classList.toggle("light-mode");
}


//Enable popovers everywhere
$(function () {
  $('[data-toggle="popover"]').popover()
})

    </script>   
    
""")




f.write (  """

        </body>

</html>


""")



		





print (".....WKA WLST.py Output printed.")
print (".....DONE! ")
print ("       ")


# --------------------------------------------------


f.close() 
#exit()