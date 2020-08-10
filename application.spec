# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['application.py'],
             pathex=['/Users/Fin/Documents/csvThings/csv_convert_final'],
             binaries=[],
             datas=[('templates', 'templates'), ('static', 'static'), ('csv_convert.py', '.')],
             hiddenimports=[],
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
          name='application',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='application')
app = BUNDLE(coll,
             name='csv_to_qlab.app',
             icon='icon(big).icns',
             bundle_identifier=None)