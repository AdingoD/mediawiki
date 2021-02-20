"""
MediaWikiFile class module
"""

from .mediawikipage import MediaWikiPage


class MediaWikiFile(MediaWikiPage):
    """ MediaWiki File Instance, inheriting from the MediaWiki Page class

        Args:
            mediawiki (MediaWiki): MediaWiki class object from which to pull
            title (str): Title of file to retrieve (without the leading 'File:' namespace)
            pageid (int): MediaWiki site pageid to retrieve
            redirect (bool): **True:** Follow redirects
            preload (bool): **True:** Load most properties after getting page
            original_title (str): Not to be used from the caller; used to \
                                  help follow redirects
        Raises:
            :py:func:`mediawiki.exceptions.PageError`: if page provided does \
            not exist
        Raises:
            :py:func:`mediawiki.exceptions.DisambiguationError`: if page \
            provided is a disambiguation page
        Raises:
            :py:func:`mediawiki.exceptions.RedirectError`: if redirect is \
            **False** and the pageid or title provided redirects to another \
            page
        Warning:
            This should never need to be used directly! Please use \
            :func:`mediawiki.MediaWiki.file` """

    __slots__ = [
        "_file_url"
    ]

    def __init__(self, mediawiki, title=None, pageid=None, redirect=True, preload=False, original_title=""):
        super().__init__(mediawiki=mediawiki, title=title,
                         pageid=pageid, redirect=redirect, preload=preload, original_title=original_title)
        self._file_url = None

    @property
    def file_url(self):
        """ str: Direct URL to the file

            Note:
                Not settable """
        if self._file_url is None:
            params = {
                "prop": "imageinfo",
                "titles": self.title,
                "iiprop": "url"
            }
            raw_data = self.mediawiki.wiki_request(params=params)
            self._file_url = raw_data["query"]["pages"][self.pageid]["imageinfo"][0]["url"]
        return self._file_url
