
<?php
$servername = "localhost";
$username = "root";
$password = "";

// name of database samu
$dbname = "bayishimire";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname); 

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} else {
    echo "Connected successfully";
    // You can uncomment the above line for debugging purposes
    // but it's generally not a good practice to echo connection success in production code.
}
?>