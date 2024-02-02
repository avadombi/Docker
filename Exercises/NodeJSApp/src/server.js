// import the module Express.js
const express = require('express');

// create an instance of the express app
// app will be used to define the route and features of the web app
const app = express();

// define a route on URL = '/'. When a user access to this
// URL, the callback function is be executed
app.get('/', (req, res) => {
    // res: object that represents the HTTP response sent
    // by the server to a client
    // req: request HTTP
    res.send("Welcome to my awesome app!");
});

// start the web server and listen to input connexions
// on port 3000. When the server successfully start. the
// callback function is executed, which print the below message
app.listen(3000, function() {
    console.log("app listening on port 3000");
});

