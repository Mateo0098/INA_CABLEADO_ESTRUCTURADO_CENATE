param()

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$excelDir = Join-Path $root '06_excel'
$packageDir = Join-Path $root '08_entrega/ENTREGA_FINAL_INA_CENATE/01_EXCEL'
$evidenceDir = Join-Path $root '09_auditorias/evidencias/Excel_COM'
$template = Get-ChildItem -LiteralPath $excelDir -Filter 'Plantilla*.xlsx' |
    Where-Object { $_.Name -notmatch 'TRABAJO' } | Select-Object -First 1 -ExpandProperty FullName
$sourceOutput = Join-Path $excelDir 'INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx'
$deliveryOutput = Join-Path $packageDir 'INA_CENATE_ACTIVIDAD_1_COMPLETADA.xlsx'
$backup = Join-Path $evidenceDir 'INA_CENATE_ACTIVIDAD_1_COMPLETADA_DEFECTUOSO_2026-10-25.xlsx'
$testCopy = Join-Path $evidenceDir 'INA_CENATE_ACTIVIDAD_1_COMPLETADA_EXCEL_COM_TEST.xlsx'
$staging = Join-Path $excelDir 'INA_CENATE_ACTIVIDAD_1_COMPLETADA_REGENERANDO.xlsx'

if (-not (Test-Path -LiteralPath $template)) { throw 'No se encontró la plantilla original INA.' }
if (-not (Test-Path -LiteralPath $sourceOutput) -or -not (Test-Path -LiteralPath $deliveryOutput)) {
    throw 'No se encontraron las dos copias defectuosas esperadas para respaldar.'
}
if (Test-Path -LiteralPath $testCopy) { throw "La copia de prueba ya existe y no se sobrescribirá: $testCopy" }
if ((Get-FileHash -Algorithm SHA256 $sourceOutput).Hash -ne (Get-FileHash -Algorithm SHA256 $deliveryOutput).Hash) {
    throw 'Las copias defectuosas de origen y entrega no coinciden; se detiene para preservar ambas.'
}
if (Test-Path -LiteralPath $staging) { throw "Ya existe el archivo de trabajo: $staging" }

New-Item -ItemType Directory -Force -Path $evidenceDir | Out-Null
if (-not (Test-Path -LiteralPath $backup)) {
    Copy-Item -LiteralPath $sourceOutput -Destination $backup
} elseif ((Get-FileHash -Algorithm SHA256 $backup).Hash -ne (Get-FileHash -Algorithm SHA256 $sourceOutput).Hash) {
    throw 'El respaldo existente no coincide con la versión defectuosa actual.'
}

# Toma los datos ya aprobados de la fuente Fase 3B; Excel crea y escribe el XLSX.
$python = (Get-Command python -ErrorAction Stop).Source
$extract = "import base64,json,runpy; d=runpy.run_path(r'$root\09_auditorias\crear_excel_fase3b.py'); print(base64.b64encode(json.dumps({'materials':d['MATERIALS'],'tools':d['TOOLS'],'notes':d['NOTES']},ensure_ascii=False).encode('utf-8')).decode('ascii'))"
$encoded = & $python -c $extract
if ($LASTEXITCODE -ne 0 -or -not $encoded) { throw 'No se pudieron recuperar los datos del generador Fase 3B.' }
$payload = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(($encoded -join '').Trim())) | ConvertFrom-Json

