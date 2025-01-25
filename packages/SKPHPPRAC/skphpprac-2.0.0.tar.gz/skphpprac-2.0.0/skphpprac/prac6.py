def prac6():
    php_code = """
6. Write a PHP program to read the employee detail using form component.

<html>

<body>
<form method="POST" action="pr6.php">
<fieldset>
<legend>Enter Employee Details.</legend>
<table width="250px" border="2" align="center">
<td align="right">
Enter Employee No : <input type=text
name="eno">
</td>
<br>
<td align="right">
Enter Employee Name : <input type=text
name="name">
</td>
<br>
<td align="right">
Enter Address : <input type=text
name="addr">
</td>
<br>
<td colspan="2" align="center">
<input type=submit value=Submit>
</td>
</table>
</fieldset>
</form>
</body>
</html>

<?php
session_start();
$_SESSION['eno'] = $_POST['eno'];
$_SESSION['name'] = $_POST['name'];
$_SESSION['addr'] = $_POST['addr'];
echo "Hello " . $_SESSION['name'] . " Welcome To Insure
World<br>";
?>
<form method="POST" action="pr6b.php">
<fieldset>
<legend>Enter Insurance details.</legend>
<table width="250px" border="2" align="center">
<td align="right">
Plan No:<input type="text" name="pno">
</td>
<br>
<td align="right">
Plan Name :<input type="text" name="pname">
</td>
<br>
<td align="right">
Premium :<input type="text" name="pre">
</td>
<br>
<td colspan="2" align="center">
<input type=submit value=Display>
</td>
</table>
</fieldset>
</form>
<?php
session_start();
echo "<Center>" . "<b>Employee Details</b>" . "<br>";
echo "Employee No:" . $_SESSION['eno'] . "<br>";
echo "Employee name:" . $_SESSION['name'] . "<br>";
echo "Address:" . $_SESSION['addr'] . "<br>" . "<hr>";

echo "<b>Insurance Plan Details:</b>" . "<br>";
echo "Plan No:" . $_REQUEST['pno'] . "<br>";
echo "Plan Name:" . $_REQUEST['pname'] . "<br>";
echo "Premium:" . $_REQUEST['pre'] . "<br>" . "<hr>";
?>

"""
    print(php_code)
