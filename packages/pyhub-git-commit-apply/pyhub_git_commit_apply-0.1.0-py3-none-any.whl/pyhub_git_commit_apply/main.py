#!/usr/bin/env python3

import sys
import os
import re
import urllib.request
import json


def main():
    if len(sys.argv) < 2:
        print("Usage: git-commit-apply <commit_url>", file=sys.stderr)
        sys.exit(1)

    commit_url = sys.argv[1]

    pattern = r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/commit/(?P<sha>[0-9a-f]+)"
    match = re.search(pattern, commit_url)
    if not match:
        print("Invalid GitHub commit URL.", file=sys.stderr)
        sys.exit(1)

    owner = match.group("owner")
    repo = match.group("repo")
    sha = match.group("sha")

    api_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"

    try:
        with urllib.request.urlopen(api_url) as response:
            if response.status != 200:
                print(
                    f"Failed to fetch commit info. HTTP status code: {response.status}",
                    file=sys.stderr,
                )
                sys.exit(1)
            raw_data = response.read()
        data = json.loads(raw_data)
    except Exception as e:
        print(f"Error fetching data from GitHub API: {e}", file=sys.stderr)
        sys.exit(1)

    files = data.get("files", [])
    if not files:
        print("No files found in this commit or invalid commit data.", file=sys.stderr)
        sys.exit(0)

    for f in files:
        filename = f["filename"]
        raw_url = f["raw_url"]

        dirname = os.path.dirname(filename)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname, exist_ok=True)

        try:
            with urllib.request.urlopen(raw_url) as resp:
                if resp.status != 200:
                    print(
                        f"Failed to download file {filename}. HTTP status code: {resp.status}",
                        file=sys.stderr,
                    )
                    continue
                content = resp.read()
        except Exception as e:
            print(f"Error downloading file {filename}: {e}", file=sys.stderr)
            continue

        existed = os.path.exists(filename)
        try:
            with open(filename, "wb") as out_file:
                out_file.write(content)
            if existed:
                print(f"Overwritten: {filename}")
            else:
                print(f"Writen: {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
