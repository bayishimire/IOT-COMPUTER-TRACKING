<?php
include 'db.php';   //include the fixed connection file db.php


if (isset($_POST["submit"]))  //registration form is submitted
{

    $first_name = $_POST['first_name'] ?? '';
    $second_name = $_POST['second_name'] ?? '';
    $age = $_POST['age'] ?? '';
    $serial_number = $_POST['serial_number'] ?? '';
    $password = password_hash($_POST['password'] ?? '', PASSWORD_BCRYPT);
    $email= $_POST['email'] ?? '';
    $photo = $_FILES['photo'] ?? '';
    $main_image_name = basename($photo['name']);
    $user_id = random_int(111111,999999);

    $directory = "uploads/";
    $image_path= $directory . $main_image_name;

    if (!file_exists($directory)) {
        mkdir($directory, 0777, true); // Create directory if it doesn't exist
    }
    if (move_uploaded_file($photo['tmp_name'], $image_path)) {
        echo "<script>alert('Main image uploaded successfully.')</script>";
    } else {
        echo "Failed to upload main image.<br>";
        exit;
    }

    // md5, sha1, sha256, bcrypt, password_default
    //   You should hash the password for security!
    // $hashed_id = password_hash($id, PASSWORD_DEFAULT);
    //   BAYISHIMIRE IS FILE NAME OF DATABASE
    
    $stmt = $conn -> prepare('INSERT INTO computer_tracking (id, fist_name, second_name, password, age, serial_number, photos,email) VALUES (?,?,?,?,?,?,?,?)');
    $stmt ->  bind_param('ssssdsss',$user_id, $first_name, $second_name, $password, $age, $serial_number, $main_image_name, $email);

    if ($stmt -> execute()) {
        echo "Registered successfully!";
    } else {
        echo "Failed to register: " . mysqli_error($conn);
    }
}
?>