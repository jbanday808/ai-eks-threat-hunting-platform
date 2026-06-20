rule Remcos_Combined_Static_IOC
{
    meta:
        description = "Detects Remcos RAT using validated static indicators"
        malware_family = "Remcos RAT"
        version = "2.0"
        sha256 = "a6ccd89558c4b5cd2fec2512b846e14620be2cb3489f85b99203a9e4b9751d6a"

    strings:
        // UPX packer markers
        $packer1 = "UPX0" ascii
        $packer2 = "UPX1" ascii
        $packer3 = "UPX!" ascii

        // Windows API indicators
        $api1 = "LoadLibraryA" ascii
        $api2 = "GetProcAddress" ascii
        $api3 = "VirtualAlloc" ascii
        $api4 = "URLDownloadToFileA" ascii
        $api5 = "InternetOpenA" ascii

    condition:
        uint16(0) == 0x5A4D and
        filesize < 100KB and
        2 of ($packer*) and
        3 of ($api*)
}
