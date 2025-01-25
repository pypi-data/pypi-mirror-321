def prac11():
    php_code = """
11. Write a PHP Program for Create, Delete, and Copying βile from PHP Script.

<html>

<head>
<title>Practical-11</title>
</head>
<body>
<h1>For Create File</h1>
<form action="create.php" method="post" name="filehand">
Enter File Name<br>
<input type="text" name="filename"><br>
<input type="submit" name="createfile" value="Create
File" />
</form>
<hr>
<h1>For Copy File</h1>
<form action="copy.php" method="post" name="filehand">
Enter File Name Here<br>
<input type="text" name="filename"><br>
Enter New File name to copy file and press copy
button<br>
<input type="text" name="newfilenm"><br>
<input type="submit" name="copyfile" value="Copy File">
</form>
<hr>
<h1>For Delete File</h1>
<form action="delete.php" method="post" name="filehand">
Enter File Name for delete file<br>
<input type="text" name="deletefilenm"><br>
<input type="submit" name="deletefile" value="Delete
File" />
</form>
<hr>
</body>
</html>

//copy PHP

<?php
$filename = $_REQUEST['filename'];
$newfile = $_REQUEST['newfilenm'];
if (isset($_REQUEST['copyfile'])) {
if (file_exists($filename)) {
if (file_exists($newfile)) {
echo "Destination File Name Already Exist.....";
} else {
copy($filename, $newfile);
echo "File Successfully Copied.....";
}
} else {
echo "File Does not exist";
}
}
?>

//Create php
<?php
$filename = $_REQUEST['filename'];
if (isset($_REQUEST['createfile'])) {
if (file_exists($filename)) {
echo "The file $filename exists";
} else {
$handle = fopen($filename, 'w') or die('Cannot open
file' . $filename);
if (file_exists($filename)) {
echo "The $filename file Successfully Created";
} else {
echo "Error Creating file $filename";
}
}
}
?>

//Delete PHP
<?php
$delfile = $_REQUEST['deletefilenm'];
if (isset($_REQUEST['deletefile'])) {
if (file_exists($delfile)) {
unlink($delfile);
if (file_exists($delfile)) {
echo "File Not Deleted";
} else {
echo "File Deleted Successfully";
}
} else {
echo "File Does Not Exists....";
}
}
?>

"""
    print(php_code)
