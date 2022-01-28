### --- environment
FROM python:3
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
# I tried "flask run", but that didn't seem to work
# Wonder why.  Probably the way flask is installed?
CMD ["python", "src/app.py"]
