def prac12():
    php_code = """
    
12. Write a PHP Program to Recursive Traversals of Directory.
    
    
<?php
error_reporting(E_ALL | E_STRICT);
ini_set('display_errors', 1);
header('Content-Type:text/plain');
$dir = dirname(__FILE__);
foreach (new RecursiveIteratorIterator(new
RecursiveDirectoryIterator($dir)) as $item) {
if ($item->isFile() || $item->isDir()) {
echo $item . PHP_EOL;
}
}
?>
"""
    print(php_code)
