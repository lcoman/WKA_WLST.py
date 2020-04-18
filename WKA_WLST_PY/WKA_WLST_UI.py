
import java.util.regex.Matcher
import sys
import java.util.regex.Pattern
import os
import operator
import socket
import re
import time
import datetime
import string
import time
from java.lang import *
from java.util import Date
import weblogic.security.internal.SerializedSystemIni
import weblogic.security.internal.encryption.ClearOrEncryptedService


# **********************************************
try:
   execfile("wka_wlstPy.py")
except:
   print "There has been a problem running wka_wlstPy.py. "
   exit()
# **********************************************


redirect('log_WKA-WLST.log', 'false')

DOMAIN_HOME = os.environ["DOMAIN_HOME"]
OUTPUT_FILE_PATH = os.environ["WLST_OUTPUT_PATH"]
OUTPUT_FILE = os.environ["WLST_OUTPUT_FILE"]

# print("Current Working Directory: " , OUTPUT_FILE_PATH)

print "Connecting to the domain...."
# connect('weblogic','welcome1','t3://localhost:7001')

print "Connection established .... "


# Open the output HTML file and start the update
print "Opening the file .... "
domainConfig()
cd ('/')
Domain_Name = get('Name')


f = open(OUTPUT_FILE_PATH + Domain_Name + '_' + OUTPUT_FILE, 'w')
print "File open.... "
print "Start printing the Well Known Attributes (WKA) WLST.py output.... "

print "Printing the output menu.... "


