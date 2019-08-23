FROM python
COPY main.py /
COPY quiz.py /
CMD ["python", "./main.py"]
