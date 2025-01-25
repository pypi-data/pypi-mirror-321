def prac19():
    php_code = """
// Practical 18:

//  display.php

<!DOCTYPE html>
<html>
<head>
<title>Practical-22</title>
</head>
<body>
<center>
<h1>Details of Users</h1>
</center>
<table class="table table-dark">
<thead>
<tr>
<th>ID</th>
<th>Name</th>
<th>Number</th>
<th>City</th>
<th>Email</th>
<th>Password</th>
<th>Delete</th>
<th>Update</th>
</tr>
</thead>
<?php
include 'conn.php';
$q = "select * from practical";
$query = mysqli_query($con, $q);
while ($res = mysqli_fetch_array($query)) {
?>
<tr>
<td>
<?php echo $res['id']; ?>
</td>
<td>
<?php echo $res['name']; ?>
</td>
<td>

<?php echo $res['number']; ?>
</td>
<td>
<?php echo $res['city']; ?>
</td>
<td>
<?php echo $res['email']; ?>
</td>
<td>
<?php echo $res['password']; ?>
</td>
<td><button class="btn-danger btn"><a

href="delete.php?id=<?php echo $res['id']; ?>" class="text-
white">

Delete</a></button></td>
<td><button class="btn-primary btn"><a
href="update.php?id=<?php echo $res['id']; ?>"

class="text-
white">Update</a></button></td>

</tr>
<?php
}
?>
</table>
</body>
</html>
"""
    print(php_code)
