import os
from datetime import date

def add_problem(problem_name: str, file_path: str):
    ts = os.path.getmtime(file_path)
    solved_date = date.fromtimestamp(ts).isoformat()
    line = f"| {problem_name} | {solved_date} |\n"

    with open("progress.md", "a", encoding="utf-8") as f:
        f.write(line)

def main():
    for f in os.listdir("src"):
        path = os.path.join("src", f)
        if os.path.isfile(path):
            name, _ = os.path.splitext(f)
            add_problem(name, path)

if __name__ == "__main__":
    main()
