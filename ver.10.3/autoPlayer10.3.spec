# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['autoPlayer10.3.py'],
             pathex=['C:\\lkw\\python\\auto_Player'],
             binaries=[('chromedriver.exe', '.')],
             datas=[],
             hiddenimports=['selenium'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='autoPlayer10.3',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , uac_admin=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='autoPlayer10.3')
