def prac26():
    php_code = """
26. Create basic Joomla Template.
CreaƟng a basic index.php file
The index.php file becomes the core of every page that Joomla! delivers. EssenƟally, you
make a page (like any HTML page) but place PHP code where the content of your site should
go. The template works by adding Joomla code into module posiƟons and the component
secƟon in your template. Anything added to the template will appear on all pages unless it
is added to one of these secƟons via the Joomla CMS (or customised code). This page will
show the bare-bones code ready for you to cut and paste into your own design.
Head
The first line gets Joomla to put the correct header informaƟon in. This includes the page
Ɵtle, meta informaƟon as well as system JavaScript. The rest creates links to two system
style sheets and to your own style sheet (if it's named template.css and is located in the css
folder of your template directory. So if your template is in hƩp
://www.mysite.com/templates/my_template/ then the css files will go in hƩp
://www.mysite.com/templates/my_template/css/).
Body SecƟon
Amazingly, this will suffice! Yes, it's a very basic layout, but it will do the job. Everything else
will be done by Joomla!. These lines, usually called jdoc statements, tell Joomla to include
output from certain parts of the Joomla system. Note: you will need to ensure your menu is
set to go into the "top" module posiƟon.
Module PosiƟons
Above, the line which says name="top" adds a module posiƟon called top and allows
Joomla to place modules into this secƟon of the template. The type="component" line
contains all arƟcles and main content (actually, the component) and is very important. It
goes in the centre of the template.
Custom Images
If you want to add any images to the template you can do.
Custom CSS
TesƟng the template
Find the template in the Template Manager, select it and click Default to make it the default
template.
"""
    print(php_code)
