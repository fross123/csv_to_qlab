# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['run_gui.py'],
             pathex=['.'],
             binaries=[],
             datas=[
               ('app/static', 'static'),
               ('app/templates', 'templates'),
               ('app/qlab_osc_config.json', '.'),
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
          name='csv-to-qlab',
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
               name='csv-to-qlab')
app = BUNDLE(coll,
             name='csv-to-qlab.app',
             icon='icon.icns',
             bundle_identifier=None,
             info_plist={
                'NSPrincipalClass': 'NSApplication',
                'NSAppleScriptEnabled': False,
                'CFBundleDocumentTypes': [
                    {
                        'CFBundleTypeName': 'CSV to QLab',
                        'CFBundleTypeIconFile': 'icon.icns',
                        'LSHandlerRank': 'Owner'
                        }
                    ]
                },
             )
