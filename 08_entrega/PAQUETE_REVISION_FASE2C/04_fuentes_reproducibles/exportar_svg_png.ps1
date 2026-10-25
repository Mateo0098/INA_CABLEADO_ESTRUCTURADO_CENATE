param(
    [string]$ChromePath = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
)

$ErrorActionPreference = 'Stop'
$repo = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$source = Join-Path $repo '07_imagenes\fase2b'
$profile = Join-Path $repo '.render_profile_fase2b'

if (-not (Test-Path -LiteralPath $ChromePath)) {
    throw "No se encontró Chrome en $ChromePath"
}

New-Item -ItemType Directory -Path $profile -Force | Out-Null
foreach ($svg in Get-ChildItem -LiteralPath $source -Filter '*.svg' | Sort-Object Name) {
    $png = [System.IO.Path]::ChangeExtension($svg.FullName, '.png')
    $uri = [System.Uri]::new($svg.FullName).AbsoluteUri
    $args = @(
        '--headless=new', '--disable-gpu', '--disable-software-rasterizer', '--no-sandbox',
        '--hide-scrollbars', '--window-size=1600,1000', "--user-data-dir=$profile",
        "--screenshot=$png", $uri
    )
    $process = Start-Process -FilePath $ChromePath -ArgumentList $args -WindowStyle Hidden -Wait -PassThru
    if ($process.ExitCode -ne 0 -or -not (Test-Path -LiteralPath $png)) {
        throw "Falló la exportación de $($svg.Name)"
    }
}

$resolvedProfile = (Resolve-Path -LiteralPath $profile).Path
if (-not $resolvedProfile.StartsWith($repo, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Ruta temporal fuera del repositorio: $resolvedProfile"
}
Remove-Item -LiteralPath $resolvedProfile -Recurse -Force
Write-Output "Exportados $((Get-ChildItem -LiteralPath $source -Filter '*.png').Count) PNG."
