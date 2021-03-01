FROM daskdev/dask:2020.12.0

COPY requirements-worker.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir --ignore-installed PyYAML -r /tmp/requirements.txt