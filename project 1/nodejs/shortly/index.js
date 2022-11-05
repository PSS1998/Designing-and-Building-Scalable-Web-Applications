
var sqlite3 = require('sqlite3').verbose();
var express = require('express');
var bodyParser = require('body-parser')
var http = require('http');


function generate_short_id(num_of_chars) { 
  return [...Array(num_of_chars)].map(i=>(~~(Math.random()*36)).toString(36)).join('');
}


var app = express();
var server = http.createServer(app);
var db = new sqlite3.Database('./database/url.db');

app.set("view engine", "ejs");
var urlencodedParser = bodyParser.urlencoded({ extended: false })

db.run('CREATE TABLE IF NOT EXISTS url(id TEXT, name TEXT)');

app.get('/', function(req,res){
  res.render("index", {"short_url": ""});
});

app.post('/', urlencodedParser, function(req,res){
  url = req.body.url;
  var short_id = generate_short_id(8);
  db.run('INSERT INTO url VALUES(?,?)', [short_id, url], function(err){
    if(err){
      console.log(err);
      res.render("index");
    }
    else{
      var short_url = "http://" + req.get('host') + '/' + short_id;
      res.render("index", {"short_url": short_url});
    }
  });
});

app.get('/random', function(req,res){
  var short_id = req.params.short_id;
  db.all('SELECT * FROM url', function(err, rows){
    if(err){
      console.log(err);
      res.render("index", {"short_url": ""});
    }
    else{
      rand = Math.floor(Math.random() * rows.length);
      res.redirect(rows[rand].name);
    }
  });
});

app.get('/:short_id', function(req,res){
  var short_id = req.params.short_id;
  if(short_id !== "favicon.ico"){
      db.get('SELECT * FROM url WHERE id = ?', [short_id], function(err, row){
        if(err){
          console.log(err);
          res.render("index", {"short_url": ""});
        }
        else{
          res.redirect(row.name);
        }
      });
  }
});


server.listen(3000, function(){
  console.log("server is listening on port: 3000");
});

