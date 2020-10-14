from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from helpers import BasicHandler
from animals import AnimalHandler
from customers import CustomerHandler
from employees import EmployeeHandler
from locations import LocationHandler

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, PUT, DELETE, GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.end_headers()

    def __get_post_body(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # JSON string -> Python dict
        post_body = json.loads(post_body)

        return post_body

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # URL includes query string - parse it and return tuple of resource name, 
        # query string param, and value for that param in the query string
        if "?" in resource:
            resource, param = resource.split("?")
            key, value = param.split("=")

            value = urllib.parse.unquote(value)

            return ( resource, key, value )

        # Otherwise, it is just a request for either all items of a particular resource,
        # or a single item by ID
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

        return (resource, id) # This is called a "tuple

    def get_resource_handler(self, resource):
        if(resource == 'animals'):
            return AnimalHandler()
        elif(resource == 'customers'):
            return CustomerHandler()
        elif(resource == 'employees'):
            return EmployeeHandler()
        elif(resource == 'locations'):
            return LocationHandler()

        return BasicHandler()

  # A method on the class overriding parent method, handles GET requests
    def do_GET(self):
        self._set_headers(200)
        response = {} # default response

        url_parts = self.parse_url(self.path)

        if len(url_parts) == 2:
            resource, id = url_parts

            # get handler object for specific resource
            resource_handler = self.get_resource_handler(resource)
            
            if(id is not None):
                response = f"{resource_handler.get_by_id(id)}"
            else:
                response = f"{resource_handler.get_all()}"

        elif len(url_parts) == 3:
            resource, key, value = url_parts

            resource_handler = self.get_resource_handler(resource)

            response = resource_handler.get_by_criteria(key, value)

        self.wfile.write(f"{response}".encode())

  # Another overriding method that handles POST requests
    def do_POST(self):
        self._set_headers(201)
        
        post_body = self.__get_post_body()

        (resource, id) = self.parse_url(self.path)

        resource_handler = self.get_resource_handler(resource)
        new_resource = resource_handler.create(post_body)

        self.wfile.write(f"{new_resource}".encode())

    # Yet another overriding method that handles PUT requests
    def do_PUT(self):
        post_body = self.__get_post_body()

        (resource, id) = self.parse_url(self.path)

        resource_handler = self.get_resource_handler(resource)
        success = resource_handler.update(id, post_body)

        # responding with 404 if resource not found in the update
        if(success == False):
            self._set_headers(404)
        else:
            self._set_headers(204) # 204 - No Content

        self.wfile.write("".encode())

    def do_DELETE(self):
        (resource, id) = self.parse_url(self.path)

        resource_handler = self.get_resource_handler(resource)
        success = resource_handler.delete(id)

        if success:
            self._set_headers(204) # 204 - No Content
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_OPTIONS(self):
        self._set_headers(200)
        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()