# Payroll Protection Program Portal Python SDK

Use this python library to manage PPP Loan resources through the Payroll Protection Program Portal Python SDK.

## Requirements
The SDK supports the following versions of Python:
* Python 2 versions 2.7 and later
* Python 3 versions 3.4 and later

The SDK requires the following libraries:
* requests
* python-dateutil

## Installation
You can download or clone the sdk (PPPForgivenessSDK)  and then install the SDK by running Setuptools in the SDK installation directory:
```sh
python setup.py install --user
```

## API documentation
* [API Dictionary](https://ussbappp.github.io/API-Dictionary.html)

## Sample Use Cases
* [Use Cases](https://ussbappp.github.io/index.html)

## API examples
* [create_forgiveness_request.py](examples/create_forgiveness_request.py)
* [create_forgiveness_request_3508s.py](examples/create_forgiveness_request_3508s.py)
* [delete_forgiveness_request.py](examples/delete_forgiveness_request.py)
* [list_forgiveness_requests.py](examples/list_forgiveness_requests.py)
* [read_forgiveness_requests_by_slug.py](examples/read_forgiveness_requests_by_slug.py)
* [read_forgiveness_requests_by_sbanumber.py](examples/read_forgiveness_requests_by_sbanumber.py)
* [list_document_types.py](examples/list_document_types.py)
* [read_document_type.py](examples/read_document_type.py)
* [create_loan_document.py](examples/create_loan_document.py)


## Usage

Request an API token and vendor key

Now make your first API call....
   * copy the file `/examples` `examples/list_document_type.py` to a working directory.
   * change directoy to the working directory
        edit the file list_document_type.py, changing the lines
            ```python
            client = Client(
            access_token='{{YOUR_TOKEN_HERE}}',
            vendor_key='{{YOUR_VENDOR_KEY}},
            environment='sandbox'
                )
            ```
        by replacing '{{YOUR_TOKEN_HERE}}' with your assigned token
   * In a command/console window, run the *modified* file with
        ```sh
        python list_document_type.py'
        ```

CONGRATULATIONS - if your host is properly configured and your token valid, you console should display results of your first API call

For additional examples and documentation, refer the `API documentation` and `API examples` sections above.
Examples require addition of valid key and parameters before they will function
