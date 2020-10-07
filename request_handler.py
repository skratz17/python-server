from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal
from locations import get_all_locations, get_single_location

HANDLERS = {
    "animals": {
        "get_all": get_all_animals,
        "get_single": get_single_animal
    },
    "locations": {
        "get_all": get_all_locations,
        "get_single": get_single_location
    }
}

# A class that inherits from another class
class HandleRequests(BaseHTTPRequestHandler):

  # A class function
  def _set_headers(self, status):
    self.send_response(status)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()

  def parse_url(self, path):
    path_params = path.split("/")
    resource = path_params[1]
    id = None

    try:
      id = int(path_params[2])
    except IndexError:
      pass
    except ValueError:
      pass

    return (resource, id) # This is called a "tuple"

  # A method on the class overriding parent method, handles GET requests
  def do_GET(self):
    print(self.path)

    self._set_headers(200)
    response = {} # default response

    (resource, id) = self.parse_url(self.path)

    resource_handlers = HANDLERS[resource]
    
    if(id is not None):
      resource_handler = resource_handlers["get_single"]
      response = f"{resource_handler(id)}"
    else:
      resource_handler = resource_handlers["get_all"]
      response = f"{resource_handler()}"

    self.wfile.write(f"{response}".encode())

  # Another overriding method that handles POST requests
  def do_POST(self):
    self._set_headers(201) # 201 - CREATED

    content_len = int(self.headers.get('content-length', 0))
    post_body = self.rfile.read(content_len)
    response = f"received post request:<br>{post_body}"
    self.wfile.write(response.encode())

  # Yet another overriding method that handles PUT requests
  def do_PUT(self):
    self.do_POST() # nailed it

def main():
  host = ''
  port = 8088
  HTTPServer((host, port), HandleRequests).serve_forever()