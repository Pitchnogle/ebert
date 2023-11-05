:: Batch script to synchronize Sony Music Center content with the NAS
::
:: Written by: Justin Hadella (pitchnogle@gmail.com)

set src_dir="C:\Users\justi\Music\Music Center"
set dst_dir="\\ebert\cd"

:: Copy all (newer) files from src_dir to dst_dir
xcopy %src_dir% %dst_dir% /v /s /e /d /y

@REM forfiles /p %src_dir% /s /m *.flac /c "cmd /c echo @relpath -- @fname"