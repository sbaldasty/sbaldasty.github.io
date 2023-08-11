from _lib import gallery, thumbnail

path = 'posts/museum-of-printing/'

thumbnail(path, 'PXL_20221126_175155653',
    x=100, y=300, width=2600, angle=0)

gallery(f'{path}old-computers', 'PXL_20221126_174651546',
    x=1150, y=1000, width=1400, angle=-3)

gallery(f'{path}typewriters', 'PXL_20221126_174306210',
    x=100, y=600, width=2600, angle=0)

gallery(f'{path}newer-printing-press', 'PXL_20221126_175155653',
    x=100, y=600, width=2600, angle=0)

gallery(f'{path}color-printer', 'PXL_20221126_174908628',
    x=0, y=400, width=2600, angle=0)

gallery(f'{path}printing-my-name', 'PXL_20221126_172357021',
    x=0, y=300, width=3000, angle=0)

gallery(f'{path}ancient-chinese-printing', 'PXL_20221126_165727027',
    x=500, y=1450, width=500, angle=0)

gallery(f'{path}ornate-printing-press', 'PXL_20221126_161110320',
    x=500, y=1450, width=2000, angle=-2)

gallery(f'{path}bible-page', 'PXL_20221126_160441124',
    x=500, y=1300, width=800, angle=0)

gallery(f'{path}colored-bible-illustration', 'PXL_20221126_160531323',
    x=550, y=0, width=3400, angle=-90)
