# CCIP Read DNS Gateway Python

This project provides a DNS gateway for reading and resolving DNS queries using Flask and aiohttp. It includes tools for handling DNS queries, interacting with blockchain contracts, and performing unit and end-to-end tests.

Work in progress - Need to Implement EVM functionality
## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Ensure you have the following installed:

- Python 3.10 or later
- `pip` for managing Python packages

## Installation

1. Clone the repository:

    ```sh
    git clone <repository_url>
    cd ccip-read-dns-gateway-python
    ```

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Environment Setup

Create a `.env` file in the project directory with the following content:

```env
DOH_GATEWAY_URL=http://localhost:8081/resolve
```

## Running the Application

### Flask Application

The Flask application handles basic DNS query requests.

1. Run the Flask application:

    ```sh
    python app.py
    ```

   The server will start on `http://0.0.0.0:8082`.

### aiohttp Server

The aiohttp server handles DNS queries and processes them.

1. Run the aiohttp server:

    ```sh
    python server_instance.py
    ```

   The server will start on `http://0.0.0.0:8081`.

## Running Tests

### End-to-End Tests

End-to-end tests simulate the full workflow of DNS query resolution and interaction with blockchain contracts.

To run the end-to-end tests:

```sh
python test_end_to_end.py
```

## Project Structure

```sh
ccip-read-dns-gateway-python/
├── app.py
├── build/
│   └── bdist.linux-x86_64/
├── ccip_read_dns_gateway_python.egg-info/
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── dist/
│   ├── ccip_read_dns_gateway_python-0.1.0-py3.10.egg
│   ├── ccip_read_dns_gateway_python-0.1.0-py3-none-any.whl
│   └── ccip-read-dns-gateway-python-0.1.0.tar.gz
├── e2e_test.py
├── index.py
├── __pycache__/
│   └── app.cpython-310.pyc
├── README.md
├── requirements.txt
├── server_instance.py
├── server_test.py
├── setup.py
├── test/
└── worker.py
```

- `app.py`: Main Flask application file.
- `server_instance.py`: aiohttp server for handling DNS queries.
- `requirements.txt`: List of dependencies.
- `setup.py`: Setup script for packaging the application.
- `test_server_response.py`: Unit tests for server responses.
- `test_end_to_end.py`: End-to-end tests.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
