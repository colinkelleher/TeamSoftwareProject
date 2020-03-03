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


print_main('view_product.html', dict(items_html=items_html))
