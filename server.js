const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, 'public')));

// Parse form data
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Handle form submissions
app.post('/submit-form', (req, res) => {
    const { name, email, message } = req.body;

    // In a real-world scenario, you might want to save the form data to a database.
    // For simplicity, we'll just log it to the console here.
    console.log(`Form submitted:\nName: ${name}\nEmail: ${email}\nMessage: ${message}`);

    // Send a response (you can customize this as needed)
    res.send('Form submitted successfully!');
});

// Serve the HTML file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
