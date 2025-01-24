""" Unit tests for astblick """

# Copyright (C) 2021 Gwyn Ciesla

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import getpass
import tempfile
import configparser
from OpenSSL import crypto

import astblick


def test_humansize():
    """Test conversion of bytes to more human readable units"""
    assert astblick.humansize(102814) == "100.40K"


def test_dfree():
    """Test disk free space function"""
    assert isinstance(astblick.dfree("."), int)


def test_homesub():
    """Test homedir ~ substitution"""
    assert (
        astblick.homesub("~/.astblick.conf")
        == os.path.expanduser("~" + getpass.getuser()) + "/.astblick.conf"
    )


def test_config_handler():
    """Ensure that the generated config is what we expect."""

    handle, path = tempfile.mkstemp()  # pylint: disable=unused-variable
    testconf = astblick.config_handler(path)  # pylint: disable=unused-variable
    config = configparser.ConfigParser()
    config.read(path)
    os.unlink(path)

    assert str(config.get("Options", "database")) == "~/.astblick.db"
    assert str(config.get("Options", "ip")) == "127.0.0.1"
    assert int(config.get("Options", "port")) == 8080
    assert str(config.get("Options", "refresh")) == "900"
    assert str(config.get("Options", "key")) == "~/.astblick_key.pem"
    assert str(config.get("Options", "cert")) == "~/.astblick_cert.pem"
    assert str(config.get("Options", "tempdir")) == "0"


def test_create_certs():
    """Test that we're creating valid key/certificate pairs."""
    khandle, kpath = tempfile.mkstemp()  # pylint: disable=unused-variable
    os.unlink(kpath)
    chandle, cpath = tempfile.mkstemp()  # pylint: disable=unused-variable
    os.unlink(cpath)

    status = astblick.create_certs(kpath, cpath)

    assert status == 0

    with open(kpath, "r", encoding="utf-8") as keyfile:
        keycontent = keyfile.read()
    key = crypto.load_privatekey(crypto.FILETYPE_PEM, keycontent)
    assert isinstance(key, crypto.PKey) is True
    os.unlink(kpath)

    with open(cpath, "r", encoding="utf-8") as certfile:
        certcontent = certfile.read()
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, certcontent)
    assert isinstance(cert, crypto.X509) is True
    os.unlink(cpath)
