# # from django.test import TestCase






# # Create your tests here.
# {% extends "base.html" %}
# {% block content %} 
# <body>
    
#     <br>
#     <div class="text" style="font-size: xx-large; color: rgb(227, 236, 253); background-color: rgb(218, 153, 32);"> You searched for: '{{ searched }}'
#     </div>
#          <div class="card-header py-3">
#             <i class="fas fa-table me-1"></i>
#             Results Found: 
#         </div>
#         <div class="card-body">
#             <!-- <table id="datatablesSimple"> -->
#                 <!-- <div class="table-responsive"> -->

#                 <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">


#                 <thead>
#                     <tr>
                     
#                         <th style="background-color: rgb(114, 93, 235);">Rooms</th>
#                         <th style="background-color: rgb(114, 93, 235);">Floor</th>
#                         <th style="background-color: rgb(114, 93, 235);">Property Type</th>
#                         <th style="background-color: rgb(114, 93, 235);">Square Meters</th>
#                         <th style="background-color: rgb(114, 93, 235);">City</th>
#                         <th style="background-color: rgb(114, 93, 235);">Street</th>
#                         <th style="background-color: rgb(114, 93, 235);">Neighbourhood</th>
#                         <th style="background-color: rgb(114, 93, 235);">Price</th>
#                     </tr>
#                 </thead>
#                 <tbody>    
#                   {% for proj in A_property %}
#                   <tr >
#                       <th>{{ proj.room }}</th>
#                       <th>{{ proj.floor }}</th>
#                       <th>{{proj.property_type}}</th>
#                       <th>{{proj.square_meter}}</th>
#                       <th>{{proj.location}}</th>
#                       <th>{{proj.street}}</th>
#                       <th>{{proj.neighbourhood}}</th>
#                       <th>{{proj.price}}</th>
#                   </tr> 
#                   {% endfor %}
#                       </tbody>


                    
#                 </div>
          
  

            
                
#             </div>


           
#             <!-- <div class="card-body"> -->
               
#                     <thead>
                        
#                         <tr>
                            
#                             <th style="background-color: rgb(182, 86, 211);">Project type</th>
#                             <th style="background-color: rgb(182, 86, 211);">Size</th>
#                             <th style="background-color: rgb(182, 86, 211);">Company</th>
#                             <th style="background-color: rgb(182, 86, 211);">Value</th>
#                             <th style="background-color: rgb(182, 86, 211);">City</th>
#                             <th style="background-color: rgb(182, 86, 211);">Neighbourhood</th>
#                             <!-- <th style="background-color: rgb(182, 86, 211);">Street Number</th> -->
#                             <th style="background-color: rgb(182, 86, 211);">Dates</th>
#                         </tr>
#                     </thead>
#                     <tbody>    

#                       {% for proj in B_projects %}
#                       <tr >
#                           <th>{{ proj.type_project }}</th>
#                           <th>{{ proj.size_project }}</th>
#                           <th>{{proj.company}}</th>
#                           <th>{{proj.value}}</th>
#                           <th>{{proj.location}}</th>
#                           <!-- <th>{{proj.street}}</th> -->
#                           <th>{{proj.neighbourhood}}</th>
#                           <th>{{proj.dates}}</th>
#                       </tr> 
#                       {% endfor %}
#                           </tbody>
    
      
#                         </table>
#                     </div>
#                     <!-- <script src="js/demo/datatables-demo.js"></script>
#                      -->
#                     <script src="../../static/js/datatables-simple-demo.js"></script>
#                      <!-- Bootstrap core JavaScript-->
#                     <!-- <script src="vendor/jquery/jquery.min.js"></script> -->
#                     <script src="../../static/vendor/jquery/jquery.min.js"></script>
#                     <script src="../../static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

#                     <!-- Core plugin JavaScript-->
#                     <script src="../../static/vendor/jquery-easing/jquery.easing.min.js"></script>

#                     <!-- Custom scripts for all pages-->
#                     <!-- <script src="../../static/js/sb-admin-2.min.js"></script> -->
#                     <script src="../../static/js/"></script>

#                     <!-- Page level plugins -->
#                     <script src="../../static/vendor/datatables/jquery.dataTables.min.js"></script>
#                     <script src="../../static/vendor/datatables/dataTables.bootstrap4.min.js"></script>

                    
#                     <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
#                     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.min.js" integrity="sha384-cuYeSxntonz0PPNlHhBs68uyIAVpIIOZZ5JqeqvYYIcEL727kskC66kF92t6Xl2V" crossorigin="anonymous"></script>        
#                     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
# </body>
# {% endblock %}  
# </html>