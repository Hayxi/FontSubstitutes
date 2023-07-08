import fontforge

FONT_DIR = '输入更纱黑体字体文件所在路径'
COPYRIGHT = 'Copyright (c) 2015-2023, Renzhi Li (aka. Belleve Invis, belleve@typeof.net). Portions Copyright (c) 2016-2020 The Inter Project Authors. Portions Copyright (c) 2014, 2015 Adobe Systems Incorporated (http://www.adobe.com/). Portions Copyright (c) 2012 Google Inc.'

def open_font(path):
    return fontforge.open(path)

def remove_gasp(font):
    font.gasp = ()

def set_cleartype(font):
    font.head_optimized_for_cleartype = 1

def get_version(font):
    return font.version

def set_gothic_normal_names(font):
    font.fontname = 'MicrosoftYaHei-Extralight'
    font.familyname = 'Microsoft YaHei Xlight'
    font.fullname = 'Microsoft YaHei Xlight'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Xlight'),
        ('Chinese (PRC)', 'SubFamily', 'Regular'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Extralight'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Xlight'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Extralight'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Xlight'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Extralight'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Xlight'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Extralight')
    )

def set_ui_normal_names(font):
    font.fontname = 'MicrosoftYaHeiUI-Extralight'
    font.familyname = 'Microsoft YaHei UI Xlight'
    font.fullname = 'Microsoft YaHei UI Xlight'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Xlight'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Extralight'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Xlight'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Extralight')
    )

def set_gothic_italic_names(font):
    font.fontname = 'MicrosoftYaHei-ExtralightItalic'
    font.familyname = 'Microsoft YaHei Xlight'
    font.fullname = 'Microsoft YaHei Xlight Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑 Xlight'),
        ('Chinese (PRC)', 'SubFamily', 'Italic'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Extralight Italic'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Xlight Italic'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Extralight Italic'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei Xlight'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Extralight Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Xlight Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Extralight Italic')
    )

def set_ui_italic_names(font):
    font.fontname = 'MicrosoftYaHeiUI-ExtralightItalic'
    font.familyname = 'Microsoft YaHei UI Xlight'
    font.fullname = 'Microsoft YaHei UI Xlight Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI Xlight'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Extralight Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Xlight Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Extralight Italic')
    )

def gen_normal():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-extralight.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_normal_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-extralight.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_normal_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhxl.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_italic():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-extralightitalic.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_italic_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-extralightitalic.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_italic_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhxli.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_normal()
    gen_italic()