print >>f, """


<html>
    <meta charset="UTF-8">
    <head>

<!--    https://mdbootstrap.com/md-bootstrap-cdn   -->

<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.10.1/css/mdb.min.css" rel="stylesheet">


<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.10.1/js/mdb.min.js"></script>

<!-- ADD YOUR CUSTOM FAVICON 
<link href= "data:image/png;base64, ACBD1234******"   rel="icon" type="image/x-icon"/> 
-->

<link href= "data:image/png;base64,AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM3NzQC7u7sC5OTkLOrq6n/09PS78fHxyu/v7+nw8PDR7e3tcuLi4iSkpKQBxsbGAAAAAAAAAAAAAAAAAOTk5ADb29sO7e3td/T09OH39/f4/fz8/PH09v/t7/H/8fHx/PHx8e/z8/PZ7e3tbNjY2Avh4eEAAAAAAOLi4gDc3NwR8PDwnvT09Pjv7++r6urrSfTz80vn6u1w5+rtbuvr61jm5uY77e3tnvPz8/Tv7++V2dnZDt/f3wC3t7cD7u7uhvT09Pbr6+uAe3duI0U+MSc9NScWXlZHADEqHQAoIhgIRj8yJGplWyXm5uZ58/Pz8+3t7X6ampoC5+fnQ/T09Ovt7e2c////BWVfVF+uq6XsmJSNrC0lFgo1LR8Jko6GlcTCve2Tj4i8amVbFe3t7Znz8/Pn5ubmPO/v76by8vLn4+PjLq2qpQBUTUEgvru22s7MyPJmYFU7aWNYP8/NyfTNy8fsfnlwjxUMAAnl5eUv8vLy6O/v757y8vLm7+/vssXFxQa4trQA////AI2JgYfc29n/kIyEk46KgpDe3dv/jYmBiwAAAAL///8AycnJB+/v77Xy8vLh8/Pz/+zs7I3///8Az8/PAGReUwBdV0swxsTA6Le0r+yxrqnqzszJ8WVfVD1qZFkA0dHRAP///wDt7e2T8vLy/PPz8//s7OyM////ANLS0gBXUUUAAAAABJmVjZ7k4+H/6uro/6ilnrwjGgoMWFJGANLS0gD///8A7e3tkvLy8v3y8vLp7+/vrr6+vgTS0tIAenVtAHJtYwBqZFlD0tDN8ubl4/+Ae3JuraqkAHJtZADT09MAxsbGBu/v77Py8vLk7+/vrfLy8uPi4uIo5OTkAAAAAABYUkYATUY6JsG/uuXCwLzkVU5CKF5YTAAAAAAA5eXlAOPj4yzy8vLm7+/vp+jo6Ezz8/Pv7OzsjcbHxwQwKBgCamVaSZaSiqLa2db/mJSMngAAAANcVksA2traAMjIyAXs7OyS8/Pz7efn50fKysoH7+/vlvPz8/Pq6upoWlVKCYyHf7LR0Mz/t7Sv3WVfVDdval8A29vbAM3NzQXq6ups8/Pz9O/v75HExMQF5ubmAODg4Brx8fG18/Pz9Ovr64+Zlo9nf3tyZ1xWSy0AAAAAy8vLBOLi4ijs7OyR8/Pz9PHx8bHf398Y5eXlAJOTkwDt7e0A4eHhGu/v75b09PTx9PT04fHy8qrv7++J7e3tjO/v76/y8vLl9PT08O/v75Pg4OAY6+vrAHt7ewAAAAAAAAAAAN3d3QDT09MI6OjoTPDw8K3y8vLq8/Pz/vPz8/7y8vLp7+/vq+jo6EnT09MH3NzcAAAAAAAAAAAA4AcAAMADAACAAQAAAYAAAAAAAAAQAAAAGAgAADgcAAA4HAAAHDgAABw4AAAAMAAAAGAAAICBAADAAwAA4AcAAA=="   rel="icon" type="image/x-icon"/> 

<style>

<!-- Custom CSS --> 

.colspan_color {
color:#3a474e !important;
}

.light-mode .colspan_color {
color:#f29111 !important;
}

.navbar-toggler   {
background-color: #3a474e !important;
}

.light-mode  .navbar-toggler   {
background-color: #4a5b64 !important;
}

.light-mode  .nav-tabs {
    border-bottom: 0px solid transparent;
}

.nav-tabs {
    border-bottom: 0px solid transparent;
}


footer.page-footer .footer-copyright {
background-color: #3a474e !important;
}


.light-mode footer.page-footer .footer-copyright {
background-color: #f3f3f3 !important;
}


.cyan.darken-3 {
    background-color: #3a474e !important;
}


.light-mode .cyan.darken-3 {
background-color: #f3f3f3 !important;
}
	
.light-mode footer.page-footer .footer-copyright 	{
color: #4a5b64 !important;
}
	

::selection {
background:     #8aadbf;
color: white;
}

::-moz-selection {
background:     #8aadbf;
color: white;
}


.custom-control-input:checked~.custom-control-label::before {
background-color: #3a474e; 
border-color: white;
}


.custom-switch .custom-control-label::after{
color:  #3a474e; 
background-color: #3a474e; 
}	


.dark-mode html,
body,
header,
#intro {
height: 100%;
color: white;
background-color: #3a474e;
}


.col-1 {
max-width:100%;
top:0px !important;
}
	

.col-9 {
max-width: 84%;	
}

		
h4 { 
color: #f29111; 
}		 
	 
		 
.row {
margin-left: 15px;
margin-right: 15px;
flex-wrap: nowrap !important;
}
  

.nav-pills .nav-link.active, .nav-pills .show>.nav-link {
padding: .34rem 1.10rem;
border-right: transparent !important;
background: transparent;
color: white;
border-left: 3px solid  white;
}


.nav-pills .nav-link.active:hover {
background: transparent;
color: white;
border-left: 3px solid  white;
padding: .34rem 1.10rem;
}

.nav-pills .nav-link:hover {
color: white;
background: transparent;
border-left: 3px solid  #f29111;
}

.nav-pills .nav-link {
border-radius: 0rem; 
background: transparent;
color: white;
border-left: 3px solid #78909c;
}
			

.extraspace {
flex-wrap: nowrap !important;
text-overflow: ellipsis;
white-space: nowrap;
display:block;
width:100%;
min-width:1px;
}
			 
			 
.nav-tabs .nav-link {
color:  white;
background-color: #30353c;
border-color: #dee2e6 #dee2e6 #fff;
}
	

.nav-tabs .nav-item.show .nav-link, .nav-tabs .nav-link.active {
color:  white;
background-color: #30353c;
border-color: #dee2e6 #dee2e6 #fff;
}


.tab-content>.tab-pane {
padding-left:5px;
padding-top:20px;
margin-top:80px;
}

	

.nav-tabs .nav-link:hover {
color:   white;
}



.logo {
color: white;
}



kbd {
background: #4a5b64  ;
border-radius: 100px !important;
color: white;
padding: 0.5rem 1.4rem;
box-shadow: 0px 0px 5px rgba(0,0,0,0.10),
     0px 5px 5px rgba(0,0,0,0.05),
     0px 5px 5px rgba(0,0,0,0.05),
     0px 5px 5px rgba(0,0,0,0.05) !important;
}


.kbd_text {
background: #00758f;
border-radius: 100px !important;
color: white;
padding: .34rem 1.10rem;
}



.nav-tabs .nav-link {
border: 0px solid transparent !important;;
border-top-left-radius: 0rem;
border-top-right-radius: 0rem;
}



.table th {
text-align: center;
font-weight: bold;
position: sticky;
top: 66px;
color: white;
background-color: #78909c !important;
white-space:nowrap;
}

tr, .runtimeth {
position: sticky !important;
top: 29px !important;
}


.table, th, tr, td {
border: 1px solid #003b4d;
font-weight: bold;
}


tr:hover {
box-shadow: 0px 0px 5px rgba(0,0,0,0.10),
     0px 5px 5px rgba(0,0,0,0.05),
     0px 5px 5px rgba(0,0,0,0.05),
     0px 5px 5px rgba(0,0,0,0.05) !important;
}


table {
width: 100%; 
text-align: left;
overflow-y: auto;
/*word-break: break-word;   */
box-shadow: 5px 0px 5px rgba(0,0,0,0.10),
     5px 5px 5px rgba(0,0,0,0.05),
     5px 5px 5px rgba(0,0,0,0.05),
     5px 5px 5px rgba(0,0,0,0.05) !important;
}


/* only the cells with at least one cell before (aka all except the first one): td + td */
td + td{  
word-break: break-all;
max-width: 560px;
}

/* only the first cell: td:nth-child(1)  */
td:nth-child(1) {  
padding-right:10px;
}


/* hover only for the first cell: td:nth-child(1)  */
tr:hover td:nth-child(1) {  
 /* add here design  */
}


.btn-blue-grey   {
background: #4a5b64  !important;
color: white;    
border-radius: 100px !important;
padding: .34rem 1.10rem;
}

	
.btn-blue-grey:hover   {
background: #78909c  !important;
color: white;    
border-radius: 100px !important;
padding: .34rem 1.10rem;
}	

	
.navbar-brand {
margin-left: 20px;
background: #30353c;
}

.default-color{
background-color: #30353c !important;
}


.btn {
margin: 0rem;  
}

.font-weight-bold {
color: white;
}


.hr_title_sec {
width: 30px;
border: 4px solid #f29111;
margin: 3px;
display:inline-block;
margin-bottom: 30px;
}


.hr_title { 
width: 50px;
border: 5px solid #f29111;
margin: 3px;
display:inline-block;0
}


hr {
border-top: 1px solid #324b5c;
}


 .light-mode  hr {
border-top: 1px solid #dadada;
}


.col-md-12 {
/*  margin-left:15px;  */
top: 50px;
}


.form-control:focus   {
color: #f29111;
border-bottom: 1px solid #ced4da !important;
box-shadow: 0 0 3px transparent !important;
-moz-box-shadow: 0 0 3px transparent !important;
-webkit-box-shadow: 0 0 3px transparent !important;
}

.form-control {
color: #78909c;
}


.w-75 {
width: 49%!important;
}


.sticky {
position: -webkit-sticky; /* Safari */  
position: sticky;
top: 100px;
z-index: 1020;
}


.light-mode #myBtn {
display: none;
position: fixed;
bottom: 20px;
left: 7px;
z-index: 99;
font-size: 40px !important;
border: none;
outline: none;
background-color : transparent !important;
color: white;
cursor: pointer;
padding: 15px;
}


#myBtn {
display: none;
position: fixed;
bottom: 20px;
left: 7px;
z-index: 99;
font-size: 40px;
border: none;
outline: none;
background-color : transparent !important;
color: white;
cursor: pointer;
padding: 15px;
}

#myBtn:hover {
background-color : transparent !important;
color: #f29111;
}


.tab-extra-content{
padding-left:0%;
padding-top:5px;
}

.fa-arrow-down {
color:#f80000;
}


.fa-times-circle {
color:#f80000;
}

.fa-arrow-up  {
color: #3a913f;
}

.fa-play  {
color: #3a913f;
}

.fa-exclamation-triangle {
color: white !important;
}




.fa-times {
color:#f29111;
}
    

.fa-check {
color: #3a913f;
}

.fa-eye-slash  {
color: white !important;
}
	
h4  {
color: white !important;
}	

.card-body
{
background-color: #4a5b64 !important;
color: white !important;
box-shadow: 10px 0px 10px rgba(0,0,0,0.10),
     10px 5px 10px rgba(0,0,0,0.05),
     10px 5px 10px rgba(0,0,0,0.05),
     10px 5px 10px rgba(0,0,0,0.05) !important;
}

.card-header {
background-color: #4a5b64 !important;
color: white !important;
border-bottom: 1.5px solid #939699;
}

    
.card-text {
color: white !important;
}

.rowspan_2 {
background-color: #30353c !important;
color: #f29111 !important;
}

.fa-times-circle {
color:#8aadbf;
}


.light-mode {
background-color: #f3f3f3; 
height: 100%;
}
	
.light-mode #html  #body  #header  #intro {
height: 100%;
background-color:white  !important;
}
	


.light-mode .nav-pills .nav-link.active, .nav-pills .show>.nav-link {
padding: .34rem 1.10rem;
border-right: transparent !important;
background: transparent;
color: #343a40;
border-left: 3px solid  white;
}


.light-mode  .nav-pills .nav-link.active:hover {
background: transparent;
color: #343a40;
border-left: 3px solid  white;
padding: .34rem 1.10rem;
}

 .light-mode  .nav-pills .nav-link:hover {
color: #343a40;
background: transparent;
border-left: 3px solid  #f29111;
}

.light-mode  .nav-pills .nav-link {
border-radius: 0rem; 
background: transparent;
color: #343a40;
border-left: 3px solid #78909c;
}	

	
.light-mode .white-text {
color: #454d55 !important;
}
	
	
.light-mode #myBtn {
display: none;
position: fixed;
bottom: 20px;
left: 7px;
z-index: 99;
font-size: 50px;
border: none;
outline: none;
background-color : transparent !important;
color: #454d55;
cursor: pointer;
padding: 15px;
}
	
.light-mode #myBtn:hover {
color: #f29111;
}



.light-mode .fa-search:before {
color: #343a40 !important;

}
	
	
.light-mode .table th {
text-align: center;
font-weight: bold;
position: sticky;
top: 66px;
color: white;
background-color: #4a5b64 !important;
white-space:nowrap;

}	
	
.light-mode  table {
border: 1px solid #003b4d;
font-weight: bold;
background-color:#f8f8f8;
color: #454d55;
}
	
.light-mode tr:hover {
font-weight:bold !important;
color: black !important;
background-color: #d9e0e6 !important;
}
	
.light-mode  .card-body {
background-color: #dee0e0 !important;
color: #454d55 !important;

}

.light-mode  .card-header {
background-color: #dee0e0 !important;
color: #454d55 !important;

}	

.light-mode .fa-eye-slash {
color: #454d55 !important;
font-weight:bold !important;
}
	
.light-mode .fa-exclamation-triangle {
color: #454d55 !important;
font-weight:bold !important;
}	
	
	
.btn-link:hover, .btn-link:focus, .btn-link:active {
color: white;  
}


.btn-link {
  color: #f29111;
} 

.accordion>.card .card-header  {
background-color: #343a40 !important;
}


.list-group-item  {
color: black;
}

.card-header {
border-bottom: 1.5px solid #f29111;
background-color: #343a40 !important;
}

.card {
box-shadow: 10px 0px 10px rgba(0,0,0,0.10),
     10px 5px 10px rgba(0,0,0,0.05),
     10px 5px 10px rgba(0,0,0,0.05),
     10px 5px 10px rgba(0,0,0,0.05) !important;
	}


.list-group-item{
background-color: #4a5b64 !important;
color: white !important;
}

	
.light-mode	 .list-group-item {
background-color: white !important;
color: #4a5b64 !important;
}
	
	
.btn.btn-lg {
padding: 10px;
background-color: #78909c !important;
border-radius: 100% 100% 100% 100%;
}


.btn.btn-lg:hover {
background-color: #f29111 !important;
}
	
.popover-header  {
background-color: #78909c !important;
font-weight: bold;
}



.light-mode .default-color {
background-color: #f3f3f3 !important;
}
	
.light-mode .nav-tabs .nav-link {
color: #454d55;
background-color: #f3f3f3;
}
	
	
.light-mode .navbar-brand {
background-color: #f3f3f3 !important;
}
	
	
.light-mode .logo {
color: #454d55 !important;
}
	
	
.light-mode .fa-github {
color: #454d55 !important;
}	
	
.light-mode .fa-blogger {
color: #454d55 !important;
}	
	
	
.light-mode .fa-code-branch {
color: #454d55 !important;
}	


.light-mode .hr_title {
border: 5px solid #f29111;	 
}
	
	
.light-mode .hr_title_sec {
border: 4px solid #f29111;
}

	
.light-mode .font-weight-bold {
color: #454d55;
}
	

.light-mode .rowspan_2 {
    background-color: #78909c !important;
    color: white !important;
}


</style>
</head>

<body>

<button onclick="topFunction()" id="myBtn" data-toggle="tooltip" data-placement="top" title=""><i class="fas fa-angle-double-up"></i></button>

<!--Navbar -->
<nav class="mb-1 navbar navbar-expand-lg navbar-dark default-color fixed-top ">
    <a class="navbar-brand"><h3 class = "logo" data-toggle="tooltip" data-placement="bottom" title="Well Known Attributes" > WLST.p<font color= "#f29111">&#x3BB; </font> &nbsp; </h3></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent-333"
      aria-controls="navbarSupportedContent-333" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent-333">


        <ul class="nav nav-tabs  " id="myTab" role="tablist">
            <li class="nav-item">
              <a class="nav-link active" id="Domain-tab" data-toggle="tab" href="#Domain" role="tab" aria-controls="Domain"
                aria-selected="true">Domain</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" id="Server-tab" data-toggle="tab" href="#Server" role="tab" aria-controls="Server"
                aria-selected="false">Server</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="Cluster-tab" data-toggle="tab" href="#Cluster" role="tab" aria-controls="Cluster"
                aria-selected="false">Cluster</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="Machine-tab" data-toggle="tab" href="#Machine" role="tab" aria-controls="Machine"
                aria-selected="false">Machine</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="Applications-tab" data-toggle="tab" href="#Applications" role="tab" aria-controls="Applications"
                aria-selected="false">Applications</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="Libraries-tab" data-toggle="tab" href="#Libraries" role="tab" aria-controls="Libraries"
                aria-selected="false">Libraries</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="JDBC-tab" data-toggle="tab" href="#JDBC" role="tab" aria-controls="JDBC"
                aria-selected="false">JDBC</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="JMS-tab" data-toggle="tab" href="#JMS" role="tab" aria-controls="JMS"
                aria-selected="false">JMS</a>
            </li>

            <li class="nav-item">
              <a class="nav-link" id="Coherence-tab" data-toggle="tab" href="#Coherence" role="tab" aria-controls="Coherence"
                aria-selected="false">Coherence</a>
            </li>

            <li class="nav-item">
              <a class="nav-link" id="Stores-tab" data-toggle="tab" href="#Stores" role="tab" aria-controls="Stores"
                aria-selected="false">Stores</a>
            </li>


            <li class="nav-item">
              <a class="nav-link" id="OS-tab" data-toggle="tab" href="#OS" role="tab" aria-controls="OS"
                aria-selected="false">OS</a>
            </li>

          </ul>


<ul class="navbar-nav ml-auto nav-flex-icons">
		<li class="nav-item" >
		  <div class="custom-control custom-switch">
  <input type="checkbox" class="custom-control-input" id="customSwitch1" checked/>
  <label class="custom-control-label" for="customSwitch1" onclick="lightModeFunction()" >  </label>
<div>
	  </li>
		  </ul>

     
    </div>
  </nav>
  <!--/.Navbar -->

"""

