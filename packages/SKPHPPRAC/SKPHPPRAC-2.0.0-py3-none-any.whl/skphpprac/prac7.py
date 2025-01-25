def prac7():
    php_code = """
7. Write a PHP program to demonstrate the use of array.
<?php
$gm = array("BCA", "PGDCA", "MSCIT");
echo "I like" . $gm[0] . "," . $gm[1] . "and" . $gm[2] . ".";
echo "<br/><br/>";
$gm[0] = "BCA";
$gm[1] = "PGDCA";
$gm[2] = "MSCIT";
echo "I like" . $gm[0] . "," . $gm[1] . "and" . $gm[2] . ".";
echo "<br/><br/> Elements in Array:";
$arrsize = count($gm);
for ($cnt = 0; $cnt < $arrsize; $cnt++) {
echo "<br/>";
echo "<b>" . $gm[$cnt] . "</b>";
}
?>
"""
    print(php_code)
