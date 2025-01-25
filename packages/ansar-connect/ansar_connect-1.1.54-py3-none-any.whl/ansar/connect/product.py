# Author: Scott Woods <scott.18.ansar@gmail.com>
# MIT License
#
# Copyright (c) 2017-2023 Scott Woods
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

""".

.
"""
__docformat__ = 'restructuredtext'

import ansar.connect as ar

__all__ = [
	'InstanceOfProduct',
	'ProductAccess',
	'ProductLookup',
	'YourProduct',
]

InstanceOfProduct = ar.Enumeration(DEVELOPMENT=1, TESTING=2, INTEGRATION=3,
	QA=4, STAGING=5, PRODUCTION=6,
	DEMONSTRATION=7, TRAINING=8, SALES=9,
	EVALUATION=10, OTHER=11)

#
#
class ProductAccess(object):
	def __init__(self, access_ipp=None, encrypted=False, product_name=None, product_instance=None):
		self.access_ipp = access_ipp or ar.HostPort()
		self.encrypted = encrypted
		self.product_name = product_name
		self.product_instance = product_instance

class ProductLookup(object):
	def __init__(self, product_name=None, product_instance=None):
		self.product_name = product_name
		self.product_instance = product_instance

class YourProduct(object):
	def __init__(self, address=None):
		self.address = address

INSTANT_SCHEMA = {
	"access_ipp": ar.UserDefined(ar.HostPort),
	"encrypted": ar.Boolean(),
	"product_name": ar.Unicode(),
	"product_instance": InstanceOfProduct,
	"address": ar.Address(),
}

ar.bind(ProductAccess, object_schema=INSTANT_SCHEMA)
ar.bind(ProductLookup, object_schema=INSTANT_SCHEMA)
ar.bind(YourProduct, object_schema=INSTANT_SCHEMA)