print "Done printing the output menu.... "

print "Printing the intro domain info.... "


print >>f, listIntroDomain()


print >>f, """

<!-- **********************  -->
<!-- **********************  -->
<!-- **********************  -->

<div class="tab-content" id="myTabContent"> """


print "Done printing the intro domain info.... "

print "Printing the Domain info.... "

print >>f, """
    
<!-- **********************  -->

<!--  start Domain tabs -->

    <div class="tab-pane fade show active" id="Domain" role="tabpanel" aria-labelledby="Domain-tab">

      <!--  start sub Domain tabs -->

        <div class="row  ">
            <div class="col-1 ">
                <h2 class="font-weight-bold ">Domain</h2>
                <hr class="hr_title_sec ">
            <p></p>

              <div class="nav flex-column nav-pills sticky extraspace " id="v-pills-tab" role="tablist" aria-orientation="vertical">
                <a class="nav-link active" id="v-pills-DomainOverview-tab" data-toggle="pill" href="#v-pills-DomainOverview" role="tab" aria-controls="v-pills-DomainOverview" aria-selected="true">Domain Overview  </a>
                <a class="nav-link" id="v-pills-DomainAttributes-tab" data-toggle="pill" href="#v-pills-DomainAttributes" role="tab" aria-controls="v-pills-DomainAttributes" aria-selected="false">Domain Attributes</a>
                <a class="nav-link" id="v-pills-JTAAttributes-tab" data-toggle="pill" href="#v-pills-JTAAttributes" role="tab" aria-controls="v-pills-JTAAttributes" aria-selected="false">JTA Attributes</a>
                <a class="nav-link" id="v-pills-WorkManagersTargets-tab" data-toggle="pill" href="#v-pills-WorkManagersTargets" role="tab" aria-controls="v-pills-WorkManagersTargets" aria-selected="false">WorkManagers Target</a>
                <a class="nav-link" id="v-pills-WMOverview-tab" data-toggle="pill" href="#v-pills-WMOverview" role="tab" aria-controls="v-pills-WMOverview" aria-selected="false">WorkManagers Overview</a>
                <a class="nav-link" id="v-pills-WorkManagersMaxThreadsConstraints-tab" data-toggle="pill" href="#v-pills-WorkManagersMaxThreadsConstraints" role="tab" aria-controls="v-pills-WorkManagersMaxThreadsConstraints" aria-selected="false">WM MaxThreadsConstraints</a>
                <a class="nav-link" id="v-pills-WorkManagersMinThreadsConstraints-tab" data-toggle="pill" href="#v-pills-WorkManagersMinThreadsConstraints" role="tab" aria-controls="v-pills-WorkManagersMinThreadsConstraints" aria-selected="false">WM MinThreadsConstraints</a>
                <a class="nav-link" id="v-pills-WorkManagersCapacities-tab" data-toggle="pill" href="#v-pills-WorkManagersCapacities" role="tab" aria-controls="v-pills-WorkManagersCapacities" aria-selected="false">WM Capacities</a>
                <a class="nav-link" id="v-pills-WorkManagersFairShareRequestClasses-tab" data-toggle="pill" href="#v-pills-WorkManagersFairShareRequestClasses" role="tab" aria-controls="v-pills-WorkManagersFairShareRequestClasses" aria-selected="false">WM FairShareRequestClasses</a>
                <a class="nav-link" id="v-pills-WorkManagersResponseTimeRequestClasses-tab" data-toggle="pill" href="#v-pills-WorkManagersResponseTimeRequestClasses" role="tab" aria-controls="v-pills-WorkManagersResponseTimeRequestClasses" aria-selected="false">WM ResponseTimeRequestClasses</a>
                <a class="nav-link" id="v-pills-WorkManagersContextRequestClasses-tab" data-toggle="pill" href="#v-pills-WorkManagersContextRequestClasses" role="tab" aria-controls="v-pills-WorkManagersContextRequestClasses" aria-selected="false">WM ContextRequestClasses</a>
                <a class="nav-link" id="v-pills-WorkManagerMainValues-tab" data-toggle="pill" href="#v-pills-WorkManagerMainValues" role="tab" aria-controls="v-pills-WorkManagerMainValues" aria-selected="false">WorkManager Main Values</a>
                
                <a class="nav-link" id="v-pills-AuthenticationProviders-tab" data-toggle="pill" href="#v-pills-AuthenticationProviders" role="tab" aria-controls="v-pills-AuthenticationProviders" aria-selected="false">Authentication Providers</a>
              </div>
            </div>

            <div class="col-9">
              <div class="tab-content tab-extra-content" id="v-pills-tabContent">
                <div class="tab-pane fade show active" id="v-pills-DomainOverview" role="tabpanel" aria-labelledby="v-pills-DomainOverview-tab"> """

print >>f,  listDomainOverviewTable("id_545454")

print >>f,     """
                
                </div>

                <div class="tab-pane fade" id="v-pills-DomainAttributes" role="tabpanel" aria-labelledby="v-pills-DomainAttributes-tab"> """
                
print >>f,  listDomainConfig("id_544881212222")

print >>f,     """
                
                </div>
                <div class="tab-pane fade" id="v-pills-JTAAttributes" role="tabpanel" aria-labelledby="v-pills-JTAAttributes-tab"> """ 
                
print >>f,  listValuesVerticalCheck ("id_2908411091" , "domainConfig", "JTA");
                
print >>f, """                
                 </div>
                <div class="tab-pane fade" id="v-pills-WorkManagersTargets" role="tabpanel" aria-labelledby="v-pills-WorkManagersTargets-tab">  """
                
print >>f, listWMTargetCheck ("id_1000211882345") 

print >>f, """                
                 </div>

                <div class="tab-pane fade" id="v-pills-WMOverview" role="tabpanel" aria-labelledby="v-pills-WMOverview-tab">  """
          

