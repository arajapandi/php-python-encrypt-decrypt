# php-python-encrypt-decrypt
PHP Encrypt Decrypt - Python Encrypt Decrypt<br><br>

Python Version - 2.7 <br>
PHP Version - 5+<br><br>

PHP  Usage - refer test.php<br>
  // Change Key in MyCypher.php File (Same As Python) <br>
  $cypher = new MyCypher($iv = "anyrandomvalue") ; <br>
  //Encrypt  <br>
  $php_encrypted      = $cypher->encrypt("test") ; <br>
  //Decrypt <br>
  $php_decrypted      = $cypher->decrypt($php_encrypted)  ; 
  
  <br><br><br>

<p>
Python Usage - refer test.py
	// Change Key in MyCypher.py File (Same As PHP) <br/>
	cipher = MyCypher(iv) <br/>
	//encrypt <br>
	python_encrypted = cipher.encrypt("secret")  - <br/>
	//decrypt<br>
    python_decrypted = cipher.decrypt(enc_str)<br>
	</p>
