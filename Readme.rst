Post Revision
#############

This Pelican plugin extracts the post's revision history from Git, and offer
several ``article`` and ``page`` attributes.


Settings
========

- ``GITHUB_URL``: the Github URL where the page source repository is hosted.
  For example: https://github.com/jhshi/blog_source

- ``PROJECT_ROOT``: Root directory of the Pelican project. You should set this
  to ``os.path.dirname(os.path.abspath(__file__))``. I don't know if Pelican
  offers in some for meta data, so let me know if that's the case and this
  settings is not necessary.
