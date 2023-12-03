<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"]);
    $email = htmlspecialchars($_POST["email"]);
    $message = htmlspecialchars($_POST["message"]);

    // In a real-world scenario, you might want to save the form data to a database.
    // For simplicity, we'll just log it to the console here.
    $logMessage = "Form submitted:\nName: $name\nEmail: $email\nMessage: $message";
    error_log($logMessage);

    // Send a response (you can customize this as needed)
    echo 'Form submitted successfully!';
} else {
    // Invalid request
    http_response_code(400);
    echo 'Invalid request.';
}
?>