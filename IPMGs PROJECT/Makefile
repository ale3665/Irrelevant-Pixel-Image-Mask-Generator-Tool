# Define variables for reuse
VENV_DIR = venv
PYTHON = $(VENV_DIR)/Scripts/python
PIP = $(VENV_DIR)/Scripts/pip

# Default target when running `make`
all: install run

# Target to create a virtual environment if it doesn't exist
$(VENV_DIR)/bin/activate:
	python -m venv $(VENV_DIR)

# Install dependencies
install: $(VENV_DIR)/bin/activate
	$(PIP) install -r requirements.txt

# Run the Streamlit app
run:
	$(PYTHON) -m streamlit run app.py

# Clean up the virtual environment and any pycache files
clean:
	rm -rf $(VENV_DIR)
	find . -name "__pycache__" -exec rm -rf {} +

# Target for installing numpy separately, if needed
install-numpy: $(VENV_DIR)/bin/activate
	$(PIP) install numpy
