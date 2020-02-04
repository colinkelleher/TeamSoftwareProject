#!/usr/bin/python3
from cgi import FieldStorage
from python.login import *
from python.html_components import *
from python.databases.databaseQueries import select_all

print('Content-Type: text/html')
print()
print_head()
print_nav()

try:
    items = select_all("products")
    items_html = """<section id='header'>
                        <span><b>ID</b></span>
                        <span><b>Title</b></span>
                        <span><b>Description</b></span>
                        </section>"""
    for i in items:
        item = """<span>%d</span>
                  <span>%s</span>
                  <span>%s</span>""" % (i[0], i[1], i[2])
        items_html += """<section class='item' onclick="getInfo(id=%s);">
                            %s
                         </section>""" % (i[0], str(item))


except Exception as e:
    print(e)

html = """
<main>
    <section id="main">
        <img src="/TeamSoftwareProject/images/locations/main.png" id="map">
        <section id="info">
            <h3>Product Information</h3>
            <table>
                <tr>
                    <th>ID</th><th>Title</th><th>Description</th><th>Comment</th>
                </tr>
                <tr>
                    <td>1</td><td>Cod</td><td>Some smelly cod</td><td>Comment here. long comment 12345</td>
                </tr>
            </table>
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
            </section>
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
        padding-left:230px;
        display: grid;
        grid-template-columns: 1fr 1fr 0.75fr;
    }
    #right{
        float:right;
        grid-column:3;
        background-color:lightgrey;
        overflow: scroll;
    }
    img{
         display:inline;
         height:100%;
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
        grid-column:2;
        display:inline;
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
    
</style>
"""

javascript = """
<script>
    function getInfo(id){
        console.log(id);
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                var map = document.getElementById("map").src = this.responseText;
                

            }
        };
        xhttp.open("GET", "/TeamSoftwareProject/api/get_product_map.py?pid="+id, true);
        xhttp.send();
    }
    
    function generate(){ 
        var message = document.getElementById("generate_message").innerHTML = "Print out is being \
                      generated. It will be available <a href='#'>Here</a> in a few seconds" 
    }
    
    function delete_prod(){ 
        if (confirm('Are you sure you want to save this thing into the database?')) {
            var message = document.getElementById("delete_message").innerHTML = "This has been deleted" 
        }else {
            return;
        }
    } 
    
    </script> """
print(html, style, javascript)
