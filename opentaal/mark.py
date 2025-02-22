"""Class definition for Mark."""


class Mark():
    """Class for exporting to markup languages such as HTML and Markdown."""

    @staticmethod
    def html_link(text: str,
                  url: str,
                  tooltip: str | None = None,
                  new: bool = False) -> str:
        """TODO.

        :param text: TODO.
        :param url: TODO.
        :param tooltip: TODO.
        :param new: TODO.
        :return: TODO.
        """
        if not new:
            if tooltip is None:
                return f'<a href="{url}">{text}</a>'
            return f'<a title="{tooltip}" href="{url}">{text}</a>'
        if tooltip is None:
            return f'<a target="_blank" href="{url}">{text}</a>'
        return f'<a target="_blank" title="{tooltip}" href="{url}">{text}</a>'

    @staticmethod
    def md_link(text: str,
                url: str,
                tooltip: str = None,
                new: bool = False) -> str:
        """TODO.

        :param text: TODO.
        :param url: TODO.
        :param tooltip: TODO.
        :param new: TODO.
        :return: TODO.
        """
        if not new and tooltip is None:
            return f'[{text}]({url})'
        return Mark.html_link(text=text, url=url, tooltip=tooltip, new=new)

    @staticmethod
    def html_head(title: str,
                  lang: str = 'nl',
                  style: str = None,
                  mono: bool = False) -> str:
        """TODO.

        :param title: TODO.
        :param lang: TODO.
        :param style: TODO.
        :param mono: TODO.
        :return: TODO.
        """
        if style is None:
            if mono:
                style = '''<style>
* {font-family: monospace, monospace;}
</style>
'''
            else:
                style = ''
        else:
            if mono:
                style = f'''<style>
* {{font-family: monospace, monospace;}}
{style}
</style>
'''
            else:
                style = f'''<style>
{style}
</style>
'''
        return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
{style}</head>
<body>
<h1>{title}</h1>
'''

    @staticmethod
    def md_head(title: str) -> str:
        """TODO.

        :param title: TODO.
        :return: TODO.
        """
        return f'''# {title}

'''

    @staticmethod
    def html_foot(footer: str = None) -> str:
        """TODO.

        :param footer: TODO.
        :return: TODO.
        """
        if footer is not None:
            return f'''<p><small>{footer}</small></p>
</body>
</html>
'''
        return '''</body>
</html>
'''

    @staticmethod
    def md_foot(footer: str = None) -> str:
        """TODO.

        :param footer: TODO.
        :return: TODO.
        """
        if footer is not None:
            return f'''
<small>{footer}</small>
'''
        return ''
