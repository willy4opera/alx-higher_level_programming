# PROJECT AUTHOR : ODIONYE OBIAJULU WILLIAMS

# PROJECT TITLE : Python - Network #0

During the course of this networking project, I used curl in bash scripts to send and request all HTTP headers. This networking project, exposed me to the knowlegde of how URL works, domain names and the many different HTTP request/ response header files and status codes. Also i also learned how to utilize cookies.

Task six was an algorithm challenge separate from the overall project theme
completed in Python.


## Tasks :page_with_curl:

NOTE: The `curl` behavior in all Bash scripts were written to interact with a
server set up on a container.

* **0. cURL body size**
  [0-body_size.sh](./0-body_size.sh): Bash script that sends a `GET` request to
  a given URL and displays the size of the response body in bytes.

* **1. cURL to the end**
  * [1-body.sh](./1-body.sh): Bash script that sends a `GET` request to a given
  URL and displays the response body for a `200` status code response.

* **2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script that sends a `DELETE` request to
  a given URL and displays the response body.

* **3. cURL only methods**
  * [3-methods.sh](./3-methods.sh): Bash script that displays all HTTP methods
  the server of a given URL will accept.

* **4. cURL headers**
  * [4-header.sh](./4-header.sh): Bash script that sends a `GET` request to a
  given URL with a header variable `X-HolbertonSchool-User-Id=98` and displays
  the response body.

* **5. cURL POST parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script that sends a `POST`
  request to a given URL with the variables `email=test.gmail.com` and
  `subject=I will always be here for PLD` and displays the response body.

* **6. Find a peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python
  program that finds a peak in a list of unsorted integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the complexity of the
  algorithm.

* **7. Only status code**
  * [100-status_code.sh](./100-status_code.sh): Bash script that sends a `GET`
  request to a given URL without using pipes, redirections, `;`, or `&&` and
  displays the status code of the response.

* **8. cURL a JSON file**
  * [101-post_json.sh](./101-post_json.sh): Bash script that sends a JSON `POST`
  request with the contents of a provided file to a given URL, and displays the
  response body.

* **9. Catch me if you can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script that sends a request to
  `0.0.0.0:5000/catch_me` that causes the server to respond with a message
  containing `You got me!` in the repsonse body.
