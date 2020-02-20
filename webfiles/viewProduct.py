#!/usr/bin/python3
from python.webpage_functions import print_main
from python.databases.databaseQueries import select_all

items = select_all("products")
items_html = """<section id='header'>
                    <span><b>ID</b></span>
                    <span><b>Title</b></span>
                    <!-- <span><b>Dessscription</b></span> -->
                    </section> """
for i in items:
    item = """<span>%d</span>
              <span>%s</span>
              <!-- <span>%s</span> -->""" % (i['id'], i['title'], i['description'])
    items_html += """<section class='item' onclick="getInfo(id=%s);">
                        %s
                     </section>""" % (i['id'], str(item))



html = """
<main>
    <section id="main">
        <img src="/images/locations/main.png" id="map">
        <section id="info">
            <h3>Product Information</h3>
            <table>
                <tr>
                    <th>ID</th><th>Title</th><th>Description</th><th>Comment</th>
                </tr>
                <tr>
                    <td id="id"></td><td id="title"></td><td id="description"></td>
                    <td>Comments coming soon</td>
                </tr>
            </table>
            <h3 id="linfo">Location Information</h3>
            <table>
                <tr>
                    <th>ID</th><th>Title</th><th colspan="2">Description</th><th></th>
                </tr>
                <tr>
                    <td id="lid"></td><td id="ltitle"></td><td id="ldescription" colspan="2"></td>
                </tr>
            </table>
            <!--
            <section id="admin">
                <h3>Admin</h3>
                <div>
                    <h5>Generate Print Out</h5>
                    <button onClick="generate()">Generate</button>
                    <p id="generate_message">
                </div>
                <div>
                    <h5>Delete</h5>
                    <button onClick="delete_prod()">Delete</button>
                    <p id="delete_message">
                </div>
            </section> -->
        </section>  
        <section id="right">
            %s
        </section>
    </section>
</main>
""" % items_html

style = """
<style>
    html, body {
        max-width: 100%;
        overflow-x: hidden;
        overflow-y: hidden;
    }
    #main{
        height:100%;
        width:100%;
        display: grid;
        grid-template-columns: 1fr 2fr 0.5fr;
    }
    #right{
        height: 1000px;
        float:right;
        grid-column:3;
        background-color:lightgrey;
        overflow: scroll;
    }
    img{
         padding:0;
         margin:0;
         grid-column:1;
         display:inline;
         width:100%;
         height: 700px;
    }
    .item{
        padding:5px;
        width:100%;
        display:grid;
        grid-template-columns: 1fr 1fr 1fr;
        border-top:2px solid black;
    }
    .item:hover{
        background-color: darkgrey;
    }
    #header{
        width:100%;
        display:grid;
        grid-template-columns: 1fr 1fr 1fr;
    }
    #info{
        text-align: center;
        grid-column:2;
        display:inline;
        width: 450px;
    }
    table{
        width:100%;
        text-align: center;
    }
    tr{
        padding:2em;
    }
    tr *{
         padding-left: 1em;
    }
    
    #admin{
        position: absolute;
        bottom: 10%;
    }
    
    #linfo{
        margin-top: 40%;
    }
    
    h3{
        text-align:center;
    }
    
</style>
"""

javascript = """
<script>
    function getInfo(id){
        console.log(id);
        
        var xhttp1 = new XMLHttpRequest();
        xhttp1.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var json = JSON.parse(this.responseText);
                console.log(json.location_info)
                document.getElementById("id").innerHTML = json.id;
                document.getElementById("title").innerHTML = json.title;
                document.getElementById("description").innerHTML = json.description;
                document.getElementById("lid").innerHTML = json.location_info.id;
                document.getElementById("ltitle").innerHTML = json.location_info.title;
                document.getElementById("ldescription").innerHTML = json.location_info.description;

            }
        };
        xhttp1.open("GET", "/api/get_product_info.py?pid="+id, true);
        xhttp1.send();
        
        
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var map = document.getElementById("map").src = this.responseText;
                

            }
        };
        xhttp.open("GET", "/api/get_product_map.py?pid="+id, true);
        xhttp.send();
        
        
    }
    
    function generate(){ 
        var message = document.getElementById("generate_message").innerHTML = "Print out is being \
                      generated. It will be available <a href='#'>Here</a> in a few seconds" 
    }
    
    function delete_prod(){ 
        if (confirm('Are you sure you want to save this thing into the database?')) {
            var message = document.getElementById("delete_message").innerHTML = "This has been deleted. Refresh to stop seeing it" 
        }else {
            return;
        }
    } 
    
    </script> """


print_main(html + style + javascript)
