def prac16():
    php_code = """
    16. Write a PHP program for Error Handling.
    
<?php
class customException extends Exception
{
public function errorMessage()
{
$errorMsg = 'Error on line ' . $this->getLine() . ' in
' . $this->getFile()
. ': <b>' . $this->getMessage() . '</b> is not a
valid E-Mail address';
return $errorMsg;
}
}
$email = "jigneshamala@example...com";
try {
if (filter_var($email, FILTER_VALIDATE_EMAIL) === FALSE) {
throw new customException($email);
}
} catch (customException $e) {
echo $e->errorMessage();
}
?>
"""
    print(php_code)
