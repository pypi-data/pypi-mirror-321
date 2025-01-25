def prac18():
    php_code = """
18. Write a PHP program for connection with my Sql and display all record from the database
19. Write a PHP program for add record into database
20. Write a PHP program for search record from the database
21. Write a PHP program for delete, update record from the database
22. Develop a PHP application to make following Operation
I. Registration of user.
ii. Insert the details of user.
iii. Modify the details
Note: Practical 18,19,20,21,22 all are in below practical
//Print all For Easy Understaning

 // conn.php
<?php
$con = mysqli_connect('localhost','root');
mysqli_select_db($con, 'practical');
?>


 // registration.php
<?php
include 'conn.php';
if (isset($_POST['done'])) {
$id = $_POST['id'];
$name = $_POST['name'];
$number = $_POST['number'];
$city = $_POST['city'];
$email = $_POST['email'];
$password = $_POST['password'];
$q = "INSERT INTO `practical`(`id`, `name`, `number`,
`city`, `email`, `password`)
VALUES ('$id','$name','$number','$city','$email','$password')";
$query = mysqli_query($con, $q);
}
?>
<!DOCTYPE html>
<html>

<head>
<title>Registration Of User</title>

</head>
<style>
body {
background-color: whitesmoke;
}
input {
width: 40%;
height: 5%;
border: 1px;
border-radius: 05px;
padding: 8px 15px 8px 15px;
margin: 10px 0px 15px 0px;
box-shadow: 1px 1px 2px 1px grey;
}
</style>
<body>
<center>
<h1>Registration Of User</h1>
<section class="my-2">
<div class="py-3">
<div class="container">
<form method="post">
<div class="form-group">
<label
for="exampleInputText">ID(Assign Diffrent to Each User)</label>

<input type="text" class="form-
control" placeholder="Enter ID" name="id"

required="Please Enter
Details">
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
