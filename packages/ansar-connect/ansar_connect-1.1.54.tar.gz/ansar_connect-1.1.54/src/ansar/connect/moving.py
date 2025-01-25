# Author: Scott Woods <scott.18.ansar@gmail.com>
# MIT License
#
# Copyright (c) 2017-2024 Scott Woods
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
'''.

.
'''
__docformat__ = 'restructuredtext'

import ansar.create as ar

__all__ = [
	'overlay',
]

def overlay(self, source, target, selected_source=False, empty_target=True, blacklist=None):
	'''Copy values of matching names, where target value is empty.'''
	if not ar.is_message(source) or not ar.is_message(target):
		s = ar.tof(source)
		t = ar.tof(target)
		self.warning(f'Cannot overlay "{s}" on "{t}" - something not a bound type.')
		return
	s = source.__art__.value
	t = target.__art__.value
	for k, v in s.items():
		if k not in s or k not in t:
			continue
		if blacklist and k in blacklist:
			continue
		a = getattr(source, k, None)
		b = getattr(target, k, None)
		if selected_source and a is None:
			continue
		if empty_target and b is not None:
			continue
		setattr(target, k, a)
