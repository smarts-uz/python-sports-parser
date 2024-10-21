import os
import subprocess


def html_downloader(name_en, link, html_file_path):
    if os.path.exists(html_file_path):
        print(f"HTML for {name_en} already exists: {html_file_path} skip...")
    else:
        # Monolith yordamida HTML saqlash
        print(f"Saving HTML for {name_en}...")
        subprocess.run(["monolith", link, "-o", html_file_path], check=True)
        print(f"HTML saved for {name_en}: {html_file_path}")


