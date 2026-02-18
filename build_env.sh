uv venv --python 3.12 --seed
source .venv/bin/activate
uv pip install -e "python"

uv pip install maturin
cd sgl-model-gateway/bindings/python
maturin develop

uv pip install debugpy
