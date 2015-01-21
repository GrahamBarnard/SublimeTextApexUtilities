import sublime, sublime_plugin

class SystemDebugCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				debug_start_text = "System.debug('" + self.view.substr(region) + ": ' + "
				debug_end_text = ");"
			elif sublime.get_clipboard():
				debug_start_text = "System.debug('" + sublime.get_clipboard() + ": ' + " + sublime.get_clipboard()
				debug_end_text = ");"
			else:			
	   			debug_start_text = "System.debug('"
	   			debug_end_text = ");"

			self.view.insert(edit, region.end(), debug_end_text)
			self.view.insert(edit, region.begin(), debug_start_text)