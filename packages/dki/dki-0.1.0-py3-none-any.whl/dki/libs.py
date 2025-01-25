import pathlib
import sys
import os
import subprocess


default_path = pathlib.Path("~/.config/deployments").expanduser()


def has_deployments() -> bool:
  return default_path.exists()


def build_image(template: str, name: str):
  """considering context is the current directory"""
  image_name = f"{name}:latest"
  template_dir = default_path / template
  dockerfile = template_dir / "Dockerfile"
  context = "."

  if (template_dir / "check.py").exists():
    res = subprocess.run(
      [
        "python",
        template_dir / "check.py",
      ],
      cwd=context,
    )
    if res.returncode != 0:
      print('Check files failed, please check the files in the context directory.')
      sys.exit(1)

  subprocess.run(
    [
      "docker",
      "build",
      "-t",
      image_name,
      "-f",
      dockerfile,
      context,
    ],
    cwd=context,
  )


def download_deployment():
  subprocess.run(
    [
      "git",
      "clone",
      "https://github.com/svtter/deployments.git",
      default_path,
    ]
  )


def pull_deployment(branch: str = "main"):
  subprocess.run(
    [
      "git",
      "pull",
      "origin",
      branch,
    ],
    cwd=default_path,
  )
