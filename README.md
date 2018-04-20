# php-python-encrypt-decrypt
PHP Encrypt Decrypt - Python Encrypt Decrypt

Python Version - 2.7 
PHP Version - 5+

PHP  Usage - refer test.php
  // Change Key in MyCypher.php File (Same As Python)
  $cypher = new MyCypher($iv = 'anyrandomvalue');
  //Encrypt 
  $php_encrypted      = $cypher->encrypt('test');
  //Decrypt
  $php_decrypted      = $cypher->decrypt($php_encrypted);


Python Usage - refer test.py
	// Change Key in MyCypher.py File (Same As PHP)
	cipher = MyCypher(iv)
	//encrypt
	python_encrypted = cipher.encrypt('secret')
	//decrypt
    python_decrypted = cipher.decrypt(enc_str)
