param([string]$Out, [int]$Width = 2400)
Add-Type -AssemblyName System.Drawing
Add-Type @"
using System;
using System.Runtime.InteropServices;
public static class Clip {
  [DllImport("user32.dll")] public static extern bool OpenClipboard(IntPtr h);
  [DllImport("user32.dll")] public static extern bool CloseClipboard();
  [DllImport("user32.dll")] public static extern IntPtr GetClipboardData(uint fmt);
  [DllImport("gdi32.dll")] public static extern IntPtr CopyEnhMetaFile(IntPtr h, IntPtr file);
}
"@
if (-not [Clip]::OpenClipboard([IntPtr]::Zero)) { throw "clipboard busy" }
try {
  $h = [Clip]::GetClipboardData(14)   # CF_ENHMETAFILE
  if ($h -eq [IntPtr]::Zero) { throw "no EMF on clipboard" }
  $copy = [Clip]::CopyEnhMetaFile($h, [IntPtr]::Zero)
} finally { [void][Clip]::CloseClipboard() }

$mf = New-Object System.Drawing.Imaging.Metafile($copy, $true)
$ratio = $mf.Height / $mf.Width
$w = $Width; $hgt = [int]($Width * $ratio)
$bmp = New-Object System.Drawing.Bitmap($w, $hgt)
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode = 'AntiAlias'; $g.TextRenderingHint = 'AntiAliasGridFit'
$g.Clear([System.Drawing.Color]::White)
$g.DrawImage($mf, 0, 0, $w, $hgt)
$g.Dispose()
$bmp.Save($Out, [System.Drawing.Imaging.ImageFormat]::Png)
"saved $Out ${w}x$hgt"
