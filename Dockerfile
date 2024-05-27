# 
FROM python:3.12

#
WORKDIR /code

# 
COPY . /code


# 
RUN pip install  -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["fastapi", "run", "/code/main.py", "--port", "8000"]