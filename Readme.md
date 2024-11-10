
# Currency Converter - Python

This project is a **currency conversion web application** built with Python. It uses a web framework and a currency API to convert between different currencies in real time.

## Features

- Real-time currency conversion.
- List of available currencies based on the current exchange rates.
- Simple and functional UI using **Tkinter** (for desktop) or **Flask** (for web interface).
- Python API integration for currency exchange rates.

## Requirements

To run and develop this project, you will need to have the following programs installed on your machine:

### Development Requirements

- **Python** (version 3.8 or higher)  
  [Install Python](https://www.python.org/).

- **Package Manager**:  
  - [pip](https://pip.pypa.io/en/stable/) (installed automatically with Python)
  - You can also use a **virtual environment** for managing dependencies.

### Optional Production Requirements

- **Docker**: To run the application in a containerized environment.
  - [Install Docker](https://www.docker.com/get-started).

## Installation

Follow these steps to clone and set up the project on your local machine:

1. **Clone the repository**:

   If you have `git` installed, you can clone the repository with the following command:

   ```bash
   git clone https://github.com/your-username/currency-converter-python
   cd currency-converter-python
   ```

2. **Create and activate a virtual environment**:

   For better dependency management, it's recommended to use a virtual environment. You can create one by running the following commands:

   - For Windows:
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

   - For Mac/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install dependencies**:

   Once the virtual environment is activated, install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` file yet, create it by running:
   
   ```bash
   pip freeze > requirements.txt
   ```

4. **Run the application**:

   - For a desktop GUI using Tkinter:

     ```bash
     python currency_converter.py
     ```

   - For a web-based GUI using Flask:

     ```bash
     python app.py
     ```

5. **Access the application**:

   - For the **desktop** version, the GUI should open automatically.
   - For the **web** version, open your browser and navigate to `http://127.0.0.1:5000` to see the app in action.

## Usage

The application allows users to convert currencies between different currencies:

- **Input**: The amount of money you want to convert.
- **Select from currency**: The currency you want to convert from (e.g., USD).
- **Select to currency**: The currency you want to convert to (e.g., EUR).
- **Convert button**: Clicking "Convert" will display the converted value in the interface.

## Development

If you'd like to modify or add new features, you can start by editing the following files:

- `currency_converter.py`: Modify this file to change the logic of the currency conversion.
- `app.py`: Modify this file if you're working with the web-based version (Flask).
- `templates/index.html`: Modify this HTML file if you're working with the Flask app and need to change the UI.

### API Integration

This application uses the **Exchangerate-API** to get exchange rates:

- [Exchangerate-API Documentation](https://www.exchangerate-api.com/)

Ensure to check the API usage restrictions and limits if you plan to make significant changes or use the service in a production environment.

## Docker

### Dockerfile

To run this project in Docker, you can use the provided `Dockerfile`.

1. **Build the Docker image**:

   In the project root, run the following command to build the Docker image:

   ```bash
   docker build -t currency-converter-python .
   ```

2. **Run the Docker container**:

   After building the image, you can run the application inside a container:

   ```bash
   docker run -p 5000:5000 currency-converter-python
   ```

3. **Access the application**:

   Open your browser and navigate to `http://localhost:5000` to view the web app.

## Deployment

To deploy the project in production, you can use platforms like **Heroku**, **AWS**, or **Google Cloud**. Alternatively, you can deploy it using **Docker**.

### Deploying on Docker

1. Push the Docker image to **Docker Hub**:

   ```bash
   docker tag currency-converter-python your-username/currency-converter-python
   docker push your-username/currency-converter-python
   ```

2. On your server or cloud platform, pull the Docker image and run it.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/) - Learn about Flask and how to build web applications with it.
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) - Learn about Tkinter for building desktop GUIs in Python.
- [Exchangerate-API](https://www.exchangerate-api.com/) - API to get real-time exchange rates.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