print >>f, listValuesVerticalWMCheck ("id_100235897852025" , "domainConfig",  "SelfTuning",  "WorkManagers" )
print >>f, listValuesHorizontalWMCheck ("id_1078899999025" , "domainConfig",  "SelfTuning",  "WorkManagers" )
     
                
print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersMaxThreadsConstraints" role="tabpanel" aria-labelledby="v-pills-WorkManagersMaxThreadsConstraints-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_1089788888025" , "domainConfig",  'SelfTuning',  'MaxThreadsConstraints' )
print >>f, listValuesHorizontalWMCheck ("id_101111108025" , "domainConfig",  'SelfTuning',  'MaxThreadsConstraints' )

print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersMinThreadsConstraints" role="tabpanel" aria-labelledby="v-pills-WorkManagersMinThreadsConstraints-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_8888872025" , "domainConfig",  'SelfTuning',  'MinThreadsConstraints' )
print >>f, listValuesHorizontalWMCheck ("id_888555222225" , "domainConfig",  'SelfTuning',  'MinThreadsConstraints' )


print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersCapacities" role="tabpanel" aria-labelledby="v-pills-WorkManagersCapacities-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_1002358999987888" , "domainConfig",  'SelfTuning',  'Capacities' )
print >>f, listValuesHorizontalWMCheck ("id_1002300011117888" , "domainConfig",  'SelfTuning',  'Capacities' )


print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersFairShareRequestClasses" role="tabpanel" aria-labelledby="v-pills-WorkManagersFairShareRequestClasses-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_1002777444110" , "domainConfig",  'SelfTuning',  'FairShareRequestClasses' )
print >>f, listValuesHorizontalWMCheck ("id_106666644110" , "domainConfig",  'SelfTuning',  'FairShareRequestClasses' )


print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersResponseTimeRequestClasses" role="tabpanel" aria-labelledby="v-pills-WorkManagersResponseTimeRequestClasses-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_10855225844110" , "domainConfig",  'SelfTuning',  'ResponseTimeRequestClasses' )
print >>f, listValuesHorizontalWMCheck ("id_22222220844110" , "domainConfig",  'SelfTuning',  'ResponseTimeRequestClasses' )


print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagersContextRequestClasses" role="tabpanel" aria-labelledby="v-pills-WorkManagersContextRequestClasses-tab">  """
    
print >>f, listValuesVerticalWMCheck ("id_1087890000" , "domainConfig",  'SelfTuning',  'ContextRequestClasses' )
print >>f, listValuesHorizontalWMCheck ("id_1055555400" , "domainConfig",  'SelfTuning',  'ContextRequestClasses' )


print >>f, """
       </div>
       
       <div class="tab-pane fade" id="v-pills-WorkManagerMainValues" role="tabpanel" aria-labelledby="v-pills-WorkManagerMainValues-tab">  """
    
print >>f, getValuesVerticalWMFullOverviewCheck ("id_107896321477852025" , "domainConfig",  'SelfTuning',  'WorkManagers' )
print >>f, getValuesHorizontalWMFullOverviewCheck   ("id_1078852585258852025" , "domainConfig",  'SelfTuning',  'WorkManagers' ) 
                
print >>f, """
                </div>

                <div class="tab-pane fade" id="v-pills-AuthenticationProviders" role="tabpanel" aria-labelledby="v-pills-AuthenticationProviders-tab"> """
                          
                
print >>f, listAuthenticationProvidersVertical("id_00545485888400")
print >>f, listAuthenticationProvidersHorizontal("id_0985689082120400")
                
print >>f, """           
                
                </div>
              </div>
            </div>
          </div>
         <!--  stop sub Domain tabs -->
       
    </div>

<!--  stop  Domain tabs -->  
<!-- **********************  -->

""" 

print "Done printing the Domain info.... "




print "Printing the Server info.... "

print >>f, """

<!--  start Server tabs -->

    <div class="tab-pane fade" id="Server" role="tabpanel" aria-labelledby="Server-tab">

  <!--  start sub Server tabs -->

    <div class="row  ">
        <div class="col-1 ">
            <h2 class="font-weight-bold ">Servers</h2>
            <hr class="hr_title_sec ">
        <p></p>

          <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            <a class="nav-link active" id="v-pills-ServerAttributes-tab" data-toggle="pill" href="#v-pills-ServerAttributes" role="tab" aria-controls="v-pills-ServerAttributes" aria-selected="true">Server Attributes  </a>
            <a class="nav-link" id="v-pills-ServerRuntimes-tab" data-toggle="pill" href="#v-pills-ServerRuntimes" role="tab" aria-controls="v-pills-ServerRuntimes" aria-selected="false"> Server Runtimes</a>
            <a class="nav-link" id="v-pills-JVMRuntime-tab" data-toggle="pill" href="#v-pills-JVMRuntime" role="tab" aria-controls="v-pills-JVMRuntime" aria-selected="false">JVM Runtime</a>
            <a class="nav-link" id="v-pills-ServerLifeCycleRuntimes-tab" data-toggle="pill" href="#v-pills-ServerLifeCycleRuntimes" role="tab" aria-controls="v-pills-ServerLifeCycleRuntimes" aria-selected="false">Server Life Cycle Runtimes</a>
            <a class="nav-link" id="v-pills-SSL-tab" data-toggle="pill" href="#v-pills-SSL" role="tab" aria-controls="v-pills-SSL" aria-selected="false">SSL</a>
            <a class="nav-link" id="v-pills-ServerLog-tab" data-toggle="pill" href="#v-pills-ServerLog" role="tab" aria-controls="v-pills-ServerLog" aria-selected="false">Server Log</a>
            <a class="nav-link" id="v-pills-WebServer-tab" data-toggle="pill" href="#v-pills-WebServer" role="tab" aria-controls="v-pills-WebServer" aria-selected="false">WebServer</a>
            <a class="nav-link" id="v-pills-ThreadPoolRuntime-tab" data-toggle="pill" href="#v-pills-ThreadPoolRuntime" role="tab" aria-controls="v-pills-ThreadPoolRuntime" aria-selected="false">Thread Pool Runtime</a>
            <a class="nav-link" id="v-pills-JTARuntime-tab" data-toggle="pill" href="#v-pills-JTARuntime" role="tab" aria-controls="v-pills-JTARuntime" aria-selected="false">JTA Runtime</a>

          </div>
        </div>

        <div class="col-9">
          <div class="tab-content tab-extra-content" id="v-pills-tabContent">
            <div class="tab-pane fade show active" id="v-pills-ServerAttributes" role="tabpanel" aria-labelledby="v-pills-ServerAttributes-tab"> """
                      
print >>f,  listValuesVerticalCheck ("id_2299989809891" , "domainConfig", "Servers")
print >>f,  listValuesHorizontalCheck ("id_22644646464" , "domainConfig", "Servers")

print >>f, """            
            </div>
            <div class="tab-pane fade" id="v-pills-ServerRuntimes" role="tabpanel" aria-labelledby="v-pills-ServerRuntimes-tab">  """
            

print >>f, listValuesVerticalCheck ("id_2788201478963" , "domainRuntime", "ServerRuntimes")
print >>f, listValuesHorizontal ("id_85264898201478963" , "domainRuntime", "ServerRuntimes")


print >>f, """            
</div>
            <div class="tab-pane fade" id="v-pills-JVMRuntime" role="tabpanel" aria-labelledby="v-pills-JVMRuntime-tab"> """
            
           
print >>f, listValuesVerticalCheck ("id_2788456548963" , "domainRuntime", "ServerRuntimes", "JVMRuntime")
print >>f, listValuesHorizontal ("id_852665896588963" , "domainRuntime", "ServerRuntimes", "JVMRuntime")


print >>f, """     
                        
            </div>
            <div class="tab-pane fade" id="v-pills-ServerLifeCycleRuntimes" role="tabpanel" aria-labelledby="v-pills-ServerLifeCycleRuntimes-tab">  """
                    
print >>f, listValuesVerticalCheck ("id_65486548963" , "domainRuntime", "ServerLifeCycleRuntimes")
print >>f, listValuesHorizontal ("id_349634996588963" , "domainRuntime", "ServerLifeCycleRuntimes")


print >>f, """     
                        
            </div>
            <div class="tab-pane fade" id="v-pills-SSL" role="tabpanel" aria-labelledby="v-pills-SSL-tab"> """
            
print >>f,  listValuesVerticalCheck ("id_2299983459809891" , "domainConfig", "Servers", "SSL")
print >>f,  listValuesHorizontalCheck ("id_2263457644646464" , "domainConfig", "Servers" , "SSL")
            
print >>f, """            
            </div>
            <div class="tab-pane fade" id="v-pills-ServerLog" role="tabpanel" aria-labelledby="v-pills-ServerLog-tab"> """

print >>f,  listValuesVerticalCheck ("id_229346359891" , "domainConfig", "Servers", "Log")
print >>f,  listValuesHorizontalCheck ("id_2267988" , "domainConfig", "Servers" , "Log")

print >>f, """ 
            </div>
            <div class="tab-pane fade" id="v-pills-WebServer" role="tabpanel" aria-labelledby="v-pills-WebServer-tab"> """

