import datetime, getpass
import sublime, sublime_plugin

class SystemDebugCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():

			if not region.empty():
				debug_start_text = "System.debug(LoggingLevel.ERROR, '" + self.view.substr(region).replace("'","").replace("+","") + ": ' + "
				debug_end_text = ");"
			elif sublime.get_clipboard():
				debug_start_text = "System.debug(LoggingLevel.ERROR, '" + sublime.get_clipboard().replace("'","").replace("+","") + ": ' + " + sublime.get_clipboard()
				debug_end_text = ");\n"
			else:			
	   			debug_start_text = "System.debug(LoggingLevel.ERROR, '"
	   			debug_end_text = ");"

			self.view.insert(edit, region.end(), debug_end_text)
			self.view.insert(edit, region.begin(), debug_start_text)

class SystemAssertCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				debug_start_text = "System.assertEquals(null, "
				debug_end_text = ");"
			elif sublime.get_clipboard():
				debug_start_text = "System.assertEquals(null"
				debug_end_text = ", " + sublime.get_clipboard() + ");"
			else:			
	   			debug_start_text = "System.assertEquals(null"
	   			debug_end_text = ", null);"

			self.view.insert(edit, region.end(), debug_end_text)
			self.view.insert(edit, region.begin(), debug_start_text)

class SystemAssertSizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				debug_start_text = "System.assertEquals(0, "
				debug_end_text = ".size());"
			elif sublime.get_clipboard():
				debug_start_text = "System.assertEquals(0"
				debug_end_text = ", " + sublime.get_clipboard() + ".size());"
			else:			
	   			debug_start_text = "System.assertEquals(0"
	   			debug_end_text = ", accounts.size());"

			self.view.insert(edit, region.end(), debug_end_text)
			self.view.insert(edit, region.begin(), debug_start_text)

class SystemNotAssertCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				debug_start_text = "System.assertNotEquals(null, "
				debug_end_text = ");"
			elif sublime.get_clipboard():
				debug_start_text = "System.assertNotEquals(null"
				debug_end_text = "," + sublime.get_clipboard() + ");"
			else:			
	   			debug_start_text = "System.assertNotEquals(null"
	   			debug_end_text = ",null);"

			self.view.insert(edit, region.end(), debug_end_text)
			self.view.insert(edit, region.begin(), debug_start_text)

class UserDebugOnlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        size = self.view.size()
        regions = self.view.find_all('USER_DEBUG')
        for region in regions:
	        self.view.insert(edit,self.view.text_point(1,0), str(region.size()))

class HeaderCommentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet", { "contents": "/**\n *  @description ${1:[description]}\n *  @author 	 Graham Barnard\n *  @date        %s${2:}\n */" %datetime.date.today().strftime("%Y-%m-%d") } )
