def prac8():
    php_code = """
8. Write a PHP program to prepare student Mark sheet using Switch statement.
<html>
<head>
<title>Practical-8</title>
</head>
<body>
<form name="frmdemo" action="pr8.php" method="post">
<fieldset>
<legend align="center">
Enter Your Name with Marks Detail
</legend>
<table width="250px" border="2" align="center">
<tr>
<td align="right">Your Name</td>
<td><input type="text" name="txtname"></td>
</tr>
<tr>
<td align="right">Roll No.</td>
<td><input type="text" name="txtrnum"></td>
</tr>
<tr>
<td align="right">OOPL C++</td>
<td><input type="text" name="txtsub1"></td>
</tr>
<tr>
<td align="right">PHP</td>
<td><input type="text" name="txtsub2"></td>
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
$rnum = $_REQUEST['txtrnum'];
$sub1 = $_REQUEST['txtsub1'];
$sub2 = $_REQUEST['txtsub2'];
echo "<b>Your Name is:</b>" . $name . "<br/>";
echo "<b>Your Roll No is:</b>" . $rnum . "<br/>";
echo "<b>Your Marks Details:</b><br>";
echo "OOP C++(BCA-401):" . $sub1 . "<br/>";
echo "PHP(BCA-402):" . $sub2 . "<br/>";
$total = $sub1 + $sub2 ;
echo "Total Marks" . $total . "<br/>";
$per = $total / 2;
echo "Percentage:" . $per . "%<br/>";

switch ($per) {
case $per < 35:
echo "Grade:F" . "<br/>";
break;
case $per >= 35 && $per <= 50:
echo "Grade:D" . "<br/>";
break;
case $per > 50 && $per <= 60:
echo "Grade:C" . "<br/>";
break;
case $per > 60 && $per <= 70:
echo "Grade:B" . "<br/>";
break;
case $per > 70 && $per < 100:
echo "Grade:A" . "<br/>";
break;
default:
echo "Invalid..... or out of limit";
}
} else {
echo "Go Back and Press submit button";
}
?>
"""
    print(php_code)
