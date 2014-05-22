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
					# check if the file is already opened
					if (
						_view.file_name() and # if the view has a file name
						_view.id() != view.id() and # if the view is different and not the same that we just opened
						_view.buffer_id() != view.buffer_id() and # if the buffer is not the same (if is not a real clone)
						path == normalize(_view.file_name()) # if the path of the file matches exactly
					) :
						# close it
						window.focus_view(view)
						window.run_command('close')

						# focus the first instance
						_window.focus_view(_view)
						_window.run_command('focus_neighboring_group')
						_window.focus_view(_view)
						_window.run_command('clone_file')
						sublime.error_message('Preventing opening an already opened file (aka "fake clone")\nFocusing already opened file....\n\nUse: "File -> New File into View" which will open a real clone.')
						return