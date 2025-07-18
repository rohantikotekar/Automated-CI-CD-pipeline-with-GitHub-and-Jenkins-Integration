
FROM python:3.9
WORKDIR /app
COPY testcase.py /app
#RUN pip install unittest
RUN pip install requests
CMD ["python", "testcase.py"]
