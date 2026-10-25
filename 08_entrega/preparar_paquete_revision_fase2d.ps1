$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$package = Join-Path $PSScriptRoot 'PAQUETE_REVISION_FASE2D'
$images = Join-Path $package '01_imagenes_revision'
$support = Join-Path $package '02_soporte_tecnico'
$excel = Join-Path $package '03_excel_provisional'
$sources = Join-Path $package '04_fuentes_reproducibles'

foreach ($dir in @($images, $support, $excel, $sources)) {
    New-Item -ItemType Directory -Path $dir -Force | Out-Null
}

Copy-Item -Path (Join-Path $repo '07_imagenes\fase2b\*.svg') -Destination $images -Force
Copy-Item -Path (Join-Path $repo '07_imagenes\fase2b\*.png') -Destination $images -Force

$supportFiles = @(
    '04_calculos\MEMORIA_CALCULOS_FASE2D.md',
    '04_calculos\resultados_fase2d.csv',
    '05_materiales\MATRIZ_TECNICA_FASE2D.md',
    '08_entrega\GUIA_EXPOSICION_8_MIN_FASE2D.md'
)
foreach ($relative in $supportFiles) {
    Copy-Item -LiteralPath (Join-Path $repo $relative) -Destination $support -Force
}

$excelFiles = @(
    '06_excel\PLAN_TRANSFERENCIA_EXCEL_FASE2D.md',
    '06_excel\PLAN_FILAS_MATERIALES_FASE2D.csv',
    '06_excel\PLAN_FILAS_HERRAMIENTAS_FASE2D.csv'
)
foreach ($relative in $excelFiles) {
    Copy-Item -LiteralPath (Join-Path $repo $relative) -Destination $excel -Force
}
$workingBook = Get-ChildItem -LiteralPath (Join-Path $repo '06_excel') -Filter '*_TRABAJO_FASE2B.xlsx' | Select-Object -First 1
if ($null -eq $workingBook) { throw 'No se encontró la copia Excel de trabajo.' }
Copy-Item -LiteralPath $workingBook.FullName -Destination $excel -Force

$sourceFiles = @(
    '03_diseno\generar_diagramas_fase2b.py',
    '03_diseno\exportar_svg_png.ps1',
    '04_calculos\entradas_fase2d.csv',
    '04_calculos\modelo_calculos_fase2d.py'
)
foreach ($relative in $sourceFiles) {
    Copy-Item -LiteralPath (Join-Path $repo $relative) -Destination $sources -Force
}

$hashFile = Join-Path $package 'SHA256SUMS.csv'
$records = Get-ChildItem -LiteralPath $package -File -Recurse |
    Where-Object { $_.FullName -ne $hashFile } |
    Sort-Object FullName |
    ForEach-Object {
        [PSCustomObject]@{
            ruta = $_.FullName.Substring($package.Length + 1).Replace('\', '/')
            bytes = $_.Length
            sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName).Hash
        }
    }
$records | Export-Csv -LiteralPath $hashFile -NoTypeInformation -Encoding UTF8

Write-Output "Paquete preparado: $package"
Write-Output "Archivos con hash: $($records.Count)"