print >>f,  listValuesVerticalCheck ("id_35609891" , "domainConfig", "Servers", "WebServer")
print >>f,  listValuesHorizontalCheck ("id_274586584" , "domainConfig", "Servers" , "WebServer")

print >>f, """
            </div>
            <div class="tab-pane fade" id="v-pills-ThreadPoolRuntime" role="tabpanel" aria-labelledby="v-pills-ThreadPoolRuntime-tab">  """ 
                                   
print >>f, listValuesVerticalCustom ("id_6548678950" , "domainRuntime", "ServerRuntimes" , "ThreadPoolRuntime", "ThreadPoolRuntime")
print >>f, listValuesHorizontalCustom ("id_3496349965000121" , "domainRuntime", "ServerRuntimes" , "ThreadPoolRuntime", "ThreadPoolRuntime") 

print >>f, """               
            
            </div>
            <div class="tab-pane fade" id="v-pills-JTARuntime" role="tabpanel" aria-labelledby="v-pills-JTARuntime-tab">  """
             
print >>f, listValuesVerticalCustom ("id_6548678950002" , "domainRuntime", "ServerRuntimes" , "JTARuntime", "JTARuntime")
print >>f, listValuesHorizontalCustom ("id_6349965000121987503" , "domainRuntime", "ServerRuntimes" , "JTARuntime", "JTARuntime")


print >>f, """

            </div>
          </div>
        </div>
      </div>
     <!--  stop sub Server tabs -->
   
    </div>

    <!--  stop  Server tabs -->   
    
<!-- **********************  -->
""" 

print "Done printing the Server info.... "



print "Printing the Cluster info.... "

print >>f, """

    <div class="tab-pane fade" id="Cluster" role="tabpanel" aria-labelledby="Cluster-tab">

<!--  start sub Cluster tabs -->

<div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">Cluster</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-ClustersOverview-tab" data-toggle="pill" href="#v-pills-ClustersOverview" role="tab" aria-controls="v-pills-ClustersOverview" aria-selected="true">Clusters Overview  </a>
      <a class="nav-link" id="v-pills-ClusterServers-tab" data-toggle="pill" href="#v-pills-ClusterServers" role="tab" aria-controls="v-pills-ClusterServers" aria-selected="false"> Cluster Servers</a>
      <a class="nav-link" id="v-pills-JTAClusters-tab" data-toggle="pill" href="#v-pills-JTAClusters" role="tab" aria-controls="v-pills-JTAClusters" aria-selected="false"> JTA Clusters</a>
      <a class="nav-link" id="v-pills-OverloadProtection-tab" data-toggle="pill" href="#v-pills-OverloadProtection" role="tab" aria-controls="v-pills-OverloadProtection" aria-selected="false"> OverloadProtection</a>
      <a class="nav-link" id="v-pills-DatabaseLessLeasingBasis-tab" data-toggle="pill" href="#v-pills-DatabaseLessLeasingBasis" role="tab" aria-controls="v-pills-DatabaseLessLeasingBasis" aria-selected="false"> DatabaseLessLeasingBasis</a>
      <a class="nav-link" id="v-pills-DynamicServers-tab" data-toggle="pill" href="#v-pills-DynamicServers" role="tab" aria-controls="v-pills-DynamicServers" aria-selected="false"> Dynamic Servers</a>

      <a class="nav-link" id="v-pills-CandidateMachinesForMigratableServers-tab" data-toggle="pill" href="#v-pills-CandidateMachinesForMigratableServers" role="tab" aria-controls="v-pills-CandidateMachinesForMigratableServers" aria-selected="false"> CandidateMachinesForMigratableServers</a>
      <a class="nav-link" id="v-pills-CoherenceTier-tab" data-toggle="pill" href="#v-pills-CoherenceTier" role="tab" aria-controls="v-pills-CoherenceTier" aria-selected="false"> Coherence Tier</a>
      <a class="nav-link" id="v-pills-DataSourceForAutomaticMigration-tab" data-toggle="pill" href="#v-pills-DataSourceForAutomaticMigration" role="tab" aria-controls="v-pills-DataSourceForAutomaticMigration" aria-selected="false"> DataSourceForAutomaticMigration</a>
      <a class="nav-link" id="v-pills-DataSourceForJobScheduler-tab" data-toggle="pill" href="#v-pills-DataSourceForJobScheduler" role="tab" aria-controls="v-pills-DataSourceForJobScheduler" aria-selected="false"> DataSourceForJobScheduler</a>
      <a class="nav-link" id="v-pills-DataSourceForSessionPersistence-tab" data-toggle="pill" href="#v-pills-DataSourceForSessionPersistence" role="tab" aria-controls="v-pills-DataSourceForSessionPersistence" aria-selected="false"> DataSourceForSessionPersistence</a>
      
      


    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-ClustersOverview" role="tabpanel" aria-labelledby="v-pills-ClustersOverview-tab">"""
      
print >>f,  listValuesVerticalCheck ("id_27854643491" , "domainConfig", "Clusters")
print >>f,  listValuesHorizontalCheck ("id_56764" , "domainConfig", "Clusters")


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-ClusterServers" role="tabpanel" aria-labelledby="v-pills-ClusterServers-tab"> """

print >>f,  listResourceTargetTable ( "id_39879589722700" , "domainConfig", "Clusters", 'Servers')


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-JTAClusters" role="tabpanel" aria-labelledby="v-pills-JTAClusters-tab"> """

print >>f,  listValuesVerticalCheck ("id_22967769891" , "domainConfig", "Clusters", "JTACluster")
print >>f,  listValuesHorizontalCheck ("id_22640654" , "domainConfig", "Clusters" , "JTACluster")   

print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-OverloadProtection" role="tabpanel" aria-labelledby="v-pills-OverloadProtection-tab"> """

print >>f,  listValuesVerticalCheck ("id_229000169891" , "domainConfig", "Clusters", "OverloadProtection")
print >>f,  listValuesHorizontalCheck ("id_296633660654" , "domainConfig", "Clusters" , "OverloadProtection")      


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-DatabaseLessLeasingBasis" role="tabpanel" aria-labelledby="v-pills-DatabaseLessLeasingBasis-tab"> """

print >>f,  listValuesVerticalCheck ("id_8965698540169891" , "domainConfig", "Clusters", "DatabaseLessLeasingBasis")
print >>f,  listValuesHorizontalCheck ("id_29663852365478" , "domainConfig", "Clusters" , "DatabaseLessLeasingBasis")      


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-DynamicServers" role="tabpanel" aria-labelledby="v-pills-DynamicServers-tab"> """

print >>f,  listValuesVerticalCheck ("id_89878880169891" , "domainConfig", "Clusters", "DynamicServers")
print >>f,  listValuesHorizontalCheck ("id_2966256985365478" , "domainConfig", "Clusters" , "DynamicServers")      


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-CandidateMachinesForMigratableServers" role="tabpanel" aria-labelledby="v-pills-CandidateMachinesForMigratableServers-tab"> """

print >>f,  listValuesVerticalCheck ("id_8987788201209891" , "domainConfig", "Clusters", "CandidateMachinesForMigratableServers")
print >>f,  listValuesHorizontalCheck ("id_265489703085365478" , "domainConfig", "Clusters" , "CandidateMachinesForMigratableServers")  


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-CoherenceTier" role="tabpanel" aria-labelledby="v-pills-CoherenceTier-tab"> """

print >>f,  listValuesVerticalCheck ("id_20102018201209891" , "domainConfig", "Clusters", "CoherenceTier")
print >>f,  listValuesHorizontalCheck ("id_10100356899703085365478" , "domainConfig", "Clusters" , "CoherenceTier")       


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-DataSourceForAutomaticMigration" role="tabpanel" aria-labelledby="v-pills-DataSourceForAutomaticMigration-tab"> """

print >>f,  listValuesVerticalCheck ("id_2010201820202020" , "domainConfig", "Clusters", "DataSourceForAutomaticMigration")
print >>f,  listValuesHorizontalCheck ("id_10100332020301478" , "domainConfig", "Clusters" , "DataSourceForAutomaticMigration")       


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-DataSourceForJobScheduler" role="tabpanel" aria-labelledby="v-pills-DataSourceForJobScheduler-tab"> """

print >>f,  listValuesVerticalCheck ("id_2050505020202020" , "domainConfig", "Clusters", "DataSourceForJobScheduler")
print >>f,  listValuesHorizontalCheck ("id_1016060505001478" , "domainConfig", "Clusters" , "DataSourceForJobScheduler")      


print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-DataSourceForSessionPersistence" role="tabpanel" aria-labelledby="v-pills-DataSourceForSessionPersistence-tab"> """

print >>f,  listValuesVerticalCheck ("id_2050505808080920" , "domainConfig", "Clusters", "DataSourceForSessionPersistence")
print >>f,  listValuesHorizontalCheck ("id_101690907078" , "domainConfig", "Clusters" , "DataSourceForSessionPersistence")      

