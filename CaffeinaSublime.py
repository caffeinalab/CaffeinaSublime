import datetime

import sublime
import sublime_plugin


class CaffeinaAddSignatureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.settings = sublime.load_settings('CaffeinaSublime.sublime-settings')

        self.user = self.settings.get('developer', 'developer@caffeinalab.com')
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if sublime.score_selector(get_current_scope(), 'text.html'):
            self.view.run_command("insert_snippet", {"contents": "<!--\n | Caffeina srl\n | @author {user}\n | @date {date}\n -->\n".format(user=self.user, date=self.date)})
        else:
            self.view.run_command("insert_snippet", {"contents": "/**\n * Caffeina srl\n * @author {user}\n * @date {date}\n */\n".format(user=self.user, date=self.date)})


def get_current_scope():
    view = sublime.active_window().active_view()
    pt = view.sel()[0].begin()
    scope = 'text'

    if hasattr(view, 'scope_name'):
        scope = view.scope_name(pt)
    else:
        scope = view.syntax_name(pt)

    return scope
