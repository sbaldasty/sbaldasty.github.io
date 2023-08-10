from _lib import gallery, thumbnail

path = 'posts/information-theory/'

thumbnail(path, 'PXL_20230809_184047322',
    x=400, y=500, width=1000, angle=0)

gallery(f'{path}textbook', 'PXL_20230809_184047322',
    x=0, y=0, width=2980, angle=0)

gallery(f'{path}uvm-campus', 'IMG_20200303_175151',
    x=200, y=0, width=2900, angle=0)
