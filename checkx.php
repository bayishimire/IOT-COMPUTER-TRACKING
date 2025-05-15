<?php
include("db.php");

if (isset($_POST["submit"])) {
    $serial_number = $_POST['serial_number'];
    $stmt = $conn->prepare("SELECT * FROM computer_tracking WHERE email = ?");
    $stmt->bind_param("s", $serial);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        echo "<h2>Serial Number Found:</h2>";
        echo "<p><strong>Username:</strong> " . htmlspecialchars($row['username']) . "</p>";
        echo "<p><strong>County:</strong> " . htmlspecialchars($row['county']) . "</p>";
        echo "<p><strong>Machine Type:</strong> " . htmlspecialchars($row['machine_type']) . "</p>";
        echo '<img src="data:image/jpeg;base64,' . base64_encode($row['photo']) . '" width="200"/>';
    } else {
        echo "<h1>Not Registered 🖥️dr.samu🖥️
        .&nbsp;&nbsp;&nbsp; &nbsp;<p><u><b>WELLCAME REGISTERATION<br></P></h1>";
        
        echo '<p><a href="samu.php">Click here to register</a></p>';
        
    }

    $stmt->close();
    $conn->close();
} else {
    echo 'Form not submitted.';
}
?>