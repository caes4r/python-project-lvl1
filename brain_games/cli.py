"""Command line interface."""


import prompt  # import.


def welcome_user():
	"""Name request."""
	name = prompt.string('May I have your name? ')
	print('Hello, {}!'.format(name))
