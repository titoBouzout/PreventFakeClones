# coding=utf8
import sublime, sublime_plugin
import os.path as op

def normalize(path):
	return op.normcase(op.normpath(op.realpath(path)))

class prevent_fake_clones_listener(sublime_plugin.EventListener):
	def on_load(self, maybe_fake_clone):

		# Prevent Fake Clones
		breaky = False
		path = maybe_fake_clone.file_name()
		if path:
			path = normalize(maybe_fake_clone.file_name())
			for window in sublime.windows():
				for _view in window.views():
					if _view.id() != maybe_fake_clone.id() and not _view.is_loading() and _view.file_name() and _view.buffer_id() != maybe_fake_clone.buffer_id() and path == normalize(_view.file_name()):
						maybe_fake_clone.window().focus_view(maybe_fake_clone)
						maybe_fake_clone.window().run_command('close')

						# ahhhhhhhhh!!!!
						_view.window().focus_view(_view)
						_view.window().run_command('focus_neighboring_group')
						_view.window().focus_view(_view)
						_view.window().run_command('clone_file')
						# sublime.error_message('Preventing opening an already opened file(a "fake" clone), focusing already opened file.')
						breaky = True
						break;
				if breaky:
					break




