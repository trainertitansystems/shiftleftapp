from vertexai.preview.generative_models import GenerativeModel
import subprocess

def git(cmd):
    return subprocess.check_output(cmd, shell=True).decode()

changed_files = git("git diff --name-only origin/main").splitlines()
unit_tests = git("git log -1 --format=%cd autoscale_demo/tests/unit").strip()
integration_tests = git("git log -1 --format=%cd autoscale_demo/tests/integration").strip()

prompt = f"""
Changed files: {changed_files}

Last unit test update: {unit_tests}
Last integration test update: {integration_tests}

Check if tests align with changes.
Highlight risks.
"""

model = GenerativeModel("gemini-1.5-pro")
response = model.generate_content(prompt)

print(response.text)

