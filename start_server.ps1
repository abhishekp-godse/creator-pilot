# Native Windows Localhost Web Server
# Uses System.Net.Sockets.TcpListener - Requires ZERO Admin privileges and ZERO external software!

$port = 8080
$root = $PSScriptRoot
if (-not $root) { $root = "c:\creator pilot" }

$ip = [System.Net.IPAddress]::Loopback
$listener = New-Object System.Net.Sockets.TcpListener($ip, $port)

try {
    $listener.Start()
} catch {
    Write-Host "[ERROR] Could not bind to port $port. Is another server running?" -ForegroundColor Red
    Pause
    exit
}

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "   CreatorPilot Local Server Running on http://localhost:$port" -ForegroundColor Green
Write-Host "   Access URL: http://localhost:$port" -ForegroundColor Yellow
Write-Host "   Keep this window open while using the application!" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

# Open default browser
Start-Process "http://localhost:$port"

while ($listener.Server.IsBound) {
    try {
        $client = $listener.AcceptTcpClient()
        $stream = $client.GetStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $writer = New-Object System.IO.StreamWriter($stream)
        
        $requestLine = $reader.ReadLine()
        if (-not $requestLine) {
            $client.Close()
            continue
        }

        # Parse request line: GET / HTTP/1.1
        $tokens = $requestLine.Split(" ")
        $url = if ($tokens.Length -gt 1) { $tokens[1] } else { "/" }
        $cleanPath = $url.Split("?")[0].TrimStart("/")
        if ([string]::IsNullOrWhiteSpace($cleanPath) -or $cleanPath -eq "/") {
            $cleanPath = "index.html"
        }

        $fullPath = Join-Path $root $cleanPath

        if (Test-Path $fullPath -PathType Leaf) {
            $contentBytes = [System.IO.File]::ReadAllBytes($fullPath)
            
            $contentType = "text/html; charset=utf-8"
            if ($fullPath.EndsWith(".js")) { $contentType = "application/javascript" }
            elseif ($fullPath.EndsWith(".css")) { $contentType = "text/css" }
            elseif ($fullPath.EndsWith(".json")) { $contentType = "application/json" }
            elseif ($fullPath.EndsWith(".png")) { $contentType = "image/png" }

            $header = "HTTP/1.1 200 OK`r`n" +
                      "Content-Type: $contentType`r`n" +
                      "Content-Length: $($contentBytes.Length)`r`n" +
                      "Access-Control-Allow-Origin: *`r`n" +
                      "Connection: close`r`n`r`n"
            
            $headerBytes = [System.Text.Encoding]::ASCII.GetBytes($header)
            $stream.Write($headerBytes, 0, $headerBytes.Length)
            $stream.Write($contentBytes, 0, $contentBytes.Length)
        } else {
            $notFound = "HTTP/1.1 404 Not Found`r`nContent-Length: 9`r`nConnection: close`r`n`r`nNot Found"
            $errBytes = [System.Text.Encoding]::ASCII.GetBytes($notFound)
            $stream.Write($errBytes, 0, $errBytes.Length)
        }

        $writer.Flush()
        $client.Close()
    } catch {
        # Continue loop on connection reset
    }
}
