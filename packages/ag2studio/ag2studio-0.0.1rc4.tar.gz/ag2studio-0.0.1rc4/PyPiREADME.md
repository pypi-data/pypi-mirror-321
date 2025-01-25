# AG2 Studio

[![PyPI version](https://badge.fury.io/py/ag2studio.svg)](https://badge.fury.io/py/ag2studio)
[![Downloads](https://static.pepy.tech/badge/ag2studio/week)](https://pepy.tech/project/ag2studio)

AG2 Studio is an AG2-powered (formerly AutoGen) AI app (user interface) to help you rapidly prototype AI agents, enhance them with skills, compose them into workflows and interact with them to accomplish tasks. It is built on top of the [AG2](https://ag2ai.github.io/ag2) framework, which is a toolkit for building AI agents.

> **Note**: AG2 Studio is meant to help you rapidly prototype multi-agent workflows and demonstrate an example of end user interfaces built with AG2. It is not meant to be a production-ready app.

Project Structure:

- _ag2studio/_ code for the backend classes and web api (FastAPI)
- _frontend/_ code for the webui, built with Node.js and TailwindCSS

### Installation

There are two ways to install AG2 Studio - from PyPi or from source. We **recommend installing from PyPi** unless you plan to modify the source code.

1.  **Install from PyPi**

    We recommend using a virtual environment (e.g., conda) to avoid conflicts with existing Python packages. With Python 3.12 or newer active in your virtual environment, use pip to install AG2 Studio:

    ```bash
    pip install ag2studio
    ```

2.  **Install from Source**

    > Note: This approach requires some familiarity with building interfaces in React.

    If you prefer to install from source, ensure you have Python 3.10+ and Node.js (version above 20) installed. Here's how you get started:

    - Clone the AG2 Studio repository and install its Python dependencies:

      ```bash
      pip install -e .
      ```

    - Navigate to the `frontend` directory, install dependencies, and build the UI.

      For MacOS/Linux/Windows:

      ```bash
      yarn install
      ```

      Then, for MacOS/Linux:

      ```bash
      yarn build
      ```

      Or, for Windows:

      ```
      yarn build-windows
      ```

### Running the Application

Once installed, run the web UI by entering the following in your terminal:

```bash
ag2studio ui --port 8081
```

This will start the application on the specified port. Open your web browser and go to `http://localhost:8081/` to begin using AG2 Studio.

AG2 Studio also takes several parameters to customize the application:

- `--host <host>` argument to specify the host address. By default, it is set to `localhost`. Y
- `--appdir <appdir>` argument to specify the directory where the app files (e.g., database and generated user files) are stored. By default, it is set to the a `.ag2studio` directory in the user's home directory.
- `--port <port>` argument to specify the port number. By default, it is set to `8080`.
- `--reload` argument to enable auto-reloading of the server when changes are made to the code. By default, it is set to `False`.
- `--database-uri` argument to specify the database URI. Example values include `sqlite:///database.sqlite` for SQLite and `postgresql+psycopg://user:password@localhost/dbname` for PostgreSQL. If this is not specified, the database URIL defaults to a `database.sqlite` file in the `--appdir` directory.

Now that you have AG2 Studio installed and running, you are ready to explore its capabilities, including defining and modifying agent workflows, interacting with agents and sessions, and expanding agent skills.

## Contribution Guide

We welcome contributions to AG2 Studio. We recommend the following general steps to contribute to the project:

- Review the overall AG2 project [contribution guide](https://github.com/ag2ai/ag2?tab=readme-ov-file#contributing)
- Please initiate a discussion on the roadmap issue or a new issue to discuss your proposed contribution.
- Submit a pull request with your contribution!
- If you are modifying AG2 Studio, it has its own devcontainer. See instructions in `.devcontainer/README.md` to use it
- Please use the tag `studio` for any issues, questions, and PRs related to Studio

## FAQ

Please refer to the AG2 Studio [FAQs](https://ag2ai.github.io/ag2/docs/autogen-studio/faqs) page for more information.

## Acknowledgements

AG2 Studio is Based on the [AG2 (Formerly AutoGen)](https://ag2ai.github.io/ag2) project. It was adapted from a research prototype built in October 2023 (original credits: Gagan Bansal, Adam Fourney, Victor Dibia, Piali Choudhury, Saleema Amershi, Ahmed Awadallah, Chi Wang).
