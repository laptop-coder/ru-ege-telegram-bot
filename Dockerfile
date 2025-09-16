FROM python:3.13.7-alpine3.22 AS deps
WORKDIR /bot
COPY requirements.txt .
RUN python -m venv env \
&& source env/bin/activate \
&& pip install --no-cache-dir -r requirements.txt

FROM python:3.13.7-alpine3.22
WORKDIR /bot
COPY --from=deps /bot/env env
COPY src src
RUN adduser botuser --disabled-password --no-create-home --gecos ""
USER botuser
RUN source env/bin/activate
CMD ["env/bin/python", "src/__main__.py"]
