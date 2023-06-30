import fontforge as ff

FONT_DIR = '输入字体所在路径，例如 C:/Fonts'
COPYRIGHT = 'Copyright (c) 2015-2023, Renzhi Li (aka. Belleve Invis, belleve@typeof.net). Portions Copyright (c) 2016-2020 The Inter Project Authors. Portions Copyright (c) 2014, 2015 Adobe Systems Incorporated (http://www.adobe.com/). Portions Copyright (c) 2012 Google Inc.'

def open_font(path):
    return ff.open(path)

def remove_gasp(font):
    font.gasp = ()

def set_cleartype(font):
    font.head_optimized_for_cleartype = 1

def get_version(font):
    return font.version

def set_gothic_normal_names(font):
    font.fontname = 'MicrosoftYaHei-Bold'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'SubFamily', 'Bold'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Bold'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Bold'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Bold'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Bold'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Bold'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Bold')
    )

def set_ui_normal_names(font):
    font.fontname = 'MicrosoftYaHeiUI-Bold'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Bold'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Bold'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Bold'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Bold')
    )

def set_gothic_italic_names(font):
    font.fontname = 'MicrosoftYaHei-BoldItalic'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Bold Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'SubFamily', 'Bold Italic'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Bold Italic'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Bold Italic'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Bold Italic'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Bold Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Bold Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Bold Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Bold Italic')
    )

def set_ui_italic_names(font):
    font.fontname = 'MicrosoftYaHeiUI-BoldItalic'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Bold Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Bold Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Bold Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Bold Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Bold Italic')
    )

def gen_normal():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-bold.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_normal_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-bold.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_normal_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhbd.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_italic():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-bolditalic.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_italic_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-bolditalic.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_italic_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhbdi.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_normal()
    gen_italic()
