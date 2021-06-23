FROM python:3
ADD carta_solution.py /
ADD nginx /
RUN pip install flask
RUN pip install ipaddress
ENTRYPOINT [ "python", "./carta_solution.py" ]
