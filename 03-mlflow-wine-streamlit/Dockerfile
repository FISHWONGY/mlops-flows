FROM python:3.11-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VERSION=1.7.1 \
    USERNAME=nonroot

RUN adduser $USERNAME
USER $USERNAME

ENV HOME=/home/$USERNAME
ENV PATH="$HOME/.local/bin:$PATH"

RUN pip install pipx
RUN pipx install poetry==${POETRY_VERSION}

COPY ./poetry.lock pyproject.toml /usr/src/app/
RUN poetry install -nv --no-root

COPY app .

EXPOSE 80

CMD ["poetry", "run", "streamlit", "run", "main.py", "--server.port=80", "--server.address=0.0.0.0"]