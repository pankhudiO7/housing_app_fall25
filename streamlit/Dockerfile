FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy project files
COPY ./script ./script
COPY ./streamlit ./streamlit
COPY ./data ./data
# Expose ports
EXPOSE 8000 8501
# Run both FastAPI and Streamlit
CMD sh -c "uvicorn script.api:app --host 0.0.0.0 --port 8000 & streamlit run streamlit/titanic_app.py --server.port 8501 --server.address 0.0.0.0"