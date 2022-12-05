#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import logging
logging.root.setLevel(logging.INFO)
logging.getLogger('pelican.utils').setLevel(logging.WARN)  # avoids very verbose "-> Copying ..." logs

SITENAME = 'Hôpitaux À Défendre : Clinique Tondu @ Bordeaux'
SITESUBTITLE = 'Suivi de la lutte des soignants de la clinique Tondu à Bordeaux'

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR.utf8'  # impacts date format; must be installed with sudo dpkg-reconfigure locales

THEME = '../html5-dopetrope'
DISPLAY_HOMEPAGE_ON_MENU = True
MENUITEMS = (
    ('Liens', '#footer'),
)
DISABLE_LATEST_ARTICLES= True

ABOUT_TEXT = '''
Lancée le 25 octobre, la grève des personnels soignants et administratifs de la clinique du Tondu à Bordeaux, a duré 2 semaines. Ils obtiennent entre 50 et 80 € brut de plus sur la fiche de paie. Bien loin des revendications initiales. Le malaise persiste.
<br>
Ce site web vise à servir de <b>revue de presse</b> pour couvrir cette mobilisation.
'''
# "Open Graph tags do not acknowledge <base>, and should always have full absolute URLs" - https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base
META_IMAGE = 'images/logo-NouvelleCLiniqueBordeauxTondu.webp'
META_IMAGE_TYPE = 'image/jpeg'
ABOUT_IMAGE = META_IMAGE

LINKS = (
    ("Cagnotte leetchi - Soignants du Tondu maltraités", "https://www.leetchi.com/c/soignants-du-tondu-maltraites"),
    ("Tweets @RevPermanente à propos de la clinique du Tondu", "https://nitter.lacontrevoie.fr/RevPermanente/search?q=tondu"),
    ("Sources de ce site web @GitHub", "https://github.com/hopitaux-a-defendre/clinique-tondu-bordeaux"),
)

CUSTOM_CSS = '''
#footer img {
  background: rgba(255,255,255,0.9);
  border-radius: 1rem;
  padding: 2rem;
}
'''

PATH = './content'
OUTPUT_PATH = './output'

MARKDOWN = {'output_format': 'html5'}

PLUGIN_PATHS = ('../pelican-plugins',)
PLUGINS = ('i18n_subsites', 'representative_image')#, 'w3c_validate')
logging.getLogger('i18n_subsites.i18n_subsites').setLevel(logging.DEBUG)
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'  # indicates the theme templates default language

# Disabling generation of unnecessary pages:
ARCHIVES_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''

CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None


#######################################
# Config options specific to dev-mode:
#######################################

SITEURL = ''
RELATIVE_URLS = True

# Making output generation faster:
STATIC_CHECK_IF_MODIFIED = True # create links instead of copying files
STATIC_CREATE_LINKS = True # compare mtimes of content and output files, and only copy content files that are newer than existing output files
LOAD_CONTENT_CACHE = True
CACHE_CONTENT = True
