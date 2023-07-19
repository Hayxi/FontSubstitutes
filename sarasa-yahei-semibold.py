import fontforge

FONT_DIR = '输入更纱黑体字体文件所在路径'
COPYRIGHT = 'Copyright (c) 2015-2023, Renzhi Li (aka. Belleve Invis, belleve@typeof.net). Portions Copyright (c) 2016-2020 The Inter Project Authors. Portions Copyright (c) 2014, 2015 Adobe Systems Incorporated (http://www.adobe.com/). Portions Copyright (c) 2012 Google Inc.'

def open_font(path):
    return fontforge.open(path)

def get_version(font):
    return font.version

def set_gothic_normal_names(font):
    font.fontname = 'MicrosoftYaHei-Semibold'
    font.familyname = 'Microsoft YaHei Semibold'
    font.fullname = 'Microsoft YaHei Semibold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Semibold'),
        ('Chinese (PRC)', 'SubFamily', 'Regular'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Semibold'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Semibold'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Semibold'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Semibold'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Semibold'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Semibold'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Semibold')
    )

def set_ui_normal_names(font):
    font.fontname = 'MicrosoftYaHeiUI-Semibold'
    font.familyname = 'Microsoft YaHei UI Semibold'
    font.fullname = 'Microsoft YaHei UI Semibold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Semibold'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Semibold'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Semibold'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Semibold')
    )

def set_gothic_italic_names(font):
    font.fontname = 'MicrosoftYaHei-SemiboldItalic'
    font.familyname = 'Microsoft YaHei Semibold'
    font.fullname = 'Microsoft YaHei Semibold Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Semibold'),
        ('Chinese (PRC)', 'SubFamily', 'Italic'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Semibold Italic'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Semibold Italic'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Semibold Italic'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Semibold'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Semibold Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Semibold Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Semibold Italic')
    )

def set_ui_italic_names(font):
    font.fontname = 'MicrosoftYaHeiUI-SemiboldItalic'
    font.familyname = 'Microsoft YaHei UI Semibold'
    font.fullname = 'Microsoft YaHei UI Semibold Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Semibold'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Semibold Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Semibold Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Semibold Italic')
    )

def gen_normal():
    font = open_font(FONT_DIR + 'sarasa-gothic-sc-semibold.ttf')
    set_gothic_normal_names(font)

    font_ui = open_font(FONT_DIR + 'sarasa-ui-sc-semibold.ttf')
    set_ui_normal_names(font_ui)

    font.generateTtc(FONT_DIR + 'msyhsb.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_italic():
    font = open_font(FONT_DIR + 'sarasa-gothic-sc-semibolditalic.ttf')
    set_gothic_italic_names(font)

    font_ui = open_font(FONT_DIR + 'sarasa-ui-sc-semibolditalic.ttf')
    set_ui_italic_names(font_ui)

    font.generateTtc(FONT_DIR + 'msyhsbi.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_normal()
    gen_italic()
