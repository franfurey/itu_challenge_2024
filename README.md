# itu_challenge_2024
GeoAI Ground-level NO2 Estimation Challenge by ITU

## Development environment configuration

### Create and configure a virtual environment (venv)

1. Create the virtual environment:
    ```sh
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    - In macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    - In Windows:
        ```sh
        .\venv\Scripts\activate
        ```

### Create a Jupyter Notebook kernel linked to venv

3. Install Jupyter in the virtual environment:
    ```sh
    pip install jupyter
    ```

4. Create a Jupyter Notebook kernel linked to the venv:
    ```sh
    python -m ipykernel install --user --name=itu_challenge --display-name "ITU Challenge 2024"
    ```
