FROM mcr.microsoft.com/devcontainers/python:0-3.11

ENV PYTHONUNBUFFERED 1

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


# Create a non-root user and group with /app as home directory
RUN groupadd -r myappgroup && useradd -r -g myappgroup -d /app -s /sbin/nologin -c "Docker image user" myappuser

# Create the application directory
RUN mkdir /app && chown myappuser:myappgroup /app

# Set the working directory to /app
WORKDIR /app

# [Optional] Install dependencies, OS packages, etc.

# Switch to the non-root user
USER myappuser

# Your command to start the application, e.g., python, flask, django
CMD ["python", "manage.py runserver -p 8080"]