print >>f, """      
      </div> 
    </div>
  </div>
</div>

<!--  stop sub Cluster tabs -->
    
    </div>

    <!-- **********************  -->

"""


print "Done printing the Cluster info.... ";




print "Printing the Machine info.... ";

print >>f, """

    <div class="tab-pane fade" id="Machine" role="tabpanel" aria-labelledby="Machine-tab">
        
        <!--  start sub Machine tabs -->

     <div class="row  ">
      <div class="col-1 ">
          <h2 class="font-weight-bold ">Machine</h2>
          <hr class="hr_title_sec ">
      <p></p>
    
        <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
          <a class="nav-link active" id="v-pills-MachinesAttributes-tab" data-toggle="pill" href="#v-pills-MachinesAttributes" role="tab" aria-controls="v-pills-MachinesAttributes" aria-selected="true">Machines Attributes </a>
          <a class="nav-link" id="v-pills-NodeManagerAttributes-tab" data-toggle="pill" href="#v-pills-NodeManagerAttributes" role="tab" aria-controls="v-pills-NodeManagerAttributes" aria-selected="false"> NodeManager Attributes</a>
          <a class="nav-link" id="v-pills-NodeManagerRuntimes-tab" data-toggle="pill" href="#v-pills-NodeManagerRuntimes" role="tab" aria-controls="v-pills-NodeManagerRuntimes" aria-selected="false"> NodeManager Runtimes</a>
    
    
        </div>
      </div>
    
      <div class="col-9">
        <div class="tab-content tab-extra-content" id="v-pills-tabContent"> 
          <div class="tab-pane fade show active" id="v-pills-MachinesAttributes" role="tabpanel" aria-labelledby="v-pills-MachinesAttributes-tab">"""

print >>f,  listValuesVerticalCheck ("id_244409891" , "domainConfig", "Machines")
print >>f,  listValuesHorizontalCheck ("id_299994" , "domainConfig", "Machines")

print >>f, """          
          </div>
          <div class="tab-pane fade" id="v-pills-NodeManagerAttributes" role="tabpanel" aria-labelledby="v-pills-NodeManagerAttributes-tab"> """

print >>f,  listValuesVerticalCheck ("id_2293339891" , "domainConfig", "Machines", "NodeManager")
print >>f,  listValuesHorizontalCheck ("id_2262110" , "domainConfig", "Machines" , "NodeManager")

print >>f, """
           </div>
          <div class="tab-pane fade" id="v-pills-NodeManagerRuntimes" role="tabpanel" aria-labelledby="v-pills-NodeManagerRuntimes-tab">  """
          
# e.g. wlst:domainRuntime -> NodeManagerRuntimes available for release 12.2.1.1.0 +
print >>f, listValuesVerticalCheck ("id_654868528963" , "domainRuntime", "NodeManagerRuntimes")
print >>f,  listValuesHorizontalCheck ("id_6554060504060" , "domainRuntime", "NodeManagerRuntimes")

print >>f, """          
                
          </div>         
        </div>
      </div>
    </div>

  <!--  stop sub Machine  tabs -->
  
  </div>

<!-- **********************  -->  

 """ 

print "Done printing the Machine info.... "




print "Printing the Applications info.... "

print >>f, """

  <div class="tab-pane fade" id="Applications" role="tabpanel" aria-labelledby="Applications-tab">
  
         <!--  start sub Applications tabs -->

         <div class="row  ">
          <div class="col-1 ">
              <h2 class="font-weight-bold ">Applications</h2>
              <hr class="hr_title_sec ">
          <p></p>
        
            <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
              <a class="nav-link active" id="v-pills-ApplicationsTarget-tab" data-toggle="pill" href="#v-pills-ApplicationsTarget" role="tab" aria-controls="v-pills-ApplicationsTarget" aria-selected="true">  Application Targets</a>
              <a class="nav-link" id="v-pills-ApplicationsAttribute-tab" data-toggle="pill" href="#v-pills-ApplicationsAttribute" role="tab" aria-controls="v-pills-ApplicationsAttribute" aria-selected="false"> Application Attributes</a>
              
        
        
            </div>
          </div>
        
          <div class="col-9">
            <div class="tab-content tab-extra-content" id="v-pills-tabContent">
              <div class="tab-pane fade show active" id="v-pills-ApplicationsTarget" role="tabpanel" aria-labelledby="v-pills-ApplicationsTarget-tab">"""
              
              
print >>f, listResourceTargetTable ( "id_33987902227000" , "domainConfig", "AppDeployments", 'Targets')
              
print >>f, """              
              
              </div>
              <div class="tab-pane fade" id="v-pills-ApplicationsAttribute" role="tabpanel" aria-labelledby="v-pills-ApplicationsAttribute-tab">  """
              
print >>f,  listValuesVerticalCheck ("id_97821" , "domainConfig", "AppDeployments")
print >>f,  listValuesHorizontalCheck ("id_525206464" , "domainConfig", "AppDeployments")
              
print >>f, """               
              </div>
            </div>
          </div>
        </div>
    
      <!--  stop sub Applications  tabs -->

</div>
<!-- **********************  -->

 """

print "Done printing the Applications info.... "




print "Printing the Libraries info.... "


print >>f, """

<div class="tab-pane fade" id="Libraries" role="tabpanel" aria-labelledby="Libraries-tab">

  <!--  start sub Libraries tabs -->

  <div class="row  ">
    <div class="col-1 ">
        <h2 class="font-weight-bold ">Libraries</h2>
        <hr class="hr_title_sec ">
    <p></p>
  
      <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
        <a class="nav-link active" id="v-pills-LibrariesTarget-tab" data-toggle="pill" href="#v-pills-LibrariesTarget" role="tab" aria-controls="v-pills-LibrariesTarget" aria-selected="true">  Libraries Targets</a>
        <a class="nav-link" id="v-pills-LibrariesAttribute-tab" data-toggle="pill" href="#v-pills-LibrariesAttribute" role="tab" aria-controls="v-pills-LibrariesAttribute" aria-selected="false"> Libraries Attributes</a>
        
  
      </div>
    </div>
  
    <div class="col-9">
      <div class="tab-content tab-extra-content" id="v-pills-tabContent">
        <div class="tab-pane fade show active" id="v-pills-LibrariesTarget" role="tabpanel" aria-labelledby="v-pills-LibrariesTarget-tab">"""
              
        
print >>f, listResourceTargetTable ( "id_97971045000" , "domainConfig", "Libraries", 'Targets')
              
print >>f, """        
        
        </div>
        <div class="tab-pane fade" id="v-pills-LibrariesAttribute" role="tabpanel" aria-labelledby="v-pills-LibrariesAttribute-tab"> """
        
        
print >>f,  listValuesVerticalCheck ("id_22809891" , "domainConfig", "Libraries")
print >>f,  listValuesHorizontalCheck ("id_023646464" , "domainConfig", "Libraries")
        
print >>f, """         
        </div>
      </div>
    </div>
  </div>

<!--  stop sub Libraries  tabs -->
 
</div>
<!-- **********************  -->

"""

print "Done printing the Libraries info.... "




print "Printing the JDBC info.... "

