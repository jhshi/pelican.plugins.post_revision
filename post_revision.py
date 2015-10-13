
import subprocess
from pelican import signals


def generate_post_revision(generator):
  pages = []
  pages += getattr(generator, 'articles', [])
  pages += getattr(generator, 'pages', [])
  for page in pages:
    path = getattr(page, 'source_path', None)
    if path is None:
      continue
    try:
      output = subprocess.check_output('git log --format="%%ai|%%s" %s'\
          % (path), shell=True)
      commits = []
      for line in output.split('\n'):
        line = line.strip()
        if len(line) == 0:
          continue
        parts = line.split('|')
        date, msg = parts[0], '|'.join(parts[1:])
        commits.append((date, msg))
      setattr(page, 'commits', commits)
    except:
      continue


def register():
  signals.article_generator_finalized.connect(generate_post_revision)
  signals.page_generator_finalized.connect(generate_post_revision)
