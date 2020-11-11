# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['application.py'],
             pathex=['/Users/Fin/Documents/csvThings/csv_convert_final'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='application',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

app = BUNDLE(exe,
          name='csv_to_qlab.app',
          icon='icon(big).icns',
          bundle_identifier=None,
          info_plist={
             'NSPrincipalClass': 'NSApplication',
             'NSAppleScriptEnabled': False,
             'CFBundleDocumentTypes': [
                 {
                     'CFBundleTypeName': 'My File Format',
                     'CFBundleTypeIconFile': 'MyFileIcon.icns',
                     'LSItemContentTypes': ['com.example.myformat'],
                     'LSHandlerRank': 'Owner'
                     }
                 ]
             },
          )
