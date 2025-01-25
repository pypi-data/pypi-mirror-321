def prac2():
    php_code = """
<?php
// Practical 2: Write a PHP program to display the today's date and current time.

print strftime('%c');
echo "<br/>";
print strftime('%d/%m/%Y');
echo "<br/>";
print strftime('%A,%d%B-%Y');
echo "<br/>";
echo "<b> Current Day date and time is:</b>" . date("D M d, Y
G:i A");

?>
"""
    print(php_code)
