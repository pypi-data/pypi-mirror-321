def prac17():
    php_code = """
17. Write a PHP Program for Session and Cookies.

// Pr17s.php
<?php
$_SESSION["favcolor"] = "green";
$_SESSION["favanimal"] = "cat";
?>
<!DOCTYPE html>
<html>
<body>
<?php
// Echo session variables that were set on previous page
echo "Favorite color is " . $_SESSION["favcolor"] .
".<br>";
echo "Favorite animal is " . $_SESSION["favanimal"] . ".";
?>
</body>
</html>


// Pr17c.php
<?php
setcookie("test_cookie", "test", time() + 3600, '/');
?>
<html>
<body>
<?php
if (count($_COOKIE) > 0) {
echo "Cookies are enabled.";
} else {
echo "Cookies are disabled.";
}
?>
</body>
</html>
"""
    print(php_code)
