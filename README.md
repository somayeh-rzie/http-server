# http-server

An http server that makes requests on a port as follows:
1. POST http://host:port/  <br />
In this case, it takes the data as JSON in following format: <br />
{ <br />
  "main": {"x": number, "y": number, "width": number, "height": number}, <br />
  "input": [ <br />
  {"x": number, "y": number, "width": number, "height": number}, <br />
  {"x": number, "y": number, "width": number, "height": number}, <br />
  ... <br />
  ] <br />
} <br />
This program saves just those part of input that are in common with main(inner join of main and input) <br /> <br /> <br />

2. GET http://host:port/ <br />
A list of all saved data along with the saving time of each should be in JSON format <br />
The following format should be returned: <br />
[ <br />
  {"x": number, "y": number, "width": number, "height": number, "time":
"YYYY-MM-DD HH:mm:ss"}, <br />
  {"x": number, "y": number, "width": number, "height": number, "time":
"YYYY-MM-DD HH:mm:ss"}, <br />
  ... <br />
] <br /><br />

An example for post command using curl via terminal is :<br />
curl -X POST -H "Content-Type: application/json" -d '{"main": {"x": 0, "y": 0, "width": 10, "height": 20}, "input": [{"x": 2, "y": 18, "width": 5, "height": 4}, {"x": 12, "y": 18, "width": 5, "height": 4}, {"x": -1, "y": -1, "width": 5, "height": 4, "lighten":5, "helllllooooooo":0}]}' http://localhost:5000/<br /><br />
An example for get command using curl via termianl is <br />
curl http://localhost:5000/<br /><br />