$excel = $null
$workbook = $null
$testWorkbook = $null
$autoFillFormulasInLists = $null
try {
    $excel = New-Object -ComObject Excel.Application
    $excel.Visible = $false
    $excel.DisplayAlerts = $false
    $excel.AskToUpdateLinks = $false
    $excelVersion = [string]$excel.Version
    # The template's materials range is an Excel Table. Suppress its calculated-column
    # autofill only for this instance, then restore the user's prior value in finally.
    $autoFillFormulasInLists = [bool]$excel.AutoCorrect.AutoFillFormulasInLists
    $excel.AutoCorrect.AutoFillFormulasInLists = $false

    $workbook = $excel.Workbooks.Open($template, 0, $false)
    if ($workbook.Worksheets.Count -ne 2) { throw 'La plantilla no abrió con sus dos hojas originales.' }
    $materialsSheet = $workbook.Worksheets.Item(1)
    $toolsSheet = $workbook.Worksheets.Item(2)

    $materialsSheet.Range('A2:K41').ClearContents()
    for ($i = 0; $i -lt $payload.materials.Count; $i++) {
        $record = $payload.materials[$i]
        $row = $i + 2
        $materialsSheet.Cells.Item($row, 1).Value2 = $record.name
        $materialsSheet.Cells.Item($row, 2).Value2 = $record.category
        $materialsSheet.Cells.Item($row, 3).Value2 = $record.specification
        $materialsSheet.Cells.Item($row, 4).Value2 = $record.brand
        $materialsSheet.Cells.Item($row, 5).Value2 = $record.model
        $materialsSheet.Cells.Item($row, 6).Value2 = $record.unit
        $materialsSheet.Cells.Item($row, 7).Formula = '=' + $record.formula
        $materialsSheet.Cells.Item($row, 8).Value2 = $record.supplier
        # I/J no reciben precios ni fórmulas monetarias.
        $materialsSheet.Cells.Item($row, 11).Value2 = $record.source
    }

    $materialsSheet.Range('A43').Value2 = [string]::Concat('CANTIDADES DE MATERIALES ', [char]0x2014, ' SIN COSTOS')
    $materialsSheet.Range('J43').ClearContents()
    for ($i = 0; $i -lt $payload.notes.Count; $i++) {
        $row = 45 + $i
        $note = $payload.notes[$i]
        $target = $materialsSheet.Range("A$row`:K$row")
        $styleSource = switch ([int]$note[1]) {
            11 { $materialsSheet.Range('A43') }
            3 { $materialsSheet.Range('A2') }
            8 { $materialsSheet.Range('A3') }
        }
        $styleSource.Copy()
        [void]$target.PasteSpecial(-4122) # xlPasteFormats; preserves INA cell formats.
        [void]$excel.CutCopyMode
        $target.Merge()
        $materialsSheet.Cells.Item($row, 1).Value2 = [string]$note[0]
        $materialsSheet.Cells.Item($row, 1).WrapText = $true
        $materialsSheet.Rows.Item($row).RowHeight = if ($row -eq 45) { 30 } else { 42 }
    }

    $toolsSheet.Range('A2:B41').ClearContents()
    for ($i = 0; $i -lt $payload.tools.Count; $i++) {
        $row = $i + 2
        $tool = $payload.tools[$i]
        $toolsSheet.Cells.Item($row, 1).Value2 = [string]$tool[0]
        if ($tool[1] -is [int] -or $tool[1] -is [long]) {
            $toolsSheet.Cells.Item($row, 2).Formula = '=' + [string]$tool[1]
        } else {
            $toolsSheet.Cells.Item($row, 2).Value2 = [string]$tool[1]
        }
    }

    $workbook.ForceFullCalculation = $true
    $excel.CalculateFullRebuild()
    $workbook.SaveAs($staging, 51) # xlOpenXMLWorkbook
    $workbook.Close($false)
    $workbook = $null

    # Excel itself reopens the staged file, evaluates formulas and saves a test copy.
    $testWorkbook = $excel.Workbooks.Open($staging, 0, $true)
    if ($testWorkbook.Worksheets.Count -ne 2) { throw 'El XLSX regenerado no conserva las dos hojas.' }
    $checkSheet = $testWorkbook.Worksheets.Item(1)
    for ($i = 0; $i -lt $payload.materials.Count; $i++) {
        $row = $i + 2
        $cell = $checkSheet.Cells.Item($row, 7)
        $expected = [double]$payload.materials[$i].value
        if ([string]$cell.Formula -eq '') { throw "Falta fórmula en G$row." }
        if ([Math]::Abs([double]$cell.Value2 - $expected) -gt 0.000001) {
            throw "Valor Excel inesperado en G${row}: $($cell.Value2), se esperaba $expected."
        }
    }
    for ($i = 0; $i -lt ($payload.tools.Count - 1); $i++) {
        $row = $i + 2
        $cell = $testWorkbook.Worksheets.Item(2).Cells.Item($row, 2)
        if ([Math]::Abs([double]$cell.Value2 - [double]$payload.tools[$i][1]) -gt 0.000001) {
            throw "Valor Excel inesperado en herramientas B${row}: $($cell.Value2)."
        }
    }
    for ($row = 2; $row -le 41; $row++) {
        foreach ($column in 9, 10) {
            $priceCell = $checkSheet.Cells.Item($row, $column)
            if ([string]$priceCell.Formula -ne '' -or [string]$priceCell.Value2 -ne '') { throw "Se encontró contenido de precio en $($priceCell.Address())." }
        }
    }
    if ([string]$checkSheet.Range('J43').Formula -ne '' -or [string]$checkSheet.Range('J43').Value2 -ne '') { throw 'J43 conserva contenido monetario.' }
    if ([string]$checkSheet.Range('A43').Value2 -notlike '*SIN COSTOS*') { throw 'No se sustituyó el rótulo monetario.' }
    $testWorkbook.SaveCopyAs($testCopy)
    $testWorkbook.Close($false)
    $testWorkbook = $null

    # Segunda apertura, esta vez de la copia de prueba solicitada.
    $testWorkbook = $excel.Workbooks.Open($testCopy, 0, $true)
    if ($testWorkbook.Worksheets.Count -ne 2) { throw 'Excel no reabrió la copia de prueba.' }
    $testWorkbook.Close($false)
    $testWorkbook = $null
} finally {
    if ($testWorkbook) { $testWorkbook.Close($false) }
    if ($workbook) { $workbook.Close($false) }
    if ($excel) {
        if ($null -ne $autoFillFormulasInLists) {
            $excel.AutoCorrect.AutoFillFormulasInLists = $autoFillFormulasInLists
        }
        $excel.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($excel)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

# Validación de esquema OOXML oficial de Microsoft, además de las aperturas COM.
$openXmlDll = 'C:\Program Files\Microsoft Office\root\vfs\ProgramFilesX86\Microsoft Office\Office16\DCF\DocumentFormat.OpenXml.dll'
if (-not (Test-Path -LiteralPath $openXmlDll)) { throw 'No se encontró Open XML SDK local para validación estructural.' }
Add-Type -Path $openXmlDll
$document = [DocumentFormat.OpenXml.Packaging.SpreadsheetDocument]::Open($testCopy, $false)
try {
    $schemaErrors = @([DocumentFormat.OpenXml.Validation.OpenXmlValidator]::new().Validate($document))
    if ($schemaErrors.Count -ne 0) {
        $schemaErrors | ForEach-Object { Write-Output ("OOXML_ERROR=" + $_.Id + '; ' + $_.Description) }
        throw "Open XML SDK encontró $($schemaErrors.Count) errores de esquema."
    }
} finally { $document.Dispose() }

# Solo después de que Excel y Open XML SDK aceptaron el archivo se sustituyen ambos destinos.
Copy-Item -LiteralPath $testCopy -Destination $sourceOutput -Force
Copy-Item -LiteralPath $testCopy -Destination $deliveryOutput -Force
if ((Get-FileHash -Algorithm SHA256 $sourceOutput).Hash -ne (Get-FileHash -Algorithm SHA256 $deliveryOutput).Hash) {
    throw 'Las copias finales no coinciden byte a byte.'
}

$finalExcel = $null
$finalBook = $null
try {
    $finalExcel = New-Object -ComObject Excel.Application
    $finalExcel.Visible = $false
    $finalExcel.DisplayAlerts = $false
    $finalBook = $finalExcel.Workbooks.Open($deliveryOutput, 0, $true)
    if ($finalBook.Worksheets.Count -ne 2) { throw 'Excel no abrió la ruta final del paquete.' }
    Write-Output ('FINAL_OPEN_OK=' + $finalBook.Name + '; SHEETS=' + $finalBook.Worksheets.Count)
} finally {
    if ($finalBook) { $finalBook.Close($false) }
    if ($finalExcel) {
        $finalExcel.Quit()
        [void][Runtime.InteropServices.Marshal]::ReleaseComObject($finalExcel)
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

Remove-Item -LiteralPath $staging
Write-Output ('EXCEL_VERSION=' + $excelVersion)
Write-Output ('TEST_COPY=' + $testCopy.Substring($root.Length + 1))
Write-Output ('DEFECT_BACKUP=' + $backup.Substring($root.Length + 1))
Write-Output ('FINAL_SHA256=' + (Get-FileHash -Algorithm SHA256 $deliveryOutput).Hash)
