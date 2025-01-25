def prac23():
    php_code = """
// 23. Write down steps to install joomla on local server.
Joomla Content Management System (CMS) is easy to install. No maƩer what server
operaƟng system you’re running, Joomla’s installaƟon process walks you through all the
steps.
Before you install Joomla, set up the Joomla environment. The easiest way to do this is with
XAMPP.
Once you have XAMPP installed, follow these steps to install Joomla:
Step-1: Click the Download buƩon on Joomla’s page.
Step-2: Download the compressed .zip or .tar.gz file, as appropriate for your operaƟng
system.
Step-3: Uncompress the Joomla files to the htdocs directory, or create a subdirectory of
htdocs and then copy the uncompressed files to that subdirectory. Your newly installed
XAMPP directory contains a subdirectory named htdocs, which is where you put the files
you want to access when you navigate to hƩp ://localhost in your browser.
Step-4: Open your browser, and navigate to hƩp ://localhost or hƩp ://localhost/xxxx
(where xxxx is the name of the subdirectory you created in Step 3). The first Joomla
installaƟon page appears.
Step-5: Select a language.
Step-6: Click Next.
Step-7: All items in the top pane of Pre-InstallaƟon Check page should read Yes. If you don’t
see Yes for any item, contact your ISP’s technical support department). This page also
displays a list of recommended seƫngs. If you’re installing Joomla on an ISP’s server, you
don’t have a heck of a lot of choice about these seƫngs, because the ISP’s tech staff
determines them.
Step-8: Click Next.
Step-9: Review the license and click Next to accept the terms. The Database ConfiguraƟon
page comes up. Here are the seƫngs you have to make in this page, along with brief
explanaƟons: Database Type: Choose MySQLi. Host Name: Enter localhost. User Name: In
this text box, enter the default MySQL username root. Password: Enter the password.
Database Name: Enter the name you used when you set up your database.
Step-10: Click Next.
Step-11: Click next to skip the FTP configuraƟon. The Main ConfiguraƟon page appears.
Step-12: Enter the name of your new Joomla site in the Site Name text box. This name will
appear when you log in as an administrator.

Step-13: Enter an administrator e-mail address in the Your E-Mail text box. When you log
into your new site, you’ll be the super user. The super user has maximum control of the site.
You can create several super users, but you can’t delete a super-user account. However, you
can demote the account to a lower site permission level and then delete it.
Step-14: Enter and then confirm the administrator password you want to use. Joomla gives
you the opƟon of installing some sample data to see how the site works, and unless you’re
an experienced Joomla user, you should definitely do that.
Step-15: Select the Install Default Sample Data buƩon; then click the Install Sample Data
command buƩon. When you complete this step, the Install Sample Data buƩon changes to
the Sample Data Installed Successfully buƩon.
Step-16: Click Next.
Step-17: Remove the installaƟon directory. To delete the Joomla installaƟon directory,
connect to your site by using your FTP program, and delete the directory there.
Step-18: Click the Site buƩon to visit your new Joomla site or click the Admin buƩon to go
to the administrator control panel.
"""
    print(php_code)
