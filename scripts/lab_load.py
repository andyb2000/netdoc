"""Blank the current database and load a specific scenario."""

from netdoc.tests.test import load_scenario

LAB_DIR = "netdoc/tests/netmiko_cisco_nxos/lab1"

load_scenario(LAB_DIR)
