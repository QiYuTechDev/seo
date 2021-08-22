import os
import sys

version = os.getenv('VERSION')
if version.startswith("v"):
    version = version[1:]
print(f"release {version=}")

prefix = "b2 download-file-by-name qiyutechseo"
mac_cmd = f"""{prefix} "{version}/darwin/zip/darwin/x64/seo-darwin-x64-{version}.zip" mac.zip"""
win_cmd = f"""{prefix} "{version}/win32/squirrel.windows/x64/seo-{version} Setup.exe" seo_setup.exe"""
deb_cmd = f"""{prefix} "{version}/linux/deb/x64/seo_{version}_amd64.deb" seo_amd64.deb"""
rpm_cmd = f"""{prefix} "{version}/linux/rpm/x64/seo-{version}-1.x86_64.rpm" seo.x86_64.rpm"""


def print_and_run(cmd: str):
    print(f"{cmd=}")
    ok = os.system(cmd)
    if ok != 0:
        sys.exit(ok)

for cmd in [mac_cmd, win_cmd, deb_cmd, rpm_cmd]:
    print_and_run(cmd)
