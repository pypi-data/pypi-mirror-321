def prac3():
    php_code = """
<?php
// 3. Write a PHP program to display the Fibonacci series
$count = 0;
$no1 = 0;
$no2 = 1;
$tot = 0;
while ($count <= 10) {
echo $tot . "<br/>";
$no1 = $no2;
$no2 = $tot;
$tot = $no1 + $no2;
$count++;
}
?>
"""
    print(php_code)
