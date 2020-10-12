from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import urllib

from helpers import BasicHandler
from animals import AnimalHandler
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from customers import get_all_customers, get_single_customer, get_customer_by_criteria, delete_customer, update_customer

class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
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
                response = f"{resource_handler.get_single(id)}"
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
        self._set_headers(204) # 204 - No Content

        post_body = self.__get_post_body()

        (resource, id) = self.parse_url(self.path)

        resource_handler = self.get_resource_handler(resource)
        resource_handler.update(id, post_body)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204) # 204 - No Content

        (resource, id) = self.parse_url(self.path)

        resource_handler = self.get_resource_handler(resource)
        resource_handler.delete(id)

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()