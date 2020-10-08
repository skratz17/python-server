from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from helpers import parse_url
from animals import get_all_animals, get_single_animal, create_animal, delete_animal, update_animal
from locations import get_all_locations, get_single_location, create_location, delete_location, update_location
from employees import get_all_employees, get_single_employee, create_employee, delete_employee, update_employee
from customers import get_all_customers, get_single_customer, delete_customer, update_customer

HANDLERS = {
    "animals": {
        "get_all": get_all_animals,
        "get_single": get_single_animal,
        "create": create_animal,
        "delete": delete_animal,
        "update": update_animal
    },
    "locations": {
        "get_all": get_all_locations,
        "get_single": get_single_location,
        "create": create_location,
        "delete": delete_location,
        "update": update_location
    },
    "employees": {
        "get_all": get_all_employees,
        "get_single": get_single_employee,
        "create": create_employee,
        "delete": delete_employee,
        "update": update_employee
    },
    "customers": {
        "get_all": get_all_customers,
        "get_single": get_single_customer,
        "delete": delete_customer,
        "update": update_customer
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

    def __get_post_body(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # JSON string -> Python dict
        post_body = json.loads(post_body)

        return post_body

  # A method on the class overriding parent method, handles GET requests
    def do_GET(self):
        print(self.path)

        self._set_headers(200)
        response = {} # default response

        (resource, id) = parse_url(self.path)

        # get dictionary of specific request handlers for this resource
        resource_handlers = HANDLERS[resource]
        
        if(id is not None):
            response = f"{resource_handlers['get_single'](id)}"
        else:
            response = f"{resource_handlers['get_all']()}"

        self.wfile.write(f"{response}".encode())

  # Another overriding method that handles POST requests
    def do_POST(self):
        self._set_headers(201)
        
        post_body = self.__get_post_body()

        (resource, id) = parse_url(self.path)

        create_resource_handler = HANDLERS[resource]['create']
        new_resource = create_resource_handler(post_body)

        self.wfile.write(f"{new_resource}".encode())

    # Yet another overriding method that handles PUT requests
    def do_PUT(self):
        self._set_headers(204) # 204 - No Content

        post_body = self.__get_post_body()

        (resource, id) = parse_url(self.path)

        update_resource_handler = HANDLERS[resource]['update']
        update_resource_handler(id, post_body)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204) # 204 - No Content

        (resource, id) = parse_url(self.path)

        delete_resource_handler = HANDLERS[resource]['delete']
        delete_resource_handler(id)

        self.wfile.write("".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()