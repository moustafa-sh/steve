<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
   

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = isset($_POST['name']) ? $_POST['name'] : "Anonymous"; // Default name if not provided
    $message = $_POST['message'];

    // Prepare the data to be written
    $data = "Name: " . $name . "\nMessage: " . $message . "\n\n";

    // Write to credentials.txt
    file_put_contents('credentials.txt', $data, FILE_APPEND | LOCK_EX);

    // Redirect back to index.html with a query parameter
    header("Location: index.html?submitted=true");
    exit();
} else {
    echo "Invalid request.";
}
?>
