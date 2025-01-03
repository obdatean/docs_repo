# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import shutil
import sphinx

import recommonmark
from recommonmark.transform import AutoStructify

# import sphinx_book_theme
# import sphinx_rtd_theme
# import furo


#choice theme default
# html_theme = 'sphinx_book_theme'
html_theme = 'sphinx_rtd_theme'
# html_theme = "furo"

# -- Project information -----------------------------------------------------

project = 'OrbbecSDK ROS2'
# project = """
# OrbbecSDK ROS2 documentation
# """
copyright = '2023, ORBBEC INC. www.orbbec.com.cn'
author = 'ORBBEC INC. www.orbbec.com.cn'


# -- General configuration ---------------------------------------------------
# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark',
  'sphinx_markdown_tables',

  'sphinx.ext.autosectionlabel',

#   'myst_parser',
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', 'rest', '.md', '.MD']


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language = 'zh_CN'
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# html_logo = "source/_static/orbbec_logo2.png"
# html_favicon = "source/_static/orbbec_logo2.png"

html_logo = "source/_static/orbbec-light_no_colour.svg"
html_favicon = "source/_static/web_html_logo.png"
# html_logo = "source/_static/orbbec_footerlogo_3d_world.svg"
# html_favicon = "source/_static/orbbec_footerlogo_3d_world.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['source/_static','source/image']

html_extra_path = ['source/image']

html_theme_options = {
    # 'analytics_id': 'G-EVD5Z6G6NH',
    'collapse_navigation': False,
    # 启用导航栏的“粘性”头部，这样导航栏会固定在页面顶部
    'sticky_navigation': True,
    # 配置导航栏的深度，-1 表示显示所有层级的标题
    'navigation_depth': 5,
    # 'show_navbar_depth': 4,
    # 导航栏显示+号
    'collapse_navigation': False,

    # 'analytics_anonymize_ip': False,
    # 'logo_only': False,
    # 'display_version': True,
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 5,
    # 'includehidden': True,
    # 'titles_only': False
}






# # 添加自定义的 JavaScript 文件
# html_js_files = ["theme.js"]


# #不需要添加_static目录，加了会不起作用
html_css_files = ["custom.css"]

# 与文档无关的其他资源的路径，由于无需构建此文件夹的文件，会自动忽略
# 默认情况下，此路径下的文件会输出到生成的html的根目录
# html_extra_path = ["_extra"]

# 在页面底部显示上一次更新于某某时间
html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

# 以下为 sphinx_book_theme 的主题配置/定制（sphinx_book_theme）
# html_theme_options = {
#    # ----------------主题内容中导航栏的功能按钮配置--------
#    # 添加存储库链接
#    "repository_url": "https://github.com/Eugene-Forest/NoteBook",
#    # 添加按钮以链接到存储库
#    "use_repository_button": True,
#    # 要添加按钮以打开有关当前页面的问题
#    "use_issues_button": True,
#    # 添加一个按钮来建议编辑
#    "use_edit_page_button": True,
#    # 默认情况下，编辑按钮将指向master分支，但如果您想更改此设置，请使用以下配置
#    "repository_branch": "main",
#    # 默认情况下，编辑按钮将指向存储库的根目录；而我们 sphinx项目的 doc文件其实是在 source 文件夹下的，包括 conf.py 和 index(.rst) 主目录
#    "path_to_docs": "source",
#    # 您可以添加 use_download_button 按钮，允许用户以多种格式下载当前查看的页面
#    "use_download_button": True,

#    # --------------------------右侧辅助栏配置---------
#    # 重命名右侧边栏页内目录名，标题的默认值为Contents。
#    "toc_title": "页内目录",
#    # 通常，右侧边栏页内目录中仅显示页面的第 2 级标题，只有当它们是活动部分的一部分时（在屏幕上滚动时），才会显示更深的级别。可以使用以下配置显示更深的级别，指示应显示多少级别
#    "show_toc_level": 2,

#    # --------------------------左侧边栏配置--------------
#    # logo 配置
#    "logo_only": True,
#    # 控制左侧边栏列表的深度展开,默认值为1，它仅显示文档的顶级部分
#    "show_navbar_depth": 1,
#    # 自定义侧边栏页脚,默认为 Theme by the Executable Book Project
#    # "extra_navbar": "<p>Your HTML</p>",
#    "home_page_in_toc": True,
#    # ------------------------- 单页模式 -----------------
#    # 如果您的文档只有一个页面，并且您不需要左侧导航栏，那么您可以 使用以下配置将其配置sphinx-book-theme 为以单页模式运行
#    # "single_page": True,
# }

# 是否显示页面下方的由sphinx创建, 默认为True
html_show_sphinx = False

# Function to copy video files to output directory
def setup(app):
    app.connect('build-finished', copy_videos)

def copy_videos(app, exception):
    if exception is None:  # Only copy if build succeeded
        src_dir = os.path.join(app.srcdir, '_static/videos')
        dest_dir = os.path.join(app.outdir, '_static/videos')
        if os.path.exists(src_dir):
            shutil.copytree(src_dir, dest_dir)

# 20201030
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)