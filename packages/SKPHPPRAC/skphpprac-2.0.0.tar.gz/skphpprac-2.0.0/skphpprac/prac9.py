def prac9():
    php_code = """
9. Write a PHP program to generate the multiplication of matrix.

<html>

<head>
<title>Practical-9</title>
</head>
<body>
<center>
<form name="matrix" action="pr9.php" method="get">
<table border="2" cellpadding="2" cellspacing="3">
<caption><b>Please Enter 3x3
Matrix</b></caption>
<tr>
<td rowspan="3">Matrix-A</td>
<td>
<input type="text" name="a11"
style="width: 50px">
</td>
<td>
<input type="text" name="a12"
style="width: 50px">
</td>
<td>
<input type="text" name="a13"
style="width: 50px">
</td>
<tr>
<td>
<input type="text" name="a21"
style="width: 50px">
</td>
<td>
<input type="text" name="a22"
style="width: 50px">
</td>

<td>
<input type="text" name="a23"
style="width: 50px">
</td>
</tr>
<tr>
<td>
<input type="text" name="a31"
style="width: 50px">
</td>
<td>
<input type="text" name="a32"
style="width: 50px">
</td>
<td>
<input type="text" name="a33"
style="width: 50px">
</td>
</tr>
<tr>
<td rowspan="3">Matrix-B</td>
<td>
<input type="text" name="b11"
style="width: 50px">
</td>
<td>
<input type="text" name="b12"
style="width: 50px">
</td>
<td>
<input type="text" name="b13"
style="width: 50px">
</td>
</tr>
<tr>
<td>
<input type="text" name="b21"
style="width: 50px">

</td>
<td>
<input type="text" name="b22"
style="width: 50px">
</td>
<td>
<input type="text" name="b23"
style="width: 50px">
</td>
</tr>
<tr>
<td>
<input type="text" name="b31"
style="width: 50px">
</td>
<td>
<input type="text" name="b32"
style="width: 50px">
</td>
<td>
<input type="text" name="b33"
style="width: 50px">
</td>
</tr>
<tr>
<td align="center" colspan="4">
<input type="submit" name="submit"
value="submit">
</td>
</tr>
</table>
</form>
</center>
</body>
</html>



<?php
if (isset($_REQUEST['submit'])) {
$a = array();
$a[] = array($_REQUEST['a11'], $_REQUEST['a12'],
$_REQUEST['a13']);
$a[] = array($_REQUEST['a21'], $_REQUEST['a22'],
$_REQUEST['a23']);
$a[] = array($_REQUEST['a31'], $_REQUEST['a32'],
$_REQUEST['a33']);
$b = array();
$b[] = array($_REQUEST['b11'], $_REQUEST['b12'],
$_REQUEST['b13']);
$b[] = array($_REQUEST['b21'], $_REQUEST['b22'],
$_REQUEST['b23']);
$b[] = array($_REQUEST['b31'], $_REQUEST['b32'],
$_REQUEST['b33']);
echo "Matrix-A<br/>";
dispmatrix(3, $a);
echo "<br/>";

echo "Matrix-B<br/>";
dispmatrix(3, $b);
echo "<br/>";
$r = matrixMultiply(3, $a, $b);
echo "Matrix Multiplication<br/>";
dispmatrix(3, $r);
echo "<br/>";
} else {
header('localion:practical9.php');
}
function dispmatrix($N, $r)
{
for ($i = 0; $i < $N; $i++) {
for ($j = 0; $j < $N; $j++) {
if ($j == $N) {
echo "<br/>";
} else {
echo $r[$i][$j];
}
if ($j < ($N - 1)) {
echo ",";
}
}
}
}
function matrixMultiply($N, $a, $b)
{
$r = array();
for ($i = 0; $i < $N; $i++) {
$t[] = array();
for ($j = 0; $j < $N; $j++) {
$t[] = 0;
}
$r[] = $t;
}
for ($i = 0; $i < $N; $i++) {
for ($j = 0; $j < $N; $j++) {

$t = 0;
for ($k = 0; $k < $N; $k++) {
$t += $a[$i][$k] * $b[$k][$j];
}
$r[$i][$j] = $t;
}
}
return $r;
}
?>
"""
    print(php_code)
