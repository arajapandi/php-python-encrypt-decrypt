<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

include 'MyCypher.php';

$iv = 'c09f6a9e157d253d0b2f0bcd81d338298950f246';
$cypher = new MyCypher($iv);



$secret = 'TestString From PHP';

echo "================Encrypt Test ===================";
echo "\nString = ".$secret;

$php_encrypted      = $cypher->encrypt($secret);
$python_encrypted   = exec('python ./test.py encrypt "'.$secret.'" '.$iv);

if($python_encrypted == $php_encrypted) {
    echo "\nTest - Success";
} else {
    echo "\nTest - Failed";
}
echo "\n===============================================\n";


echo "\n================Encrypt PHP, Decrypt Python Test ===================";
echo "\nString = ".$secret;

$php_encrypted      = $cypher->encrypt($secret);
$python_secret   = exec('python ./test.py decrypt "'.$php_encrypted.'" '.$iv);

if($secret == $python_secret) {
    echo "\nTest - Success";
} else {
    echo "\nTest - Failed";
}
echo "\n===============================================\n";



echo "\n================Encrypt Python, Decrypt PHP Test ===================";
echo "\nString = ".$secret;


$python_secret   = exec('python ./test.py encrypt "'.$secret.'" '.$iv);
$php_encrypted      = $cypher->decrypt($python_secret);

if($secret == $php_encrypted) {
    echo "\nTest - Success";
} else {
    echo "\nTest - Failed";
}
echo "\n===============================================\n";


