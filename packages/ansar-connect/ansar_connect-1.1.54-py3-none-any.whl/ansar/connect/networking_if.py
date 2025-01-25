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
__docformat__ = 'restructuredtext'

import ansar.create as ar

__all__ = [
    'UseAddress',
    'AddressBook',
    'NoAddress',
	'GlareTimer',
]

#
#
class UseAddress(object):
	"""Utility message. Pass an address to the receiver.

	:param address: the address to pass
	:type address: tuple
	"""
	def __init__(self, address=None):
		self.address = address

class AddressBook(object):
	"""Utility message. Pass a map of named addresses to the receiver.

	:param kw: the map of names and addresses
	:type kw: dict
	"""
	def __init__(self, **kw):
		self.book = kw

ar.bind(UseAddress, object_schema={'address': ar.Address()})
ar.bind(AddressBook, object_schema={'book': ar.MapOf(ar.Unicode, ar.Address())})

#
#
class NoAddress(object): pass

ar.bind(NoAddress)


#
#
class GlareTimer(object):
	pass

ar.bind(GlareTimer)
