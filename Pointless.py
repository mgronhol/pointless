#!/usr/bin/env python

# Class for autocurrying
class CurriedFunc(object):
	def __init__( self, N, func, args ):
		self.args = args
		self.N = N
		self.func = func
	
	def __call__(self, *args ):
		new_args = list(self.args) + list(args)
		if len( new_args ) < self.N:
			return CurriedFunc( self.N, self.func, new_args )
		else:
			return self.func( *new_args )


def curry( N ):
	def wrapper( func ):
		return CurriedFunc( N, func, [] )
	return wrapper

@curry( N = 2 )
def map( func, values ):
	return [func(value) for value in values]


@curry( N = 2)
def compose( A, B ):
	def composed( *args, **kwargs ):
		result = B(*args, **kwargs)
		
		# recursive compose if result is callable
		if hasattr(result, '__call__'):
			return compose( A, result )
			
		return A( result )
	return composed
 
 
# example:
#
# sum_over = compose(sum, map)
# sum_over_squares = sum_over( lambda x:x**2 )
#
# print sum_over_squares([1,2,3])



