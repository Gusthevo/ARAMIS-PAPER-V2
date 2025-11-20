# token_counter.py
import tiktoken
from pathlib import Path

def count_gpt_tokens(md_file_path: str) -> int:
    enc = tiktoken.encoding_for_model("gpt-4o")
    text = Path(md_file_path).read_text(encoding="utf-8")
    return len(enc.encode(text))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python token_counter.py <arquivo.md>")
        exit(1)

    file = sys.argv[1]
    total = count_gpt_tokens(file)
    print(f"Tokens GPT-4o: {total}")


