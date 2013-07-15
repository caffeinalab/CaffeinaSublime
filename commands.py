import datetime
import sublime
import sublime_plugin

settings = sublime.load_settings('Caffeina.sublime-settings')


class CaffeinaAddSignatureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        global settings
        self.view.run_command("insert_snippet", {"contents": "/**\n * Caffeina srl\n * @author {user}\n * @date {date}\n */\n".format(user=settings.get('developer', 'developer@caffeinalab.com'), date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))})
