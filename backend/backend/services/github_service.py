def push_code_to_github(code: str, filename: str = "generated_code.py"):
    with open(filename, "w") as f:
        f.write(code)
    return {"message": f"Code saved to {filename}. Push to GitHub manually for now."}
