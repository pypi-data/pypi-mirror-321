def prac22():
    php_code = """
// Practical 22: //update.php

<?php
include 'conn.php';
if (isset($_POST['done'])) {
$id = $_GET['id'];
$name = $_POST['name'];
$number = $_POST['number'];
$city = $_POST['city'];

$email = $_POST['email'];
$password = $_POST['password'];
$q = "UPDATE practical set id=$id, name='$name',
number='$number',city='$city',email='$email',password='$passwor
d' where id=$id";
$query = mysqli_query($con, $q);
}
?>
<html>

<head>
<title>Registration Of User</title>
</head>
<body>
<center>
<h1>Modify Of User Details</h1>
<br>
<section class="my-2">
<div class="py-3">
<div class="container">
<form method="post">
<div class="form-group">
<label
for="exampleInputText">ID(Assign Diffrent to Each User)</label>

<input type="text" class="form-
control" placeholder="Enter ID" name="id">

</div>

<div class="form-group">

<label for="exampleInputText">Enter
User Name</label>

<input type="text" class="form-
control" placeholder="Enter User" name="name"

required="Please Enter
Details">
</div>

<div class="form-group">

<label
for="exampleInputNumber">Enter User Mobile Number</label>

<input type="text" class="form-
control" placeholder="Enter User Mobile

Number" name="number" required="Please Enter Details">
</div>

<div class="form-group">

<label for="exampleInputCity">Enter
User City</label>

<input type="text" class="form-
control" placeholder="Enter User City" name="city"

required="Please Enter
Details">
</div>

<div class="form-group">

<label
for="exampleInputEmail1">Email address</label>

<input type="email" class="form-
control" id="exampleInputEmail1"

ariadescribedby="emailHelp"
placeholder="Enter email" name="email" required="Please Enter
Details">
</div>

<div class="form-group">

<label
for="exampleInputPassword1">Password</label>

<input type="password" class="form-
control" id="exampleInputPassword1"

placeholder="Password"
name="password" required="Please Enter Details">
</div>

<button type="submit" class="btn btn-
primary" name="done">

Submit</button>
</form>
</div>
</div>
</section>

</center>
<center>
<hr>
<h2>For See Details Of All Users</h2>
<a href="display.php"><button type="submit" class="btn
btn-primary">Check
Users</button></a>
</center>
<br>
<hr>
</body>
</html>
"""
    print(php_code)
