# http-server

An http server that makes requests on a port as follows:
1. POST http://host:port/
In this case, it takes the data as JSON in following format:
{
  "main": {"x": number, "y": number, "width": number, "height": number},
  "input": [
  {"x": number, "y": number, "width": number, "height": number},
  {"x": number, "y": number, "width": number, "height": number},
  ...
  ]
}
this program saves just those part of input that are in common with main(inner join of main and input)

3. GET http://host:port/
A list of all saved data along with the saving time of each should be in JSON format
The following format should be returned:
[
  {"x": number, "y": number, "width": number, "height": number, "time":
"YYYY-MM-DD HH:mm:ss"},
  {"x": number, "y": number, "width": number, "height": number, "time":
"YYYY-MM-DD HH:mm:ss"},
  ...
]