print >>f, """


<div class="tab-pane fade" id="JDBC" role="tabpanel" aria-labelledby="JDBC-tab">      
  
<!--  start sub JDBC tabs -->

<div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">JDBC</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-JDBCTarget-tab" data-toggle="pill" href="#v-pills-JDBCTarget" role="tab" aria-controls="v-pills-JDBCTarget" aria-selected="true">  JDBC Target</a>
      <a class="nav-link" id="v-pills-JDBCConnectionPoolParams-tab" data-toggle="pill" href="#v-pills-JDBCConnectionPoolParams" role="tab" aria-controls="v-pills-JDBCConnectionPoolParams" aria-selected="false"> JDBC Connection Pool Params</a>
      <a class="nav-link" id="v-pills-JDBCDataSourceParams-tab" data-toggle="pill" href="#v-pills-JDBCDataSourceParams" role="tab" aria-controls="v-pills-JDBCDataSourceParams" aria-selected="false"> JDBC Data Source Params</a>
      <a class="nav-link" id="v-pills-JDBCDriverParams-tab" data-toggle="pill" href="#v-pills-JDBCDriverParams" role="tab" aria-controls="v-pills-JDBCDriverParams" aria-selected="false"> JDBC Driver Params</a>
      <a class="nav-link" id="v-pills-JDBCOracleParams-tab" data-toggle="pill" href="#v-pills-JDBCOracleParams" role="tab" aria-controls="v-pills-JDBCOracleParams" aria-selected="false"> JDBC Oracle Params</a>
      <a class="nav-link" id="v-pills-JDBCXAParams-tab" data-toggle="pill" href="#v-pills-JDBCXAParams" role="tab" aria-controls="v-pills-JDBCXAParams" aria-selected="false"> JDBC XA Params</a>
      <a class="nav-link" id="v-pills-JDBCDBUser-tab" data-toggle="pill" href="#v-pills-JDBCDBUser" role="tab" aria-controls="v-pills-JDBCDBUser" aria-selected="false"> JDBC DB User </a>
      <a class="nav-link" id="v-pills-oracle_net_CONNECT_TIMEOUT-tab" data-toggle="pill" href="#v-pills-oracle_net_CONNECT_TIMEOUT" role="tab" aria-controls="v-pills-oracle_net_CONNECT_TIMEOUT" aria-selected="false">  oracle.net.CONNECT_TIMEOUT </a>
      <a class="nav-link" id="v-pills-JDBCDBREAD_TIMEOUT-tab" data-toggle="pill" href="#v-pills-JDBCDBREAD_TIMEOUT" role="tab" aria-controls="v-pills-JDBCDBREAD_TIMEOUT" aria-selected="false"> oracle.jdbc.ReadTimeout </a>
      <a class="nav-link" id="v-pills-JDBCDSendStreamAsBlob-tab" data-toggle="pill" href="#v-pills-JDBCDSendStreamAsBlob" role="tab" aria-controls="v-pills-JDBCDSendStreamAsBlob" aria-selected="false"> SendStreamAsBlob </a>
      <a class="nav-link" id="v-pills-JDBCDataSourceRuntimeMBeans-tab" data-toggle="pill" href="#v-pills-JDBCDataSourceRuntimeMBeans" role="tab" aria-controls="v-pills-JDBCDataSourceRuntimeMBeans" aria-selected="false"> Data Source Runtime </a>

      
    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-JDBCTarget" role="tabpanel" aria-labelledby="v-pills-JDBCTarget-tab"> """
      
print >>f, listResourceTargetTable ( "id_00023331000" , "domainConfig", "JDBCSystemResources", 'Targets')
      
print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCConnectionPoolParams" role="tabpanel" aria-labelledby="v-pills-JDBCConnectionPoolParams-tab">"""
      
print >>f,  listValuesVerticalCheck ("id_264369809891" , "domainConfig", "JDBCSystemResources", "JDBCResource", "JDBCConnectionPoolParams")
print >>f,  listValuesHorizontalCheck ("id_228678464" , "domainConfig", "JDBCSystemResources", "JDBCResource",  "JDBCConnectionPoolParams")


print >>f, """

      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDataSourceParams" role="tabpanel" aria-labelledby="v-pills-JDBCDataSourceParams-tab"> """
      
print >>f,  listValuesVerticalCheck ("id_22999456891" , "domainConfig", "JDBCSystemResources", "JDBCResource", "JDBCDataSourceParams")
print >>f,  listValuesHorizontalCheck ("id_28756646464" , "domainConfig", "JDBCSystemResources", "JDBCResource",  "JDBCDataSourceParams")
      
print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDriverParams" role="tabpanel" aria-labelledby="v-pills-JDBCDriverParams-tab"> """
      
print >>f,  listValuesVerticalCheck ("id_2296795449891" , "domainConfig", "JDBCSystemResources", "JDBCResource", "JDBCDriverParams")
print >>f,  listValuesHorizontalCheck ("id_2435245464" , "domainConfig", "JDBCSystemResources", "JDBCResource",  "JDBCDriverParams")
      
print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCOracleParams" role="tabpanel" aria-labelledby="v-pills-JDBCOracleParams-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_2467989891" , "domainConfig", "JDBCSystemResources", "JDBCResource", "JDBCOracleParams")
print >>f,  listValuesHorizontalCheck ("id_2769804" , "domainConfig", "JDBCSystemResources", "JDBCResource",  "JDBCOracleParams") 
      
print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCXAParams" role="tabpanel" aria-labelledby="v-pills-JDBCXAParams-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_2298076891" , "domainConfig", "JDBCSystemResources", "JDBCResource", "JDBCXAParams")
print >>f,  listValuesHorizontalCheck ("id_237804" , "domainConfig", "JDBCSystemResources", "JDBCResource",  "JDBCXAParams")

print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDBUser" role="tabpanel" aria-labelledby="v-pills-JDBCDBUser-tab"> """
      
print >>f,  listJDBCDBPropertiesCheck("id_2000005451258", "user") 


print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-oracle_net_CONNECT_TIMEOUT" role="tabpanel" aria-labelledby="v-pills-oracle_net_CONNECT_TIMEOUT-tab"> """
      
print >>f,  listJDBCDBPropertiesCheck("id_200000541359870", "oracle.net.CONNECT_TIMEOUT") 



print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDBREAD_TIMEOUT" role="tabpanel" aria-labelledby="v-pills-JDBCDBREAD_TIMEOUT-tab"> """
      
print >>f,  listJDBCDBPropertiesCheck("id_2000005459512365", "oracle.jdbc.ReadTimeout") 
# If oracle.net.READ_TIMEOUT in use then uncomment the below row and comment the above row
# print >>f,  listJDBCDBPropertiesCheck("id_200000545905123065", "oracle.net.READ_TIMEOUT") 
# for now we keep it as it is to emphasize the real value in use 


print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDSendStreamAsBlob" role="tabpanel" aria-labelledby="v-pills-JDBCDSendStreamAsBlob-tab"> """

print >>f,  listJDBCDBPropertiesCheck("id_20000852587913870", "SendStreamAsBlob") 
# If sendStreamAsBlob in use then uncomment the below row and comment the above row
#print >>f,  listJDBCDBPropertiesCheck("id_2000085258702913870", "sendStreamAsBlob")
# for now we keep it as it is to emphasize the real value in use 

print >>f, """      
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCDataSourceRuntimeMBeans" role="tabpanel" aria-labelledby="v-pills-JDBCDJDBCDataSourceRuntimeMBeansBUser-tab"> """
      
print >>f, listRuntimeValuesVerticalCheck ("id_2733333333478963" , "domainRuntime", "ServerRuntimes", "JDBCServiceRuntime", "JDBCDataSourceRuntimeMBeans" )
print >>f, listRuntimeValuesHorizontalCheck ("id_273333343111178963" , "domainRuntime", "ServerRuntimes", "JDBCServiceRuntime", "JDBCDataSourceRuntimeMBeans" )

      
print >>f, """      
      </div>
    </div>
  </div>
</div>

<!--  stop sub JDBC  tabs -->

</div>
<!-- **********************  -->

"""


print "Done printing the JDBC info.... "




print "Printing the JMS info.... "


print >>f, """

<div class="tab-pane fade" id="JMS" role="tabpanel" aria-labelledby="JMS-tab">
       
  <!--  start sub JMS tabs -->

<div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">JMS</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-JMSSystemResourcesTarget-tab" data-toggle="pill" href="#v-pills-JMSSystemResourcesTarget" role="tab" aria-controls="v-pills-JMSSystemResourcesTarget" aria-selected="true">  JMS System Resources Target </a>
      <a class="nav-link" id="v-pills-JMSSystemResources-tab" data-toggle="pill" href="#v-pills-JMSSystemResources" role="tab" aria-controls="v-pills-JMSSystemResources" aria-selected="false"> JMS System Resources </a>
      <a class="nav-link" id="v-pills-JMSServersTarget-tab" data-toggle="pill" href="#v-pills-JMSServersTarget" role="tab" aria-controls="v-pills-JMSServersTarget" aria-selected="false"> JMS Servers Target  </a>
      <a class="nav-link" id="v-pills-JMSServers-tab" data-toggle="pill" href="#v-pills-JMSServers" role="tab" aria-controls="v-pills-JMSServers" aria-selected="false"> JMS Servers</a>
      <a class="nav-link" id="v-pills-SAFAgentsTarget-tab" data-toggle="pill" href="#v-pills-SAFAgentsTarget" role="tab" aria-controls="v-pills-SAFAgentsTarget" aria-selected="false"> SAFAgents Target</a>
      <a class="nav-link" id="v-pills-SAFAgentsOverview-tab" data-toggle="pill" href="#v-pills-SAFAgentsOverview" role="tab" aria-controls="v-pills-SAFAgentsOverview" aria-selected="false"> SAFAgents </a>
      <a class="nav-link" id="v-pills-JMSSAFMessageLogFile-tab" data-toggle="pill" href="#v-pills-JMSSAFMessageLogFile" role="tab" aria-controls="v-pills-JMSSAFMessageLogFile" aria-selected="false"> JMSSAFMessageLogFile </a>
      <a class="nav-link" id="v-pills-SAFAgentsStore-tab" data-toggle="pill" href="#v-pills-SAFAgentsStore" role="tab" aria-controls="v-pills-SAFAgentsStore" aria-selected="false"> SAFAgents Store </a>
      

    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-JMSSystemResourcesTarget" role="tabpanel" aria-labelledby="v-pills-JMSSystemResourcesTarget-tab"> """
           
      
