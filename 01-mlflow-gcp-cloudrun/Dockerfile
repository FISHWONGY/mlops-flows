FROM python:3.11-slim

ENV PYTHONUNBUFFERED=True \
    POETRY_VERSION=1.7.1 \
    USERNAME=nonroot

WORKDIR /usr/src/app

RUN adduser $USERNAME
USER $USERNAME

ENV HOME=/home/$USERNAME
ENV PATH="$HOME/.local/bin:$PATH"

RUN pip install pipx
RUN pipx install poetry==${POETRY_VERSION}

COPY ./poetry.lock ./pyproject.toml /usr/src/app/

RUN poetry install -nv --no-root

COPY app .

COPY entry-point.sh ./entry-point.sh

ENTRYPOINT ["/usr/bin/env", "bash", "./entry-point.sh"]

EXPOSE 8080
