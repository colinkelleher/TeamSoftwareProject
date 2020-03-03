from string import Template

start_nav = """
<nav class="dash-nav-list">
"""
end_nav = '</nav>'
bold = Template('<i class="${icon}"></i> ${title} ')
start_menu = """
        <div class="dash-nav-dropdown-menu">"""
end_menu = """
        </div>
"""

single_item = Template("""
    <a href="${link}" class="dash-nav-item">${name}</a>
    """)

link = Template("""
    <a href="${link}" class="dash-nav-dropdown-item">${name}</a>""")

dropdown = Template("""
    <div class="dash-nav-dropdown ">
        <a href="#!" class="dash-nav-item dash-nav-dropdown-toggle">${title}</a>
       ${content}
    </div>""")


def get_items(item, depth=0):
    title = item[0]
    links = item[1]
    if len(item) == 3:
        title = bold.safe_substitute(icon=item[1], title=title)
        links = item[2]
    if type(links) == str:
        if depth == 0:
            return single_item.safe_substitute(link=links, name=title)
        else:
            return link.safe_substitute(link=links, name=title)
    content = start_menu
    for i in links:
        content += get_items(i, depth+1)
    content += end_menu
    return dropdown.safe_substitute(title=title, content=content)


def get_nav(items):
    """
    Items is list of dictionaries fpr however many items you want in dropdown nav
    """
    nav = start_nav
    for item in items:
        nav += get_items(item)
    nav += end_nav
    return nav


if __name__ == '__main__':
    # Every item is a tuple (title, icon, link/list of links
    # If length is 2, don't set an icon
    simpler = [
        ('Home', 'fas fa-home', '${root}/index.py'),
        ('Charts', 'fas fa-home', [
            ('Charts.js', 'chartsjs.html')
        ]),
        ('Components', 'fas fa-home', [
            ('Cards', 'cards.html'),
            ('Forms', 'forms.html'),
            ('Icons', [
                ('Solid Icons', 'icons.html'),
                ('Regular Icons', 'icons.html#regular-icons'),
                ('Brand Icons', 'icons.html#brand-icons')
            ]),
            ('Stats', 'stats.html'),
            ('Tables', 'tables.html'),
            ('Typography', 'typography.html'),
            ('User Interface', 'userinterface.html')
        ]),
        ('Layouts', 'fas fa-home', [
            ('Blank', 'blank.html'),
            ('Content', 'content.html'),
            ('login.html', 'Log in'),
            ('Sign up', 'signup.html')
        ]),
        ('About', 'fas fa-home', [
            ('Github', 'https://github.com/HackerThemes/spur-template'),
            ('HackerThemes', 'http://hackerthemes.com')
        ])
    ]
    print(get_nav())
