def prac13():
    php_code = """
13. Write a PHP Program to Validate Input Data

<html>

<head>
<title>Practical-13</title>
</head>
<body>
<?php
$name = $email = $gender = $comment = $website = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
$name = test_input($_POST["name"]);
$email = test_input($_POST["email"]);
$gender = test_input($_POST["gender"]);
}
function test_input($data)
{
$data = trim($data);
$data = stripslashes($data);
$data = htmlspecialchars($data);
return $data;
}
?>
<h2>PHP Form Validate Input Data</h2>
<form method="post" action='<?php echo
htmlspecialchars($_SERVER["PHP_SELF"]);?>'>
Name:
<input type="text" name="name">
<br><br>
E-mail:
<input type="email" name="email">
<br><br>
Gender:
<input type="radio" name="gender" value="female">Female
<input type="radio" name="gender" value="male">Male
<input type="radio" name="gender" value="other">Other
<br><br>

<input type="submit" name="submit" value="Submit">
</form>
<?php
echo "<h2>Your Input:</h2>";
echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $gender;
?>
</body>
</html>

"""
    print(php_code)