print >>f, listResourceTargetTable ( "id_0002339797925" , "domainConfig", "JMSSystemResources", 'Targets')
      
print >>f, """

      </div>
      <div class="tab-pane fade" id="v-pills-JMSSystemResources" role="tabpanel" aria-labelledby="v-pills-JMSSystemResources-tab">  """
      
print >>f,  listValuesVerticalCheck ("id_989895467891" , "domainConfig", "JMSSystemResources")
print >>f,  listValuesHorizontalCheck ("id_7979820964" , "domainConfig", "JMSSystemResources")
      
print >>f, """
      </div>
      <div class="tab-pane fade" id="v-pills-JMSServersTarget" role="tabpanel" aria-labelledby="v-pills-JMSServersTarget-tab"> """
           
      
print >>f, listResourceTargetTable ( "id_0021212121925" , "domainConfig", "JMSServers", 'Targets')
      
print >>f, """
     
      </div>
      <div class="tab-pane fade" id="v-pills-JMSServers" role="tabpanel" aria-labelledby="v-pills-JMSServers-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_414149809891" , "domainConfig", "JMSServers")
print >>f,  listValuesHorizontalCheck ("id_4565545646464" , "domainConfig", "JMSServers")
      
print >>f, """      
      </div>


      <div class="tab-pane fade" id="v-pills-SAFAgentsTarget" role="tabpanel" aria-labelledby="v-pills-SAFAgentsTarget-tab"> """
      
      
print >>f,  listResourceTargetTable ("id_41400211490091" , "domainConfig", "SAFAgents", "Targets")

      
print >>f, """      
      </div>

      <div class="tab-pane fade" id="v-pills-SAFAgentsOverview" role="tabpanel" aria-labelledby="v-pills-SAFAgentsTaSAFAgentsOverviewrget-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_414078990091" , "domainConfig", "SAFAgents")
print >>f,  listValuesHorizontalCheck ("id_0124590091" , "domainConfig", "SAFAgents")

      
print >>f, """      
      </div>

      <div class="tab-pane fade" id="v-pills-JMSSAFMessageLogFile" role="tabpanel" aria-labelledby="v-pills-JMSSAFMessageLogFile-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_23569878990091" , "domainConfig", "SAFAgents", "JMSSAFMessageLogFile" )
print >>f,  listValuesHorizontalCheck ("id_0122589630091" , "domainConfig", "SAFAgents", "JMSSAFMessageLogFile" )

      
print >>f, """      
      </div>

       <div class="tab-pane fade" id="v-pills-SAFAgentsStore" role="tabpanel" aria-labelledby="v-pills-SAFAgentsStore-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_2300990091" , "domainConfig", "SAFAgents", "Store" )
print >>f,  listValuesHorizontalCheck ("id_012012630091" , "domainConfig", "SAFAgents", "Store" )

      
print >>f, """      
      </div>     
   </div>  
    </div>
</div>

<!--  stop sub JMS  tabs -->

</div>

<!-- **********************  -->

"""

print "Done printing the JMS info.... "




print "Printing the Coherence info.... "


print >>f, """

<div class="tab-pane fade" id="Coherence" role="tabpanel" aria-labelledby="Coherence-tab">

 <!--  start sub Coherence tabs -->

 <div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">Coherence</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-CoherenceTarget-tab" data-toggle="pill" href="#v-pills-CoherenceTarget" role="tab" aria-controls="v-pills-CoherenceTarget" aria-selected="true">  Coherence Target</a>
      <a class="nav-link" id="v-pills-CoherenceOverview-tab" data-toggle="pill" href="#v-pills-CoherenceOverview" role="tab" aria-controls="v-pills-CoherenceOverview" aria-selected="false"> Coherence Overview</a>
      <a class="nav-link" id="v-pills-CoherenceClusterParams-tab" data-toggle="pill" href="#v-pills-CoherenceClusterParams" role="tab" aria-controls="v-pills-CoherenceClusterParams" aria-selected="false"> Coherence Cluster Params</a>
      


    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-CoherenceTarget" role="tabpanel" aria-labelledby="v-pills-CoherenceTarget-tab">  """
            

print >>f, listResourceTargetTable ( "id_5852581925" , "domainConfig", "CoherenceClusterSystemResources", "Targets")
      
print >>f, """      
      
      </div>
      <div class="tab-pane fade" id="v-pills-CoherenceOverview" role="tabpanel" aria-labelledby="v-pills-CoherenceOverview-tab"> """

print >>f,  listValuesVerticalCheck ("id_224546789100" , "domainConfig", "CoherenceClusterSystemResources")
print >>f,  listValuesHorizontalCheck ("id_78997896400" , "domainConfig", "CoherenceClusterSystemResources")
      
print >>f, """        
      </div>
      <div class="tab-pane fade" id="v-pills-CoherenceClusterParams" role="tabpanel" aria-labelledby="v-pills-CoherenceClusterParams-tab"> """
      
      
print >>f,  listValuesVerticalCheck ("id_00000989809891" , "domainConfig", "CoherenceClusterSystemResources", "CoherenceClusterResource", "CoherenceClusterParams")
print >>f,  listValuesHorizontalCheck ("id_00003646464" , "domainConfig", "CoherenceClusterSystemResources", "CoherenceClusterResource",  "CoherenceClusterParams")
      
print >>f, """      
      </div>
    </div>
  </div>
</div>

<!--  stop sub Coherence  tabs -->

</div>

<!-- **********************  -->

"""


print "Done printing the Coherence info.... "




print "Printing the Stores info.... "


print >>f, """

<div class="tab-pane fade" id="Stores" role="tabpanel" aria-labelledby="Stores-tab">  

 <!--  start sub Stores tabs -->

 <div class="row  ">
  <div class="col-1 ">
      <h2 class="font-weight-bold ">Stores</h2>
      <hr class="hr_title_sec ">
  <p></p>

    <div class="nav flex-column nav-pills sticky extraspace" id="v-pills-tab" role="tablist" aria-orientation="vertical">
      <a class="nav-link active" id="v-pills-FileStoresTarget-tab" data-toggle="pill" href="#v-pills-FileStoresTarget" role="tab" aria-controls="v-pills-FileStoresTarget" aria-selected="true">  File Stores Target</a>
      <a class="nav-link" id="v-pills-FileStoresOverview-tab" data-toggle="pill" href="#v-pills-FileStoresOverview" role="tab" aria-controls="v-pills-FileStoresOverview" aria-selected="false"> File Stores Overview</a>
      <a class="nav-link" id="v-pills-JDBCStoresTarget-tab" data-toggle="pill" href="#v-pills-JDBCStoresTarget" role="tab" aria-controls="v-pills-JDBCStoresTarget" aria-selected="false"> JDBC Stores Target</a>
      <a class="nav-link" id="v-pills-JDBCStoresOverview-tab" data-toggle="pill" href="#v-pills-JDBCStoresOverview" role="tab" aria-controls="v-pills-JDBCStoresOverview" aria-selected="false"> JDBC Stores Overview</a>

    </div>
  </div>

  <div class="col-9">
    <div class="tab-content tab-extra-content" id="v-pills-tabContent">
      <div class="tab-pane fade show active" id="v-pills-FileStoresTarget" role="tabpanel" aria-labelledby="v-pills-FileStoresTarget-tab">  """
      
print >>f, listResourceTargetTable ( "id_5878956021581925" , "domainConfig", "FileStores", "Targets")
      
print >>f, """      
      
      </div>
      <div class="tab-pane fade" id="v-pills-FileStoresOverview" role="tabpanel" aria-labelledby="v-pills-FileStoresOverview-tab"> """

print >>f,  listValuesVerticalCheck ("id_22000089100" , "domainConfig", "FileStores"  )
print >>f,  listValuesHorizontalCheck ("id_7898999997896400" , "domainConfig", "FileStores")
      
print >>f, """        
      </div>
      <div class="tab-pane fade" id="v-pills-JDBCStoresTarget" role="tabpanel" aria-labelledby="v-pills-JDBCStoresTarget-tab"> """
      
      
print >>f,  listResourceTargetTable ("id_00055565659809891" , "domainConfig", "JDBCStores", "Targets")
      
print >>f, """ 

</div>
<div class="tab-pane fade" id="v-pills-JDBCStoresOverview" role="tabpanel" aria-labelledby="v-pills-JDBCStoresOverview-tab"> """

print >>f,  listValuesVerticalCheck ("id_222235652789100" , "domainConfig", "JDBCStores")
print >>f,  listValuesHorizontalCheck ("id_120120178997896400" , "domainConfig", "JDBCStores")
      
print >>f, """        
      </div>
      </div>
    </div>
</div>

<!--  stop sub Stores  tabs -->

</div>

<!-- **********************  -->

"""


print "Done printing the Stores info.... ";



f.close(); 

# Disconnect WLST from WebLogic Server instance. 
disconnect() 
# disconnect(force)

print "Printing the OS info.... "

exit()


