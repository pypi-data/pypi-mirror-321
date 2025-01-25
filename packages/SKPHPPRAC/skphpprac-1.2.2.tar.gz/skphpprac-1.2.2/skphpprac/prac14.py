def prac14():
    php_code = """
14. Write a PHP Program to Upload File.
<?php
if (isset($_POST['upload'])) {
$file_name = $_FILES['file']['name'];
$file_type = $_FILES['file']['size'];
$file_size = $_FILES['file']['type'];
$file_tem_loc = $_FILES['file']['tmp_name'];
$file_store = "upload/" . $file_name;
move_uploaded_file($file_tem_loc, $file_store);
echo "File Upload Succesfully $file_name";
} else {
echo "Something Wrong";
}
?>
<html>
<head>
<title>Practical-14</title>
</head>
<body>
<h3>Practical-14</h3>

<form action="?" method="post" enctype="multipart/form-
data">

<input type="file" name="file">
<br><br>
<input type="submit" name="upload" value="Upload
Image">
</form>
</body>
</html>
"""
    print(php_code)
