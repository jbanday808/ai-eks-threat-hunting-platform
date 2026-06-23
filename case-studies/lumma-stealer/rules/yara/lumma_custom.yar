rule Lumma_Stealer_Credential_Theft_Strings
{
    meta:
        description = "Detects Lumma Stealer-like credential theft and browser password collection strings"
        author = "James Banday"
        purpose = "Defensive malware detection"
        sample_included = false

    strings:
        $chromium_keys = "main.GetChromiumMasterKeys" ascii wide
        $chrome_logins = "main.getChromeLogins" ascii wide
        $edge_logins = "main.getEdgeLogins" ascii wide
        $password_decrypt = "main.loginPBE.Decrypt" ascii wide
        $lsass_discovery = "main.findLsassProcess" ascii wide
        $enable_privilege = "main.enablePrivilege" ascii wide
        $dpapi = "main.DPAPI" ascii wide

    condition:
        uint16(0) == 0x5A4D and
        4 of them
}
