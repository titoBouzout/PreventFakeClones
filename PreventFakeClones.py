# coding=utf8
import sublime, sublime_plugin
import os.path as op

def normalize(path):
	return op.normcase(op.normpath(op.realpath(path)))

class prevent_fake_clones_listener(sublime_plugin.EventListener):

	def on_load(self, view):

		# Prevent Fake Clones
		if view.file_name():
			path = normalize(view.file_name())
			window = view.window()
			for _window in sublime.windows():
				for _view in _window.views():
					if _view.id() != view.id() and not _view.is_loading() and _view.file_name() and _view.buffer_id() != view.buffer_id() and path == normalize(_view.file_name()):
						window.focus_view(view)
						window.run_command('close')

						# ahhhhhhhhh!!!!
						_window.focus_view(_view)
						_window.run_command('focus_neighboring_group')
						_window.focus_view(_view)
						_window.run_command('clone_file')
						sublime.error_message('Preventing opening an already opened file(aka "fake" clone), focusing already opened file....')
						return