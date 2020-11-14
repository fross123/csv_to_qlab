# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['application.py'],
             pathex=['.'],
             binaries=[],
             datas=[
               ('static', 'static'),
               ('templates', 'templates'),
             ],
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
          name='csv_to_qlab',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='csv_to_qlab')
app = BUNDLE(coll,
             name='csv_to_qlab.app',
             icon='icon(big).icns',
             bundle_identifier=None,
             info_plist={
                'NSPrincipalClass': 'NSApplication',
                'NSAppleScriptEnabled': False,
                'CFBundleDocumentTypes': [
                    {
                        'CFBundleTypeName': 'CSV to QLab',
                        'CFBundleTypeIconFile': 'icon(big).icns',
                        'LSHandlerRank': 'Owner'
                        }
                    ]
                },
             )
