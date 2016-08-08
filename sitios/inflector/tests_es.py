#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2006 Bermi Ferrer Martinez
#
# bermi a-t bermilabs - com
#
import unittest
from inflector import Inflector
from rules.spanish import Spanish


class SpanishInflectorTestCase(unittest.TestCase):
    singular_to_plural = {
        "restaurante": "restaurantes",
        "postre": "postres",
    }

    def setUp(self):
        self.inflector = Inflector(Spanish)

    def tearDown(self):
        self.inflector = None

    def test_pluralize(self):
        for singular, plural in self.singular_to_plural.iteritems():
            print "Plur:", self.inflector.pluralize(singular), "Sing:", self.inflector.singularize(plural)



InflectorTestSuite = unittest.TestSuite()
InflectorTestSuite.addTest(SpanishInflectorTestCase("test_pluralize"))
runner = unittest.TextTestRunner()
runner.run(InflectorTestSuite)
