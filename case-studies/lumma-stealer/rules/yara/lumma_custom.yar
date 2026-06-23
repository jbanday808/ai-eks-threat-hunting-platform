rule LummaStealer_Credential_Theft_Static_IOC
{
    meta:
        description = "Detects Lumma Stealer using confirmed credential theft and Chromium browser targeting strings"
        author = "James Banday"
        date = "2026-06-22"
        malware_family = "Lumma Stealer / SalatStealer"
        version = "1.4"
        reference = "https://github.com/jbanday808/ai-eks-threat-hunting-platform"
        sha256 = "3368d54f30631c9e305f6df3464e08b6b4f24eebdb605240c44b144deed717fa"
        md5 = "c83776891f0407e6401a7d7004691f86"

    strings:

        // Confirmed Lumma Stealer Credential Theft Strings
        $a1 = "main.getChromeLogins" ascii
        $a2 = "main.GetChromiumMasterKeys" ascii
        $a3 = "main.loginPBE.Decrypt" ascii

    condition:
        uint16(0) == 0x5A4D and
        2 of ($a*)
}
