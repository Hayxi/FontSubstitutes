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
    font.fontname = 'MicrosoftYaHei'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'SubFamily', 'Regular'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Regular'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Regular'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Regular'),
        ('English (US)', 'Fullname', 'Microsoft YaHei'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Regular')
    )

def set_ui_normal_names(font):
    font.fontname = 'MicrosoftYaHeiUI'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Regular'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Regular'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Regular')
    )

def set_gothic_italic_names(font):
    font.fontname = 'MicrosoftYaHei-Italic'
    font.familyname = 'Microsoft YaHei'
    font.fullname = 'Microsoft YaHei Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('Chinese (PRC)', 'Family', '微软雅黑'),
        ('Chinese (PRC)', 'SubFamily', 'Italic'),
        ('Chinese (PRC)', 'UniqueID', '微软雅黑 Italic'),
        ('Chinese (PRC)', 'Fullname', '微软雅黑 Italic'),
        ('Chinese (PRC)', 'Preferred Family', '微软雅黑'),
        ('Chinese (PRC)', 'Preferred Styles', 'Italic'),
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei'),
        ('English (US)', 'Preferred Styles', 'Italic')
    )

def set_ui_italic_names(font):
    font.fontname = 'MicrosoftYaHeiUI-Italic'
    font.familyname = 'Microsoft YaHei UI'
    font.fullname = 'Microsoft YaHei UI Italic'
    font.version = get_version(font)
    font.copyright = COPYRIGHT
    font.sfnt_names = (
        ('English (US)', 'Copyright', COPYRIGHT),
        ('English (US)', 'Family', 'Microsoft YaHei UI'),
        ('English (US)', 'SubFamily', 'Italic'),
        ('English (US)', 'UniqueID', 'Microsoft YaHei UI Italic'),
        ('English (US)', 'Fullname', 'Microsoft YaHei UI Italic'),
        ('English (US)', 'Version', 'Version ' + get_version(font)),
        ('English (US)', 'Preferred Family', 'Microsoft YaHei UI'),
        ('English (US)', 'Preferred Styles', 'Italic')
    )

def gen_normal():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-regular.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_normal_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-regular.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_normal_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyh.ttc', font_ui, ttcflags = ('merge'), layer = 1)

def gen_italic():
    font = open_font(FONT_DIR + '/sarasa-gothic-sc-italic.ttf')
    remove_gasp(font)
    set_cleartype(font)
    set_gothic_italic_names(font)

    font_ui = open_font(FONT_DIR + '/sarasa-ui-sc-italic.ttf')
    remove_gasp(font_ui)
    set_cleartype(font_ui)
    set_ui_italic_names(font_ui)

    font.generateTtc(FONT_DIR + '/msyhi.ttc', font_ui, ttcflags = ('merge'), layer = 1)

if __name__ == '__main__':
    gen_normal()
    gen_italic()
