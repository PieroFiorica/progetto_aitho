# Base image with Python
FROM python:3.12-alpine

# Set working directory
WORKDIR /src

# Copy source code
COPY src/ /src/
COPY ./requirements.txt ./requirements.txt

# Install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Streamlit needs this to run properly in Docker
ENV PYTHONUNBUFFERED=1 \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py","--server.port","8501"]
