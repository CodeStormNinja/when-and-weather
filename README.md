# When & Weather 🌦️

A web system designed to facilitate the access to weather forecasting regardless of the location or specific period needed. Made for our project the [2025 NASA Space Apps Hackathon Challenge](https://www.spaceappschallenge.org/).

The project is divided in 3 parts:

- The **front-end layer**, with an app developed with React to display the UI for users.
- The **back-end domain layer**, with an API that deals with the business logic and decision-making to give a cleaner and more purposeful description for the users, developed with Java.
- The **data layer**, with an API that translates the location query into specific coordinates (globally) and checks the weather for that location and date/time inputs, developed with Python.
   
---

## Features

### Web application

The front-end is a small React application (Vite + TypeScript) that provides a clean UI to query a location and a date/time and show the weather forecast and a simplified interpretation (thermal comfort, rain chance, wind). Key user-facing features:

- Easy location search and forecast visualization for a chosen date/time
- Simple, mobile-friendly weather card with icons (sunny, rainy, cloudy)
- Loading states and friendly error messages when external services fail
- Integration with the domain API to receive a concise, human-friendly forecast

### Domain API

- **RESTful Endpoint**: Available at `/api/clima/analise` for GET requests.
- **Enhanced Classification Logic**: The climate service determines the thermal comfort based on temperature and appends a rain forecast based on humidity.

### Data API

- **Weather Forecast API**: Provides weather forecast data via `/api/v1/weather-forecast`.
- **Modular Structure**: Organized using Domain-Driven Design (DDD) principles.
- **External Integrations**: Connects to external APIs (e.g., Open-Meteo) using reusable HTTP context classes.
- **Swagger Documentation**: API models and documentation available for easy integration and testing, accessible through the root endpoint `/`.

---

## Requirements

### Web Application

- **Node.js 18+** (recommended) and **npm** (or **yarn / pnpm**) to install dependencies and run scripts

### Domain API

- **Java JDK 21+**
- **Apache Maven (Wrapper included)**

### Data API

- **Python 3.12**

---

## How to Run

### Web Application

1. **Open a terminal (Windows: cmd.exe) and change to the front-end folder**:
   ```cmd
   cd front-end-parade
   ```

2. **Install dependencies (using npm)**:
   ```cmd
   npm install
   ```

3. **Start the development server**:
   ```cmd
   npm run dev
   ```

After the dev server starts, open http://localhost:5173 in your browser (Vite default). The front-end expects the domain API to be available at http://localhost:8080 by default.

Notes:

- If your back-end runs on a different host/port, update the base URL in `front-end-parade/src/constants/apiUrl.ts` (the default value is `http://localhost:8080/api/`).
- To build for production use:
  ```cmd
  npm run build
  npm run preview
  ```

### Domain API

Prerequisites: Ensure Java 21 or higher is installed and configured.
Start the Application: Use the Maven Wrapper (mvnw) to run the Spring Boot application:

1. **Open a terminal (Windows: cmd.exe) and change to the front-end folder**:
   ```cmd
   cd back-end-parade
   ```
   
2. **Start the application using mvnw.cmd**:
   ```cmd
   .\mvnw.cmd spring-boot:run
   ```

Access: The API will be running at http://localhost:8080.

### Data API

1. **Open a terminal (Windows: cmd.exe) and change to the front-end folder**:
   ```cmd
   cd data-parade
   ```

2. **Set up a Python 3.12 environment**  
   (e.g., using `venv` or `conda`)

   ```cmd
   python3.12 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies from `pyproject.toml`**  
   (using [pip](https://pip.pypa.io/en/stable/) or [pip-tools](https://pip-tools.readthedocs.io/en/latest/) if you use a lock file)

   ```cmd
   pip install -e .
   # or, if using poetry:
   poetry install
   ```

4. **Run the application**
   ```cmd
   python -m main.app
   ```

---

## License:

This project was built under the MIT license.

---

## Data Sources & Attribution

This project uses weather forecast data from [**Open-Meteo**](https://open-meteo.com/).

- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

This project uses geodata from [**OpenStreetMap**](https://www.openstreetmap.org).

- **License:** OpenStreetMap data is licensed under the [**Open Database License (ODbL) 1.0**](https://opendatacommons.org/licenses/odbl/1-0/).
