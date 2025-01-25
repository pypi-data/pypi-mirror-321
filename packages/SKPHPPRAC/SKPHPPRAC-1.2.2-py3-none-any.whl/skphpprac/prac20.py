def prac20():
    php_code = """
// Practical 20: //delete.php
<?php
include 'conn.php';
$id = $_GET['id'];
$q = "DELETE FROM `practical` WHERE id = $id";
mysqli_query($con, $q);
header('location:display.php')
?>
"""
    print(php_code)
