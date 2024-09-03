FROM python:3.10-slim

# Instala o Poetry
RUN pip install pipx && \
    pipx install poetry

# Adiciona o binário do Poetry ao PATH
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

WORKDIR /app

# Copia os arquivos pyproject.toml e poetry.lock para a imagem
COPY pyproject.toml poetry.lock ./

ENV VIRTUAL_ENV=/opt/env
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instala as dependências do Poetry
RUN poetry install --no-root --no-dev

# Copia o resto do código para a imagem
COPY . .

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]
