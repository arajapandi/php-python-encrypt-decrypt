<?php

/**
 * Valid encryption methods AES-256-CFB 
 * 
 * $cypher = new MyCypher($iv);
 * $php_encrypted      = $cypher->encrypt('test');
 * $php_decrypted      = $cypher->decrypt($php_encrypted);
 */
class MyCypher {

    private $key = 'asdfa923aksadsYahoasdw998sdsads';
    private $iv = null;
    private $method = "AES-256-CFB";
    private $blocksize = 32;
    private $padwith = '`';

    /*
     * construct for cypher class - get, set key and iv
     */

    function __construct($iv, $key = null) {

        if (is_string($key)) {
            $this->key = $key;
        }

        $this->iv = $iv;
    }

    /*
     * get hased key - if key is not set on init, then default key wil be used
     */

    private function getKEY() {

        if (empty($this->key)) {
            die('Key not set!');
        }

        return substr(hash('sha256', $this->key), 0, 32);
    }

    /*
     * get hashed IV value - if no IV values then it throw error
     */

    private function getIV() {

        if (empty($this->iv)) {
            die('IV not set!');
        }

        return substr(hash('sha256', $this->iv), 0, 16);
    }

    /*
     * Encrypt given string using AES encryption standard
     */

    public function encrypt($secret) {

        try {

            $padded_secret = $secret . str_repeat($this->padwith, ($this->blocksize - strlen($secret) % $this->blocksize));
            $encrypted_string = openssl_encrypt($padded_secret, $this->method, $this->getKEY(), OPENSSL_RAW_DATA, $this->getIV());
            $encrypted_secret = base64_encode($encrypted_string);
            return $encrypted_secret;
        } catch (Exception $e) {
            die('Error : ' . $e->getMessage());
        }
    }

    /*
     * Decrypt given string using AES standard
     */

    public function decrypt($secret) {
        try {
            $decoded_secret = base64_decode($secret);
            $decrypted_secret = openssl_decrypt($decoded_secret, $this->method, $this->getKEY(), OPENSSL_RAW_DATA, $this->getIV());
            return rtrim($decrypted_secret, $this->padwith);
        } catch (Exception $e) {
            die('Error : ' . $e->getMessage());
        }
    }

}
