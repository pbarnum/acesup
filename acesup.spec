# -*- mode: python -*-

block_cipher = None


a = Analysis(['acesup'],
             pathex=['/home/p-trick/Projects/acesup'],
             binaries=[],
             datas=[],
             hiddenimports=["enum", "json"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='acesup',
          debug=False,
          strip=False,
          upx=True,
          console=True )