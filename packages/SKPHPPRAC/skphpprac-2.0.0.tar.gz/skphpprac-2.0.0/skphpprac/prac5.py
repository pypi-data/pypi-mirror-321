def prac5():
    php_code = """
    
5. Write a PHP Program that will use the concept form.

<html>
<head>
<title>Practical-5 form concept</title>
</head>
<body>
<form name="frmdemo" action="pr5.php" method="post">
<fieldset>
<legend>Enter Your Details.</legend>
<table width="250px" border="2" align="center">
<tr>
<td align="right">Name</td>
<td><input type="text" name="txtname">
</td>
</tr>
<tr>
<td align="right">Contact No.</td>
<td><input type="text" name="txtcno">
</td>
</tr>
<tr>
<td colspan="2" align="center">
<input type="submit" name="submit"
value="submit">
</td>
</tr>
</table>
</fieldset>
</form>
</body>
</html>


<?php
if (isset($_REQUEST['submit'])) {
$name = $_REQUEST['txtname'];
$cno = $_REQUEST['txtcno'];
echo "<b>Your Name is:</b>" . $name;
echo "<br/>";
echo "<b>Your Contact No:</b>" . $cno;
} else {
echo "Go Back and Press submit Button"; }
?>
"""
    print(php_code)
