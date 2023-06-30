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
    font.fontname = 'MicrosoftYaHei-Light'
    font.familyname = 'Microsoft YaHei Light'
    font.fullname = 'Microsoft YaHei Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Light'),
        ('Chinese (PRC)', 'SubFamily', 'Regular'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Light'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Light'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Light'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Light'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Light'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Light'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Light')
    )

def set_ui_normal_names(font):
    font.fontname = 'MicrosoftYaHeiUI-Light'
    font.familyname = 'Microsoft YaHei UI Light'
    font.fullname = 'Microsoft YaHei UI Light'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Light'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Light'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Light'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Light')
    )

def set_gothic_italic_names(font):
    font.fontname = 'MicrosoftYaHei-LightItalic'
    font.familyname = 'Microsoft YaHei Light'
    font.fullname = 'Microsoft YaHei Light Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Light'),
        ('Chinese (PRC)', 'SubFamily', 'Italic'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Light Italic'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Light Italic'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Light Italic'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Light'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Light Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Light Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Light Italic')
    )

def set_ui_italic_names(font):
    font.fontname = 'MicrosoftYaHeiUI-LightItalic'
    font.familyname = 'Microsoft YaHei UI Light'
    font.fullname = 'Microsoft YaHei UI Light Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Light'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Light Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Light Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Light Italic')
    )

def gen_normal():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-light.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_normal_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-light.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_normal_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_italic():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-lightitalic.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_italic_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-lightitalic.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_italic_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhli.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_normal()
    gen_italic()
