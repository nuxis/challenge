# FIXME: Refactor settings structure, using -environ or -decouple or some other solution that is nicer than noqa

# if not specified, go for dev settings

from challenge.settings.base import *  # noqa: F403
from challenge.settings.dev import *  # noqa: F403
