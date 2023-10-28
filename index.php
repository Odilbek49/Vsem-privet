<?php
echo "hello world!\n";

$name = 'Odilbek';

echo "hello, $name";

const NAME = 'asd';
// global scope
$x = 5;
function myTest()
{
    global $x;

    // using x inside this function will generate an error
    echo "<p>Variable x inside function is: $x</p>";
}
myTest();

echo "<p>Variable x outside function is: $x</p>";


function a()
{
    static $a = 0;
    echo $a;
    $a++;
}

a();
a();
a();

$count = 0;


function increment(&$c) {
    $c++;
}

increment($count);
increment($count);
print("\n". $count);

print("\nasd");

print(34);
echo "\n";
print(34.43 . "\n");

print(34.43);
var_dump(34);
var_dump(["sdf", 34.4]);
var_dump(array(434,34,34,));
class Car {

}
var_dump(new Car);
var_dump(null);
