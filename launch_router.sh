python -m debugpy --connect 5678 -m sglang_router.launch_router \
  --worker-urls http://localhost:8000 http://localhost:8001 \
  --policy cache_aware \
  --host 0.0.0.0 --port 30000
  2>&1 | tee router.log
