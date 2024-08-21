<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $name = htmlspecialchars($_POST['name']);
    $rangeValue = htmlspecialchars($_POST['range']);

    // Prepare the data to be saved
    $data = "Name: $name, Range: $rangeValue\n";

    // Save the data to like.txt
    file_put_contents('like.txt', $data, FILE_APPEND | LOCK_EX);

    // Redirect back to the form or show a success message
    echo "Data saved successfully!";
} else {
    // If not a POST request, redirect to the form
    header("Location: index.html");
    exit();
}
?>
