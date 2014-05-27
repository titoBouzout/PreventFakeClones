# coding=utf8
import sublime, sublime_plugin
import os.path as op

def normalize(path):
	return op.normcase(op.normpath(op.realpath(path)))

class prevent_fake_clones_listener(sublime_plugin.EventListener):

	def on_load(self, view):
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
						# If the other view is not "dirty", then close it, and just let the user open the view that is opening.
						if not _view.is_dirty():
							self.focus_view(_view)
							_window.run_command('close')
							self.focus_view(view)
						else:
							# If the other view is "dirty" and in the same window, just focus it.
							if window == _window:
								self.focus_view(view)
								window.run_command('close')
								self.focus_view(_view)
							# If the other view is "dirty" and is in another window. Display the popup/statusbar message
							else:
								# close it
								window.run_command('close')

								self.focus_view(_view)
								sublime.status_message('Preventing opening an already opened file (aka "fake clone") Focusing already opened file...  Use: "File -> New File into View" which will open a real clone.')
						return

	def focus_view(self, view):
		window = view.window()
		window.focus_view(view)
		window.run_command('focus_neighboring_group')
		window.focus_view(view)