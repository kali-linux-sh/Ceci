#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__autor__ = u'Juan Beresiarte'

from escaner import Scanner
from antivirus import Antivirus
import functions

program = Antivirus()
escaner = Scanner(program)
program.init__(escaner, functions)
program.run()