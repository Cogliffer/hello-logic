
if not exist "temp" mkdir "temp"

del /q "temp\*.html"

for %%f in (*.md) do (
    pandoc "%%f" -s --katex -o "temp\\%%~nf.html"
)

del /q "temp\*.pdf"

node convert-html-to-pdf.js

del /q "*.pdf"

node mergePdfs.js