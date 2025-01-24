#!/usr/bin/env python3
import sys
import os
import re
import urllib.request
import json
import argparse
import tempfile
import zipfile
import shutil


def fetch_json(url):
    """단순화한 JSON fetch 함수"""
    try:
        with urllib.request.urlopen(url) as resp:
            if resp.status != 200:
                print(
                    f"Error: HTTP status code {resp.status} for URL: {url}",
                    file=sys.stderr,
                )
                return None
            data = resp.read()
        return json.loads(data)
    except Exception as e:
        print(f"Error fetching JSON from {url}: {e}", file=sys.stderr)
        return None


def download_and_write_file(raw_url, filename):
    """raw_url에서 파일을 다운로드해 filename에 기록"""
    try:
        with urllib.request.urlopen(raw_url) as resp:
            if resp.status != 200:
                print(
                    f"Failed to download file {filename} (status: {resp.status})",
                    file=sys.stderr,
                )
                return
            content = resp.read()
    except Exception as e:
        print(f"Error downloading {filename}: {e}", file=sys.stderr)
        return

    existed = os.path.exists(filename)
    dirname = os.path.dirname(filename)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)

    try:
        with open(filename, "wb") as out_file:
            out_file.write(content)
        if existed:
            print(f"Overwritten: {filename}")
        else:
            print(f"Write: {filename}")
    except Exception as e:
        print(f"Error writing {filename}: {e}", file=sys.stderr)


def download_commit_zip(owner, repo, sha):
    """
    해당 커밋의 zip을 다운로드하여 현재 디렉토리에 압축 해제.
    이미 존재하는 파일은 Overwritten, 새 파일이면 Write 로 표기.
    """
    zip_url = f"https://github.com/{owner}/{repo}/archive/{sha}.zip"
    try:
        with urllib.request.urlopen(zip_url) as resp:
            if resp.status != 200:
                print(
                    f"Failed to download zip file (status: {resp.status})",
                    file=sys.stderr,
                )
                return False
            zip_data = resp.read()
    except Exception as e:
        print(f"Error downloading zip file: {e}", file=sys.stderr)
        return False

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, "commit.zip")
        # zip 파일 저장
        try:
            with open(zip_path, "wb") as zf:
                zf.write(zip_data)
        except Exception as e:
            print(f"Error writing temp zip file: {e}", file=sys.stderr)
            return False

        # 압축 풀기
        try:
            with zipfile.ZipFile(zip_path, "r") as z:
                z.extractall(tmpdir)
        except Exception as e:
            print(f"Error extracting zip file: {e}", file=sys.stderr)
            return False

        # zip을 풀면, 예: {repo}-{sha} 폴더가 생성됨
        # 해당 폴더 경로를 찾아서 모든 파일을 현재 디렉토리에 덮어쓰기
        extracted_dir = os.path.join(tmpdir, f"{repo}-{sha}")
        if not os.path.exists(extracted_dir):
            # 간혹 레포지토리명이 하이픈, 언더스코어 등 다른 형태일 수 있으므로
            # "repo-sha" 폴더를 찾지 못하면 폴더 탐색 로직을 도입해야 할 수도 있음
            # 여기서는 단순히 "{repo}-{sha}"라고 가정
            print(f"Extracted folder not found: {extracted_dir}", file=sys.stderr)
            return False

        # 이제 extracted_dir 안의 모든 파일·폴더를 현재 디렉토리로 옮김
        # 이미 존재하는 경우 Overwritten, 없으면 Write
        for root, dirs, files in os.walk(extracted_dir):
            for name in files:
                src_path = os.path.join(root, name)
                # 현재 디렉토리 내 최종 대상 경로 계산
                rel_path = os.path.relpath(src_path, extracted_dir)
                dst_path = os.path.join(".", rel_path)

                # 중간 디렉토리 생성
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)

                # 복사할 때 덮어씀
                existed = os.path.exists(dst_path)
                try:
                    shutil.copy2(src_path, dst_path)  # 메타데이터까지 복사
                    if existed:
                        print(f"Overwritten: {dst_path}")
                    else:
                        print(f"Write: {dst_path}")
                except Exception as e:
                    print(
                        f"Error copying {src_path} to {dst_path}: {e}", file=sys.stderr
                    )

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Apply a GitHub commit or full repo state to current directory."
    )
    parser.add_argument("commit_url", help="URL of the GitHub commit (required)")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Download all repo files at the commit SHA via zip (overwrites entire project)",
    )
    args = parser.parse_args()

    commit_url = args.commit_url
    pattern = r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/]+)/commit/(?P<sha>[0-9a-f]+)"
    match = re.search(pattern, commit_url)
    if not match:
        print("Invalid GitHub commit URL.", file=sys.stderr)
        sys.exit(1)

    owner = match.group("owner")
    repo = match.group("repo")
    sha = match.group("sha")

    if args.all:
        # 전체 zip 다운로드 -> 압축 해제 -> 현재 디렉토리에 덮어쓰기
        success = download_commit_zip(owner, repo, sha)
        if not success:
            print("Failed to apply full repo zip.", file=sys.stderr)
            sys.exit(1)
    else:
        # 변경된 파일만 적용
        commit_api_url = f"https://api.github.com/repos/{owner}/{repo}/commits/{sha}"
        commit_json = fetch_json(commit_api_url)
        if commit_json is None:
            print("Failed to fetch commit info.", file=sys.stderr)
            sys.exit(1)

        changed_files = commit_json.get("files", [])
        if not changed_files:
            print(
                "No files found in this commit, or invalid commit data.",
                file=sys.stderr,
            )
            sys.exit(0)

        for f in changed_files:
            filename = f["filename"]
            raw_url = f["raw_url"]
            download_and_write_file(raw_url, filename)


if __name__ == "__main__":
    main()
