FROM python
COPY main.py /
COPY quiz.json /
CMD ["python", "./main.py"]
