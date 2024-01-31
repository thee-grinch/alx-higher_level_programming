#!/usr/bin/node

const fs = require('fs');

// Check if the file path argument is provided
if (process.argv.length < 3) {
    console.error('Usage: node read_file.js <file_path>');
    process.exit(1);
}

const filePath = process.argv[2];

// Read the content of the file
fs.readFile(filePath, 'utf8', function(err, data) {
    if (err) {
        console.error(err); // Print the error object if an error occurred
        return;
    }
    console.log(data); // Print the content of the file
});
