from python.webpage_functions import get_html_template, user
from string import Template
from bs4 import BeautifulSoup

start_nav = """
<nav class="dash-nav-list">
    <a href="${root}/index.py" class="dash-nav-item">
         <i class="fas fa-home"></i> Home </a>
"""
end_nav = '</nav>'
bold = '<i class="${icon}"></i>'
start_menu = """
        <div class="dash-nav-dropdown-menu">"""
end_menu = """
        </div>
"""

link = Template("""
    <a href="${link}" class="dash-nav-dropdown-item">${name}</a>""")

dropdown = Template("""
    <div class="dash-nav-dropdown ">
        <a href="#!" class="dash-nav-item dash-nav-dropdown-toggle">${title}</a>
       ${content}
    </div>""")


def get_item(title, item, toplevel=True):
    if toplevel:
        title = '%s %s ' % (bold, title)
    # item could be empty list, list of (tuples (link, name) or another dictionary)
    if len(item) == 0:
        return dropdown.safe_substitute(title=title, content="")
    content = ""
    for i in item:
        content += start_menu
        if type(i) == tuple or type(i) == list:
            href, name = i
            content += link.substitute(link=href, name=name)
        else:
            for t, j in i.items():
                content += get_item(t, j, False)
        content += end_menu
    return dropdown.safe_substitute(title=title, content=content)


def get_nav():
    """
    Items is list of dictionaries fpr however many items you want in dropdown nav
    """
    items = user.get_nav_items()
    nav = start_nav
    for title, item in items.items():
        nav += get_item(title, item)
    nav += end_nav
    return nav


if __name__ == '__main__':
    """
    So dictionary where each key is the title of nav item
    Then the item is a list
        - If the first item is a string, it's used as the nav item image class
        - If it's a tuple (href, name), it's the expanded nav item link and name
        - If it's another dictionary, everythings recursive
        - Need to do - if tuple of length one, it's not dropdown nav item, just single button
    """
    items = {
        'Charts': [
            'fas fa-home',
            ('chartsjs.html', 'Charts.js')
        ],
        'Components': [
            'fas fa-home',
            ('cards.html', 'Cards'),
            ('forms.html', 'Forms'),
            {'Icons': [
                ('icons.html', 'Solid Icons'),
                ('icons.html#regular-icons', 'Regular Icons'),
                ('icons.html#brand-icons', 'Brand Icons')
            ]},
            ('stats.html', 'Stats'),
            ('tables.html', 'Tables'),
            ('typography.html', 'Typography'),
            ('userinterface.html', 'User Interface')
        ],
        'Layouts': [
            'fas fa-home',
            ('blank.html', 'Blank'),
            ('content.html', 'Content'),
            ('login.html', 'Log in'),
            ('signup.html', 'Sign up')
        ],
        'About': [
            'fas fa-home',
            ('https://github.com/HackerThemes/spur-template', 'Github'),
            ('http://hackerthemes.com', 'HacketThemes')
        ]
    }
    print(get_nav())
