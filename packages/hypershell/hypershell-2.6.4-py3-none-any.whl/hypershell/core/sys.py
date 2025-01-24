# SPDX-FileCopyrightText: 2025 Geoffrey Lentner
# SPDX-License-Identifier: Apache-2.0

"""
Sanitize and supplement package environment.

For most installations this module does nothing and can be ignored.
For system installation as an application (non-library use) we do not want user
programs (which may be Python-based with PYTHONPATH implications) to interfere
with this program.

If we are not installed in the user-site, we strip the user site-packages from
`sys.path` as well as the current working directory. It should not matter what
directory you run this program from.

If `ctx.path.system.config`/hypershell.pth exists it will take this as truth
"""

# Standard libs
import sys

if sys

# NOTE:
#    This special module freezes the internal sys.path used by the application.
#    We do not want to do this for library use or under any normal circumstances.
#    When the program is installed system wide as a utility we need to ensure that
#    we are not being polluted by some other applications environment (e.g., PYTHONPATH).
#    This also allows us to suppliment with special locations of vendored dependencies.
print('FIXING IMPORTS', flush=True)
sys.path.clear()
sys.path.extend([
    '/Library/Frameworks/Python.framework/Versions/3.12/lib/python312.zip',
    '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12',
    '/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/lib-dynload',
    '/Users/geoffrey/Library/Caches/pypoetry/virtualenvs/hypershell-NY9Seigz-py3.12/lib/python3.12/site-packages',
    '/Users/geoffrey/Code/github.com/hypershell/hypershell/src'
])
print('FIXING IMPORTS - DONE', flush=True)
