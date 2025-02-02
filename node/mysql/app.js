let express = require('express');
let mysql = require('mysql');

const env = require('dotenv').config({ path: './../../.env' });

let connection = mysql.createConnection({
   host: process.env.host,
   user: process.env.user,
   password: process.env.password,
   database: process.env.database,
});

let app = express();

connection.connect(function (err) {
   if (!err) {
      console.log('DB is Connected\n');
   } else {
      console.log(err);
      console.log('Error Occured : Cannot connect to DB\n');
   }
});

app.get('/', function (req, res) {
   connection.query('select * from st_info', function (err, rows, fields) {
      connection.end();
      if (!err) {
         res.send([rows]);
         console.log('Result : ', rows);
      } else {
         console.log('Error Occured : Cannot get Responses.\n');
      }
   });
});

app.listen(8000, function () {
   console.log('8000 Port : Server Listening......\n');
});
