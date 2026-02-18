PORT="${1:-${PORT:-8000}}"
LOG_FILE="server_${PORT}.log"
python -m sglang.launch_server --model Qwen/Qwen3-0.6B --mem-fraction-static 0.1 --port ${PORT} 2>&1 | tee ${LOG_FILE}
