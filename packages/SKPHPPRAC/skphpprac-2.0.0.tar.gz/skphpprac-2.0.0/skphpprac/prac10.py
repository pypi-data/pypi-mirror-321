def prac10():
    php_code = """
10. Write a PHP program to send Mail from PHP Script.
<?php
$to_email = "yalih50344@youke1.com";
$subject = "testing";
$body = "Hi, This is test email send by PHP Script";
$headers = "From: jigneshamala@gmail.com";
if (mail($to_email, $subject, $body, $headers)) {
echo "Email successfully sent to $to_email...";
} else {
echo "Email sending failed...";
}
?>
"""
    print(php_code)
