from _lib import gallery, thumbnail

path = 'posts/time-release-lock/'

thumbnail(path, 'PXL_20221002_141246819',
    x=0, y=400, width=3000, angle=0)

gallery(f'{path}box', 'PXL_20221001_205305534',
    x=0, y=1150, width=2980, angle=0)

gallery(f'{path}open', 'PXL_20221002_141006336',
    x=1000, y=1020, width=2900, angle=75)

gallery(f'{path}closed', 'PXL_20221002_141246819',
    x=0, y=200, width=3000, angle=0)

gallery(f'{path}usb', 'PXL_20230527_171458849',
    x=1650, y=2150, width=1500, angle=150)
