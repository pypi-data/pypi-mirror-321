import os
import sys
from datetime import datetime, timedelta
from subprocess import run, PIPE, STDOUT
from pathlib import Path

from IPython.core.getipython import get_ipython


def install_from_file_on_colab(installer_path: Path):
    """
    Download and run a constructor-like installer, patching
    the necessary bits so it works on Colab right away.

    This will restart your kernel as a result!

    Parameters
    ----------
    installer_url
        URL pointing to a ``constructor``-like installer, such
        as Miniconda or Mambaforge
    """
    prefix = "/usr/local"
    t0 = datetime.now()
    installer_fn = installer_path
    print("📦 Installing...")
    task = run(
        ["bash", installer_fn, "-bfp", str(prefix)],
        check=False,
        stdout=PIPE,
        stderr=STDOUT,
        text=True,
    )
    os.unlink(installer_fn)
    with open("condacolab_install.log", "w") as f:
        f.write(task.stdout)
    assert (
        task.returncode == 0
    ), "💥💔💥 The installation failed! Logs are available at `/content/condacolab_install.log`."

    prefix = Path(prefix)
    pymaj, pymin = sys.version_info[:2]

    with open(prefix / ".condarc", "a") as f:
        f.write("always_yes: true\n")

    with open("/etc/ipython/ipython_config.py", "a") as f:
        f.write(
            f"""\nc.InteractiveShellApp.exec_lines = [
                    "import sys",
                    "sp = f'{prefix}/lib/python{pymaj}.{pymin}/site-packages'",
                    "if sp not in sys.path:",
                    "    sys.path.insert(0, sp)",
                ]
            """
        )
    sitepackages = f"{prefix}/lib/python{pymaj}.{pymin}/site-packages"
    if sitepackages not in sys.path:
        sys.path.insert(0, sitepackages)

    print("🩹 Patching environment...")
    env = {}
    bin_path = f"{prefix}/bin"
    if bin_path not in os.environ.get("PATH", "").split(":"):
        env["PATH"] = f"{bin_path}:{os.environ.get('PATH', '')}"
    env["LD_LIBRARY_PATH"] = f"{prefix}/lib:{os.environ.get('LD_LIBRARY_PATH', '')}"

    os.rename(sys.executable, f"{sys.executable}.real")
    with open(sys.executable, "w") as f:
        f.write("#!/bin/bash\n")
        envstr = " ".join(f"{k}={v}" for k, v in env.items())
        f.write(f"exec env {envstr} {sys.executable}.real -x $@\n")
    run(["chmod", "+x", sys.executable])

    try:
        import google.colab  # type: ignore #noqa: F401

        run(
            "cp -r /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py /usr/local/lib/python3.10/dist-packages/google-2.0.3.dist-info /usr/local/lib/python3.10/dist-packages/google_colab-1.0.0.dist-info /usr/local/lib/python3.11/site-packages",
            shell=True,
        )
        run(
            "cp -r /usr/local/lib/python3.10/dist-packages/google/* /usr/local/lib/python3.11/site-packages/google",
            shell=True,
        )
        run(
            """sed -i "s/from IPython.utils import traitlets as _traitlets/import traitlets as _traitlets/" /usr/local/lib/python3.11/site-packages/google/colab/*.py""",
            shell=True,
        )
        run(
            """sed -i "s/from IPython.utils import traitlets/import traitlets/" /usr/local/lib/python3.11/site-packages/google/colab/*.py""",
            shell=True,
        )
        run(
            """/usr/local/bin/python -m pip install ipython traitlets jupyter psutil matplotlib setuptools ipython_genutils ipykernel jupyter_console prompt_toolkit httplib2 astor google-auth==2.27.0 ipyparallel==8.8.0 pandas==2.2.2 portpicker==1.5.2 ipykernel==5.5.6 ipython==7.34.0 notebook==6.5.5 requests==2.32.3 tornado==6.3.3""",
            shell=True,
        )
    except ImportError:
        raise RuntimeError("This module must ONLY run as part of a Colab notebook!")
    run(
        r"""sed -i 's|/usr/bin/python3\.real|/usr/local/bin/python|g' /usr/bin/python3""",
        shell=True,
    )
    run("""/usr/local/bin/python -m pip install turboml-sdk""", shell=True)
    taken = timedelta(seconds=round((datetime.now() - t0).total_seconds(), 0))
    print(f"⏲ Done in {taken}")

    print("🔁 Restarting kernel...")
    ipython = get_ipython()
    if ipython is None:
        raise RuntimeError("This module must ONLY run as part of a Colab notebook!")
    ipython.kernel.do_shutdown(True)  # type: ignore


install_from_file_on_colab("turboml-0.1-Linux-x86_64.sh")
