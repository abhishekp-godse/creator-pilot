# CreatorPilot Built-in Windows HTTP Server
# Runs natively on all Windows PCs using built-in .NET (No Python or Node.js required!)

$port = 3000
$root = $PSScriptRoot
if (-not $root) { $root = "c:\creator pilot" }

$listener = New-Object System.Net.HttpListener
$prefix = "http://localhost:$port/"
$listener.Prefixes.Add($prefix)

try {
    $listener.Start()
} catch {
    Write-Host "[ERROR] Could not start server on port $port. Is another server running?" -ForegroundColor Red
    Write-Host $_.Exception.Message
    Pause
    exit
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   CreatorPilot Local Server Active on http://localhost:$port" -ForegroundColor Green
Write-Host "   Keep this window open while using the application!" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

# Open default browser automatically
Start-Process "http://localhost:$port/preview_dashboard.html"

# Serve requests
while ($listener.IsListening) {
    try {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response

        $localPath = $request.Url.LocalPath.TrimStart('/')
        if ([string]::IsNullOrWhiteSpace($localPath) -or $localPath -eq '/') {
            $localPath = "preview_dashboard.html"
        }

        # Normalize path
        $filePath = Join-Path $root $localPath

        if (Test-Path $filePath -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($filePath)
            
            # Set content types
            if ($filePath.EndsWith(".html")) {
                $response.ContentType = "text/html; charset=utf-8"
            } elseif ($filePath.EndsWith(".js")) {
                $response.ContentType = "application/javascript; charset=utf-8"
            } elseif ($filePath.EndsWith(".css")) {
                $response.ContentType = "text/css; charset=utf-8"
            } elseif ($filePath.EndsWith(".json")) {
                $response.ContentType = "application/json; charset=utf-8"
            } elseif ($filePath.EndsWith(".png")) {
                $response.ContentType = "image/png"
            } else {
                $response.ContentType = "application/octet-stream"
            }

            # Enable CORS and Cache
            $response.AddHeader("Access-Control-Allow-Origin", "*")
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
            $response.StatusCode = 200
        } else {
            $response.StatusCode = 404
            $errBytes = [System.Text.Encoding]::UTF8.GetBytes("File Not Found: $localPath")
            $response.OutputStream.Write($errBytes, 0, $errBytes.Length)
        }

        $response.OutputStream.Close()
    } catch {
        # Continue loop on connection reset
    }
}
