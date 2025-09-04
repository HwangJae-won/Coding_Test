import sys
from datetime import date

def update_readme(problem_num, problem_title, category):
    url = f"https://www.acmicpc.net/problem/{problem_num}"
    today = date.today().isoformat()

    line = f"- [{problem_num} {problem_title}]({url}) | 📅 {today} | ✅ First Attempt\n"

    readme_path = "README.md"

    with open(readme_path, "a", encoding="utf-8") as f:
        f.write(f"\n### {category}\n{line}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python utils/update_readme.py {문제번호} {문제제목} {카테고리}")
        sys.exit(1)

    problem_num = sys.argv[1]
    problem_title = sys.argv[2]
    category = sys.argv[3]

    update_readme(problem_num, problem_title, category)