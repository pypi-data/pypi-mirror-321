def prac1():
    php_code = """
<?php
// Practical 1: Create a PHP program to print Fibonacci series up to n terms.
function fibonacci($n) {
    $a = 0;
    $b = 1;
    for ($i = 0; $i < $n; $i++) {
        echo $a . " ";
        $next = $a + $b;
        $a = $b;
        $b = $next;
    }
}

// Example usage
$n = 10;
fibonacci($n);
?>
"""
    print(php_code)
